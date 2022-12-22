import pandas as pd
import random
random.seed(7)
from datetime import datetime, timedelta
import urllib.parse
from dotenv import dotenv_values

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

from fastapi import FastAPI, File, UploadFile
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
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2022, 12, 17)
    # Generate a random date between the start and end dates
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    # Convert the random date to a string in the DD--MM-YYYY format
    formatted_date = random_date.strftime("%d-%m-20%y")
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
    
    # Insert data ke tabel products
    df_products.to_sql('products', engine, if_exists='replace', index=False)

    # Insert data ke tabel users
    df_users.to_sql('users', engine, if_exists='replace', index=False)

    # Insert data ke tabel purchase
    df_purchase.to_sql('purchase', engine, if_exists='replace', index=False)
    
# Buat Session
Session = sessionmaker(bind=engine)
session = Session()
conn = engine.connect()

# Menampilkan isi dari tabel (users, products, purchase)
@app.post("/tabel/{nama_tabel}")
async def tampilkan_isi_tabel(users_csvfile: UploadFile = File(...), 
                          products_csvfile: UploadFile = File(...),
                          nama_tabel = None
                         ):
    tabel_sql_jadi(users_csvfile,products_csvfile)
    
    return conn.execute(f'select * from {nama_tabel.lower()}').all()
        
if __name__ == "__main__":
    uvicorn.run(app)
    
    
    