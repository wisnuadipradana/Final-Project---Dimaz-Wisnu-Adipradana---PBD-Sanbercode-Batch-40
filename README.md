# Final Project Dimaz Wisnu Adipradana Python Backend Development Sanbercode Batch 40

## Data Peserta Bootcamp Digital Skill - Python Backend Development
Nama: Wisnu D. Uzu <br>
Sistem Operasi yang digunakan: <img src="https://img.shields.io/badge/Windows%2010-%230078D6.svg?&amp;style=for-the-badge&amp;logo=windows&amp;logoColor=white" style="max-width:100%;">
  <img src="https://img.shields.io/badge/Core%20i7%208th-%230071C5.svg?&amp;style=for-the-badge&amp;logo=intel&amp;logoColor=white" style="max-width:100%;">
  <img src="https://img.shields.io/badge/RAM-8GB-%230071C5.svg?&amp;style=for-the-badge&amp;logoColor=white" style="max-width:100%;">
  <img src="https://img.shields.io/badge/NVIDIA-GEFORCE%20MX150-%2376B900.svg?&amp;style=for-the-badge&amp;logo=nvidia&amp;logoColor=white" style="max-width:100%;"><br>
Akun Gitlab/Github: <a href="https://gitlab.com/wisnuadipradana" target="blank"><img src="https://img.shields.io/badge/gitlab-%23330f63.svg?&style=for-the-badge&logo=gitlab&logoColor=white" ></a> / <a href="https://github.com/wisnuadipradana"><img src="https://img.shields.io/github/followers/wisnuadipradana?label=wisnuadipradana&amp;style=social" style="max-width:100%;"></a> <br>
Akun Telegram: <a href="https://t.me/uzumakinagatotenshou">@wisnuduzu</a> 

## Penjelasan Final Project

Full code jawaban pembahasan Tugas bisa dilihat di <a href="https://github.com/wisnuadipradana/Final-Project---Dimaz-Wisnu-Adipradana---PBD-Sanbercode-Batch-40/blob/main/Tugas%20Akhir.py">Tugas_Akhir.py</a></br>

<details>
<summary><strong>Penjelasan Data</strong></summary>
Pertama diberikan data users dan products yang diperlihatkan pada gambar berikut:<br>
<br>
<b><strong>Table users</strong></b> <br>
Pada tabel users terdapat nama kolom dengan penjelasannya sebagai berikut:<br>

- customer_id : nomor urut id untuk pembeli dalam format integer <br> 
- name : nama pembeli dalam format string yang merupakan primary key<br>
- city : kota tempat tinggal pembeli dalam format string <br>
- state : negara tempat tinggal pembeli dalam format string <br>
- postal :  kode pos dari tempat tinggal pembeli dalam format integer<br>

<br>
<img src="https://user-images.githubusercontent.com/49567907/211195252-9c27682a-063d-479d-9fb5-52e66f2794d1.JPG">
</br>
<b><strong>Table products</strong></b> <br>
Pada tabel products terdapat nama kolom dengan penjelasannya sebagai berikut:<br>

- product_id : nomor urut id produk dalam format integer <br> 
- product_name : nama produk dalam format string yang merupakan primary key <br>
- category : kategori produk dalam format string <br>
- sub_category : sub kategori produk dalam format string <br>

<br>
<img src="https://user-images.githubusercontent.com/49567907/211195244-bc7f1dff-0fcd-48c1-9262-e96afbf6ab30.JPG">
</br>  
</details>
  
<details>
<summary><strong>Penjelasan Tabel purchase</strong></summary>
Dari tabel users dan tabel products akan dibuat tabel purchase yang memiliki nama kolom dengan penjelasannya sebagai berikut:<br>

- date : tanggal pembelian dalam format datetime dilakukan dengan mengambil random tanggal dari tahun 2017 hingga 17-12-2022<br>
- name : nama pembeli dalam format string yang merupakan primary key yang berhubungan dengan tabel users <br>
- product_name : nama produk dalam format string yang merupakan primary key yang berhubungan dengan tabel products <br>
- quantity : jumlah barang yang dibeli dari produk_name dalam format integer dengan mengambil random bilangan asli dari 1-25<br>

Diberikan hasil tabel berupa gambarnya sebagai berikut:
<br>
![Tabel purchase](https://user-images.githubusercontent.com/49567907/211194764-bdd389da-ab4c-4b88-85b9-4207eba3f0be.JPG)
</br>  
</details>

Data ketiga tabel tersebut dimasukkan ke dalam database SQL menggunakan modul pada Python yaitu SQLAlchemy yang dibuat di dalam fungsi `tabel_sql_jadi`.<br>
Tabel yang telah tersimpan ke dalam sql tersimpan seperti pada file 
<a href="https://github.com/wisnuadipradana/Final-Project---Dimaz-Wisnu-Adipradana---PBD-Sanbercode-Batch-40/blob/main/users.sql">users.sql</a>,
<a href="https://github.com/wisnuadipradana/Final-Project---Dimaz-Wisnu-Adipradana---PBD-Sanbercode-Batch-40/blob/main/products.sql">products.sql</a>, dan
<a href="https://github.com/wisnuadipradana/Final-Project---Dimaz-Wisnu-Adipradana---PBD-Sanbercode-Batch-40/blob/main/purchase.sql">purchase.sql</a>.


Nah selanjutnya, tujuan dari tugas ini adalah menggunakan FastAPI untuk melakukan RestAPI.<br> Route-route POST yang dibuat dari FastAPI akan menggunggah file 
<a href="https://github.com/wisnuadipradana/Final-Project---Dimaz-Wisnu-Adipradana---PBD-Sanbercode-Batch-40/blob/main/users.csv">users.csv</a>
dan <a href="https://github.com/wisnuadipradana/Final-Project---Dimaz-Wisnu-Adipradana---PBD-Sanbercode-Batch-40/blob/main/products.csv">products.csv</a>

<details>
<summary><strong>Penjelasan Route</strong></summary>
Berikut adalah penjelasan tiap route FastAPI yang dibuat dan karena dilakukan autentikasi menggunakan Json Web Token atau disingkat JWT pada FastAPI yang bertujuan memproteksi dengan key bearer berbentuk token untuk bisa mengakses route-route tertentu.<br>

- Pertama, jalankan program <a href="https://github.com/wisnuadipradana/Final-Project---Dimaz-Wisnu-Adipradana---PBD-Sanbercode-Batch-40/blob/main/Tugas%20Akhir.py">Tugas_Akhir.py</a>. 
- Route `get("/")` dengan fungsi `tugas_akhir` dapat dibuka melalui link http://localhost:8000/ pada browser kalian sehingga tampilannya akan muncul sebagai berikut 
![localhost8000](https://user-images.githubusercontent.com/49567907/211193433-9a252c07-6b65-4f93-ab13-2399ae6350ee.JPG)<br>

Karena route `post("/barang")` dan `post("cari_nama_barang/{nama_barang}")` tidak perlu autentikasi dengan JWT maka dapat langsung kita lihat hasil post melalui link berikut http://localhost:8000/docs#/. Link tersebut merupakan dokumentasi dengan swagger yang tersedia langsung jika menggunakan FastAPI, tampilannya akan muncul sebagai berikut
![localhost8000,docs#](https://user-images.githubusercontent.com/49567907/211194205-241889c7-9f0c-428e-93f1-a601d1ab39f7.JPG)<br>

- Route `post("/barang")` dengan fungsi `tampilkan_barang` pada link tersebut memiliki parameter upload dokumen dari `users.csv` dan `products.csv` serta terdapat query parameter `sort_desc` yang bernilai `True` jika diinginkan pengurutan dari besar ke kecil, `False` jika diinginkan pengurutan dari kecil ke besar, dan `None` jika tidak ingin diurutkan. Tampilannya akan muncul sebagai berikut.
![image](https://user-images.githubusercontent.com/49567907/211194435-d9fe4cce-af28-414d-ac31-f8d32fc77bbc.png)
- Route `post("/cari_nama_barang")` dengan fungsi `mencari_barang` pada link tersebut memiliki parameter upload dokumen dari `users.csv` dan `products.csv` serta terdapat query parameter `nama_barang` yaitu nama dari barang yang akan dicari juga terdapat query parameter `sort_desc` yang bernilai `True` jika diinginkan pengurutan dari besar ke kecil, `False` jika diinginkan pengurutan dari kecil ke besar, dan `None` jika tidak ingin diurutkan. Tampilannya akan muncul sebagai berikut.
![localhost8000,cari_nama_barang](https://user-images.githubusercontent.com/49567907/211195886-14f501fd-54a0-44f8-be71-613e8123051c.JPG)<br>

Selanjutnya, karena route-route lain membutuhkan akses dari autentikasi dengan JWT, maka dari route `post('/login)` akan diambil authorization berupa token bearer kemudian digunakan untuk masuk ke route-route lain. Dibutuhkan aplikasi penunjang untuk melakukan request HTTP diantaranya menggunakan Postman, Insomnia, cURL, HTTPie, Advanced REST Client, Swagger UI. Pada kesempatan kali ini akan digunakan aplikasi Postman.
<br>

- Route `post("/login")` dengan fungsi `login` pada link http://localhost:8000/login memiliki parameter  `Account` yang merupakan tempat penyimpanan database kumpulan akun dengan username, email dan password yang tersimpan. Pada code ini diberikan contoh akun pada list dengan dictionary `akun`. Kemudian, terdapat parameter AuthJWT yang digunakan untuk autentikasi dengan JWT.<br>
Pada Postman di bagian body dan pilih form data, kemudian isi key dan value sesuai seperti gambar berikut.
![image](https://user-images.githubusercontent.com/49567907/211197574-590587be-c5d6-4c23-b8d7-dbeecaa2e239.png)
Kemudian, pada bagian body di Postman, pilih headers. Nah, di sini isi key dengan `Content-Type` dan value dengan `application/json` seperti pada gambar berikut.<br>
<img src="https://user-images.githubusercontent.com/49567907/211209405-67c64384-a6ea-428a-ae08-1a82019d6ff5.png"></img>
Selanjutnya, pada bagian body di Postman, pilih raw. Nah, di sini kalian isikan dengan format sebagai berikut.<br>
<code>{
    "username_or_email": "&lt;isi dengan username atau email yang terdaftar&gt;",
    "password": "&lt;isi dengan password dari username atau email sebelumnya&gt;"
}
</code>
Kemudian, klik Send pada Postman sehingga hasilnya diperoleh bearer token yang diinginkan seperti pada gambar berikut.<br>
<img src="https://user-images.githubusercontent.com/49567907/211197690-a16abf3e-3768-48ea-b9ca-a6bf533830e6.png"><br>
Dari token yang didapat salin dan tempel ke menu `Authorization` dan pilih tipenya adalah Bearer Token pada Postman seperti gambar berikut.
<img src="https://user-images.githubusercontent.com/49567907/211208179-9c6a9e48-639a-4bfa-8bff-ba62ec958ff6.png"></img>

- Route `get('\user')` dengan fungsi `user` pada link http://localhost:8000/user memiliki parameter AuthJWT yang digunakan untuk autentikasi token yang diperoleh sebelumnya dengan JWT. Pada route ini bertujuan untuk mengetahui username, email, dan password yang digunakan pada waktu login sebelumnya. Hasilnya seperti pada gambar berikut.
<img src="https://user-images.githubusercontent.com/49567907/211208651-0a7c3a55-410a-40d7-a6aa-563621cbf61d.png"></img>
- Route `post("/tabel/{nama_tabel}")` dengan fungsi `mencari_barang` pada link tersebut memiliki parameter upload dokumen dari `users.csv` dan `products.csv` serta terdapat query parameter `nama_barang` yaitu nama dari barang yang akan dicari juga terdapat query parameter `sort_desc` yang bernilai `True` jika diinginkan pengurutan dari besar ke kecil, `False` jika diinginkan pengurutan dari kecil ke besar, dan `None` jika tidak ingin diurutkan. Tampilannya akan muncul sebagai berikut.




</details>

