import pandas as pd

import random
random.seed(7)
from datetime import datetime, timedelta

import urllib.parse
from dotenv import dotenv_values
from mysql.connector import connect

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

from fastapi import FastAPI, File, UploadFile, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
import uvicorn
import nest_asyncio
nest_asyncio.apply()

params = {'db':dotenv_values('TugasAkhir.env')}

db_user = params['db']['MYSQL_USERNAME']
db_password = urllib.parse.quote_plus(params['db']['MYSQL_PASSWORD'])
db_host = params['db']['MYSQL_HOST']
db_port = params['db']['MYSQL_PORT']
db_name = params['db']['MYSQL_DB']

# Buat koneksi ke database MySQL
SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, pool_pre_ping=True)

# Membuat tanggal acak
def random_tanggal():
    # Set the start and end dates
    start_date = datetime(2017, 1, 1)
    end_date = datetime(2022, 12, 17)
    # Generate a random date between the start and end dates
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    # Convert the random date to a string in the DD--MM-YYYY format
    formatted_date = random_date.strftime("%d-%m-%Y")
    return formatted_date

# Buat base class untuk ORM
Base = declarative_base()

try:
    # Buat tabel products
    class Products(Base):
        __tablename__ = 'products'
        product_id = Column(Integer, nullable=False)
        product_name = Column(String(50), primary_key=True)
        category = Column(String(50), nullable=False)
        sub_category = Column(String(50), nullable=False)

    # Buat tabel users
    class Users(Base):
        __tablename__ = 'users'
        customer_id = Column(Integer, nullable=False)
        name = Column(String(50), primary_key=True)
        city = Column(String(50), nullable=False)
        state = Column(String(50), nullable=False)
        postal = Column(Integer, nullable=False)

    # Buat tabel purchase
    class Purchase(Base):
        __tablename__ = 'purchase'
        name = Column(String(50), nullable=False, primary_key=True)
        date = Column(DateTime, nullable=False)
        product_name = Column(String(50), nullable=False, primary_key=True)
        quantity = Column(Integer, nullable=False)

    Base.metadata.create_all(engine)
except Exception as e:
    print(e)        

    
app = FastAPI()

# Buat Session
Session = sessionmaker(bind=engine)
session = Session()
conn = engine.connect()

def tabel_sql_jadi(users_csv,products_csv):
    df_users = pd.read_csv(users_csv.file)
    df_products = pd.read_csv(products_csv.file, sep=';', encoding='latin-1')
    df_products.columns = ['product_id', 'product_name', 'category', 'sub_category']

    n = 1000 #banyaknya kolom tabel purchase

    df_purchase = pd.DataFrame({'date':[random_tanggal() for i in range(n)],
                         'name':[random.choices(df_users['name'])[0] for i in range(n)], 
                         'product_name':[random.choices(df_products['product_name'])[0] for i in range(n)],
                         'quantity':[random.randint(1,25) for i in range(n)]
                        })
    
    count_users = session.query(sa.func.count(Users.name)).one()
    count_products = session.query(sa.func.count(Products.product_name)).one()
    count_purchase = session.query(sa.func.count(Purchase.product_name)).one()
    
    if count_users[0]==len(df_users) and count_products[0]==len(df_products) and count_purchase[0]==len(df_purchase):
        pass
    else:
        # Insert data ke tabel products
        df_products.to_sql('products', engine, if_exists='replace', index=False)

        # Insert data ke tabel users
        df_users.to_sql('users', engine, if_exists='replace', index=False)

        # Insert data ke tabel purchase
        df_purchase.to_sql('purchase', engine, if_exists='replace', index=False)
    

# process JWT
class Account(BaseModel):
    username_or_email: str
    password: str

# Misalnya kumpulan akun yang terdaftar tersimpan dalam database akun berikut
akun = [
    {
        "id": 7,
        "username": "Wisnu_D_Uzu",
        "email": "wisnu_D_uzu@gmail.com",
        "password": "wisnuduzu@"
    },
    {
        "id": 2,
        "username": "kucing_miauw",
        "email": "kucing_miauw@gmail.com",
        "password": "hachiko"
    },
    {
        "id": 17,
        "username": "uzumaki_nagato_tenshou",
        "email": "wisnuadipradana17@yahoo.com",
        "password": "0987654321A"
    }
]    

# in production you can use Settings management from pydantic to get secret key from .env
class Settings(BaseModel):
    authjwt_secret_key: str = "kucing"

# callback to get your configuration
@AuthJWT.load_config
def get_config():
    return Settings()

# exception handler for authjwt in production, you can tweak performance using or json response
@app.exception_handler(AuthJWTException)
async def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

# provide a method to create access tokens. The create_access_token() function is used to actually generate the token to use authorization later in endpoint protected
@app.post('/login')
async def login(acc: Account, Authorize: AuthJWT = Depends()):
    for i,isi in enumerate(akun):
        if (acc.username_or_email==isi['username'] or acc.username_or_email==isi['email']) and acc.password==isi['password']:
            # subject identifier for who this token is for example id or username from database
            access_token = Authorize.create_access_token(subject=acc.username_or_email,
                                                         fresh=True)
            data = {
            "token_access": access_token,
            "type" : "bearer"
                }
            return data
            pass
        if i==len(akun)-1:
            raise HTTPException(status_code=401, detail="Invalid username/email or password")
        

# protect endpoint with function jwt_required(), which requires a valid access token in the request headers to access.
@app.get('/user')
async def user(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    for isi in akun:
        if current_user == isi['username']:
            return isi


# Menyapa pada localhost awal
@app.get("/")
async def tugas_akhir():
    return {'Pesan': '''Halo, saya uzu.\n
                        Ini merupakan tugas akhir dari\n 
                        Sanbercode Python Backend Development'''}

# Menampilkan isi dari tabel (users, products, purchase)
@app.post("/tabel/{nama_tabel}")
async def tampilkan_isi_tabel(users_csv: UploadFile = File(...), 
                            products_csv: UploadFile = File(...),
                            nama_tabel = str,
                            Authorize: AuthJWT = Depends()
                         ):
    Authorize.jwt_required()
    
    tabel_sql_jadi(users_csv,products_csv)
    
    return conn.execute(f'select * from {nama_tabel.lower()}').all()

    session.commit()
    session.close()

# Menampilkan semua barang dengan urutan ascending (None, True, False)
@app.post("/barang")
async def tampilkan_barang(users_csv: UploadFile = File(...), 
                          products_csv: UploadFile = File(...),
                          sort_desc = None
                         ):
    tabel_sql_jadi(users_csv,products_csv)
    
    result = session.query(Products.product_name).all()
    
    produk = [i[0] for i in result]
    if sort_desc==None:
        pass
    elif sort_desc.lower() == 'true':
        produk.sort(reverse=False)
    elif sort_desc.lower() == 'false':
        produk.sort(reverse=True)
    return produk

    session.commit()
    session.close()

# Menampilkan semua barang yang bernama <nama_barang> dengan urutan ascending (None, True, False)
@app.post("/cari_nama_barang/{nama_barang}")
async def mencari_barang(users_csv: UploadFile = File(...), 
                          products_csv: UploadFile = File(...),
                          nama_barang = '',
                          sort_desc = None
                         ):
    tabel_sql_jadi(users_csv,products_csv)
    
    result = session.query(Products.product_name).all()

    produk = [i[0] for i in result]
    cari_barang = []
    for i in produk:
        try:
            if nama_barang.lower() in i.lower():
                 cari_barang.append(i)
        except:
            continue
        
    if sort_desc==None:
        pass
    elif sort_desc.lower() == 'true':
        cari_barang.sort(reverse=False)
    elif sort_desc.lower() == 'false':
        cari_barang.sort(reverse=True)
    return cari_barang

    session.commit()
    session.close()

# Menampilkan semua orang <nama_pembeli> berserta kota dan negaranya dengan urutan ascending (None, True, False)
@app.post("/pembeli")
async def tampilkan_tempat_tinggal_pembeli(users_csv: UploadFile = File(...), 
                                         products_csv: UploadFile = File(...),
                                         sort_desc = None,
                                         Authorize: AuthJWT = Depends()
                                         ):
    Authorize.jwt_required()
    
    tabel_sql_jadi(users_csv,products_csv)
    
    if sort_desc==None:
        result = (session.query(sa.distinct(Users.name), 
                            Users.city, 
                            Users.state))
    elif sort_desc=='true':
        result = (session.query(sa.distinct(Users.name), 
                            Users.city, 
                            Users.state)
        .order_by(Users.name.desc()))
    elif sort_desc=='false':
        result = (session.query(sa.distinct(Users.name), 
                            Users.city, 
                            Users.state)
        .order_by(Users.name.asc()))
    
    hasil = []
    for x, i in enumerate(result):
        hasil.append(f'{x+1}. {i[0]} {i[1]} {i[2]}')
    return hasil

    session.commit()
    session.close()

    
# Menampilkan <n> orang dengan total pembelian terbanyak berserta nama barangnya
@app.post("/pembeli_terbanyak")
async def tampilkan_tempat_tinggal_n_pembeli_terbanyak(users_csv: UploadFile = File(...), 
                                                        products_csv: UploadFile = File(...),
                                                        banyaknya_orang_yang_ditampilkan = 1000,
                                                        Authorize: AuthJWT = Depends()
                                                         ):
    Authorize.jwt_required()
    
    tabel_sql_jadi(users_csv,products_csv)
    
    n = int(banyaknya_orang_yang_ditampilkan)
    
    result = (
    session.query(Purchase.name, 
                  sa.func.group_concat(Purchase.product_name, separator=", ").label("product_name"), 
                  sa.func.sum(Purchase.quantity).label("quantity"))
        .group_by(Purchase.name)
        .order_by(sa.func.sum(Purchase.quantity).desc())
        .limit(n)
        )

    hasil = []
    for i in result:
        kucing = {}
        kucing['name'] = i[0]
        kucing['product_name'] = i[1].split(',')
        kucing['quantity'] = i[2]
        hasil.append(kucing)
    
    return hasil
    
    session.commit()
    session.close()    
    
# Menampilkan transaksi tiap orang berdasarkan customer_id dengan data tanggal, nama, dan barang beserta banyak dan jumlahnya
@app.post("/transaksi_individu")
async def transaksi_tiap_customer_id(users_csv: UploadFile = File(...), 
                                                        products_csv: UploadFile = File(...),
                                                        customer_id = 0,
                                                        Authorize: AuthJWT = Depends()
                                                         ):
    Authorize.jwt_required()
    
    tabel_sql_jadi(users_csv,products_csv)
    
    result = (
        session.query(
            sa.func.group_concat(Purchase.date).label('Tanggal_Pembelian'),
            Purchase.name.label('Nama'),
            sa.func.group_concat(Purchase.product_name).label('Barang'),
            sa.func.count(Purchase.product_name).label('Banyaknya_Barang'),
            sa.func.sum(Purchase.quantity).label('Total_Barang')
        )
        .outerjoin(Users, Purchase.name == Users.name)
        .filter(Users.customer_id == customer_id)
        .group_by(Purchase.name)
        .order_by(Purchase.name)
    )

    hasil = []
    for i in result:
        kucing = {}
        kucing['Tanggal_Pembelian'] = i[0].split(',')
        kucing['Nama'] = i[1]
        kucing['Barang'] = i[2].split(',')
        kucing['Banyaknya_Barang'] = i[3]
        kucing['Total_Barang'] = int(i[4])
        hasil.append(kucing)
    
    return hasil
    
    session.commit()
    session.close()       
    
# Menampilkan semua data pembeli dan barang dengan query parameternya adalah nama barang, tanggal awal pembelian dan tanggal akhir pembelian
@app.post("/tampilkan_semua")
async def tampilkan_semua_data_pembelian(users_csv: UploadFile = File(...), 
                                        products_csv: UploadFile = File(...),
                                        nama_barang = None,
                                        tanggal_awal = '01-01-2017',
                                        tanggal_akhir = '17-12-2022',
                                        Authorize: AuthJWT = Depends()
                                        ):
    Authorize.jwt_required()
    
    tabel_sql_jadi(users_csv,products_csv)
    
    db = connect(host = db_host, 
         user = db_user, 
         password = params['db']['MYSQL_PASSWORD'],
         database = db_name)
    
    def query_barang_tanggal(db,nama_barang,tanggal_awal,tanggal_akhir):
        query = f'''
                select DATE_FORMAT(STR_TO_DATE(a.date, '%d-%m-%Y'), '%d-%m-%Y') AS tanggal, 
                a.name, a.product_name, c.category, c.sub_category, a.quantity, b.city, b.state
                from purchase a
                inner join users b on a.name = b.name
                inner join products c on a.product_name = c.product_name
                where a.product_name Like '%{nama_barang}%'
                and STR_TO_DATE(a.date, '%d-%m-%Y') 
                BETWEEN STR_TO_DATE('{tanggal_awal}', '%d-%m-%Y') AND STR_TO_DATE('{tanggal_akhir}', '%d-%m-%Y')
                ORDER BY a.date ASC, a.quantity DESC, a.name ASC;
                '''
        cursor_db = db.cursor()
        cursor_db.execute(query)
        result = cursor_db.fetchall()
        hasil = []
        for i in result:
            kucing = {}
            kucing['Tanggal'] = i[0]
            kucing['Nama Pembeli'] = i[1]
            kucing['Nama Produk'] = i[2]
            kucing['Kategori'] = i[3]
            kucing['Sub Kategori'] = i[4]
            kucing['Kuantitas'] = i[5]
            kucing['kota'] = i[6]
            kucing['Negara'] = i[7]
            hasil.append(kucing)
        cursor_db.close()
        db.close()
        return hasil

    return query_barang_tanggal(db,nama_barang,tanggal_awal,tanggal_akhir)
    
if __name__ == "__main__":
    uvicorn.run(app)