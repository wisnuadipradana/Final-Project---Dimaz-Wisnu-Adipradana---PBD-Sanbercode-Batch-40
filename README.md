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
<b>Table users</b> <br>
Pada tabel users terdapat nama kolom dengan penjelasannya sebagai berikut:<br>

- customer_id : nomor urut id untuk pembeli dalam format integer <br> 
- name : nama pembeli dalam format string yang merupakan primary key<br>
- city : kota tempat tinggal pembeli dalam format string <br>
- state : negara tempat tinggal pembeli dalam format string <br>
- postal :  kode pos dari tempat tinggal pembeli dalam format integer<br>

<br>
<img src="https://github.com/wisnuadipradana/Final-Project---Dimaz-Wisnu-Adipradana---PBD-Sanbercode-Batch-40/blob/main/Tabel%20users.JPG"><br>
<br>
<b>Table products</b> <br>
Pada tabel users terdapat nama kolom dengan penjelasannya sebagai berikut:<br>

- product_id : nomor urut id produk dalam format integer <br> 
- product_name : nama produk dalam format string yang merupakan primary key <br>
- category : kategori produk dalam format string <br>
- sub_category : sub kategori produk dalam format string <br>

<br>
<img src=https://github.com/wisnuadipradana/Final-Project---Dimaz-Wisnu-Adipradana---PBD-Sanbercode-Batch-40/blob/main/Tabel%20products.JPG>
<br>  
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
<img src=https://github.com/wisnuadipradana/Final-Project---Dimaz-Wisnu-Adipradana---PBD-Sanbercode-Batch-40/blob/main/Tabel%20purchase.JPG>
<br>  
</details>

Data ketiga tabel tersebut dimasukkan ke dalam database SQL menggunakan modul pada Python yaitu SQLAlchemy yang dibuat di dalam fungsi `tabel_sql_jadi`.<br>

Nah selanjutnya, tujuan dari tugas ini adalah menggunakan FastAPI untuk melakukan RestAPI.<br> Route-route POST yang dibuat dari FastAPI akan menggunggah file 
<a href="https://github.com/wisnuadipradana/Final-Project---Dimaz-Wisnu-Adipradana---PBD-Sanbercode-Batch-40/blob/main/users.csv">users.csv</a>
dan <a href="https://github.com/wisnuadipradana/Final-Project---Dimaz-Wisnu-Adipradana---PBD-Sanbercode-Batch-40/blob/main/products.csv">products.csv</a>

<details>
<summary><strong>Penjelasan Route</strong></summary>
Berikut adalah penjelasan tiap route FastAPI yang dibuat dan karena dilakukan autentifikasi menggunakan Json Web Token atau disingkat JWT pada FastAPI yang bertujuan memproteksi dengan key bearer berbentuk token untuk bisa mengakses route-route tertentu.<br>

- Pertama, jalankan program <a href="https://github.com/wisnuadipradana/Final-Project---Dimaz-Wisnu-Adipradana---PBD-Sanbercode-Batch-40/blob/main/Tugas%20Akhir.py">Tugas_Akhir.py</a>. 
- Route `get("/")` dengan fungsi `tugas_akhir` dapat dibuka melalui link http://localhost:8000/ pada browser kalian sehingga tampilannya akan muncul sebagai berikut 
![localhost8000](https://user-images.githubusercontent.com/49567907/211193433-9a252c07-6b65-4f93-ab13-2399ae6350ee.JPG)<br>
Karena route `post("/barang")` dan `post("cari_nama_barang/{nama_barang}")` tidak perlu autentifikasi dengan JWT maka dapat langsung kita lihat hasil post melalui link berikut http://localhost:8000/docs#/. Link tersebut merupakan dokumentasi dengan swagger yang tersedia langsung jika menggunakan FastAPI, tampilannya akan muncul sebagai berikut
![localhost8000,docs#](https://user-images.githubusercontent.com/49567907/211194205-241889c7-9f0c-428e-93f1-a601d1ab39f7.JPG)
- Route `post("/barang")` dengan fungsi `tampilkan_barang` pada link tersebut memiliki variabel upload dokumen dari `users.csv` dan `products.csv` serta terdapat variabel `sort_desc` yang bernilai `True` jika diinginkan pengurutan dari besar ke kecil, `False` jika diinginkan pengurutan dari kecil ke besar, dan `None` jika tidak ingin diurutkan. Tampilannya akan muncul sebagai berikut.
![image](https://user-images.githubusercontent.com/49567907/211194435-d9fe4cce-af28-414d-ac31-f8d32fc77bbc.png)


</details>

