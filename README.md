# Final Project Dimaz Wisnu Adipradana PBD Sanbercode Batch 40

## Data Peserta Bootcamp Digital Skill - Python Backend Development
Nama: Dimaz Wisnu Adipradana <br>
Email: wisnuadipradana17@yahoo.com <br>
Sistem Operasi yang digunakan: <img src="https://img.shields.io/badge/Windows%2010-%230078D6.svg?&amp;style=for-the-badge&amp;logo=windows&amp;logoColor=white" style="max-width:100%;">
  <img src="https://img.shields.io/badge/Core%20i7%208th-%230071C5.svg?&amp;style=for-the-badge&amp;logo=intel&amp;logoColor=white" style="max-width:100%;">
  <img src="https://img.shields.io/badge/RAM-8GB-%230071C5.svg?&amp;style=for-the-badge&amp;logoColor=white" style="max-width:100%;">
  <img src="https://img.shields.io/badge/NVIDIA-GEFORCE%20MX150-%2376B900.svg?&amp;style=for-the-badge&amp;logo=nvidia&amp;logoColor=white" style="max-width:100%;"><br>
Akun Gitlab/Github: <a href="https://gitlab.com/wisnuadipradana" target="blank"><img src="https://img.shields.io/badge/gitlab-%23330f63.svg?&style=for-the-badge&logo=gitlab&logoColor=white" ></a> / <a href="https://github.com/wisnuadipradana"><img src="https://img.shields.io/github/followers/wisnuadipradana?label=wisnuadipradana&amp;style=social" style="max-width:100%;"></a> <br>
Akun Telegram: <a href="https://t.me/uzumakinagatotenshou">@wisnuduzu</a> 

## Penjelasan Final Project

Full code jawaban pembahasan Tugas bisa dilihat di <a href="https://github.com/wisnuadipradana/Final-Project---Dimaz-Wisnu-Adipradana---PBD-Sanbercode-Batch-40/blob/main/wisnuadipradana17_Tugas_Akhir.py">wisnuadipradana17_Tugas_Akhir.py</a></br>

<details>
<summary><strong>Penjelasan Data</strong></summary>
Pertama diberikan data users dan products yang diperlihatkan pada gambar berikut:<br>
<b>Table users</b> <br>
Pada tabel users terdapat nama kolom dengan penjelasannya sebagai berikut:</br>
- customer_id : nomor urut id untuk pembeli dalam format integer <br> 
- name : nama pembeli dalam format string yang merupakan primary key<br>
- city : kota tempat tinggal pembeli dalam format string <br>
- state : negara tempat tinggal pembeli dalam format string <br>
- postal :  kode pos dari tempat tinggal pembeli dalam format integer<br>

<br>
<img src="https://github.com/wisnuadipradana/Final-Project---Dimaz-Wisnu-Adipradana---PBD-Sanbercode-Batch-40/blob/main/Tabel%20users.JPG">
<br>
<b>Table products</b> <br>
Pada tabel users terdapat nama kolom dengan penjelasannya sebagai berikut:</br>
- product_id : nomor urut id produk dalam format integer <br> 
- product_name : nama produk dalam format string yang merupakan primary key <br>
- category : kategori produk dalam format string <br>
- sub_category : sub kategori produk dalam format string <br>

<br>
<img src=https://github.com/wisnuadipradana/Final-Project---Dimaz-Wisnu-Adipradana---PBD-Sanbercode-Batch-40/blob/main/Tabel%20products.JPG>
<br>  
  
<details>
<summary><strong>Penjelasan Tabel purchase</strong></summary>
Dari tabel users dan tabel products akan dibuat tabel purchase yang memiliki nama kolom dengan penjelasannya sebagai berikut:<br>
- date : tanggal pembelian dalam format datetime <br>
- name : nama pembeli dalam format string yang merupakan primary key yang berhubungan dengan tabel users <br>
- product_name : nama produk dalam format string yang merupakan primary key yang berhubungan dengan tabel products <br>
- quantity : jumlah barang yang dibeli dari produk_name dalam format integer <br>

Diberikan hasil tabel berupa gambarnya sebagai berikut:
<br>
<img src=https://github.com/wisnuadipradana/Final-Project---Dimaz-Wisnu-Adipradana---PBD-Sanbercode-Batch-40/blob/main/Tabel%20purchase.JPG>
<br>  
