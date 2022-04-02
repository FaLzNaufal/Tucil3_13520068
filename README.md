# TUGAS KECIL 3

## Deskripsi
Program ini dibuat dengan tujuan utama menyelesaikan tugas kecil Strategi Algoritma dalam materi Branch and Bound. Program ini adalah implementasi strategi Branch and Bound untuk menyelesaikan 15 Puzzle.

## Requirement
* Python 10
* numpy
* tkinter (bawaan)
* timeit (bawaan)
* bisect (bawaan)

## Cara Menggunakan
Program ini merupakan program berbasis GUI tkinter untuk menyelesaikan permasalahan 15 puzzle dengan menggunakan algoritma branch and bound. Ada dua cara menjalankan program.

### Langsung dari executable
Buka folder bin dan jalankan executable. Masukkan berupa file .txt di dalam folder test dengan format seperti pada salah satu file input contoh, yang dalam hal ini, input berupa matriks 4x4 yang dipisah dengan spasi pada tiap kolom dan newline untuk tiap kolomnya, serta angka 16 merupakan representasi ubin kosong pada puzzle. Saat program dijalankan, masukkan nama file input yang diinginkan (pastikan file input ada di folder test atau masukkan full path dari file tersebut), kemudian tekan tombol open. Setelah susunan awal puzzle muncul pada layar, silakan tekan tombol solve untuk mencari solusi. Setelah solusi didapatkan, akan keluar detail pencarian pada sebelah kanan. Tekan tombol next atau prev untuk menavigasi langkah solusi. Tekan tombol rewind atau fast forward untuk menampilkan seluruh langkah secara automatis.

### Jalankan GUI.py
Jika metode pertama bermasalah, buka folder src, kemudian jalankan program dengan mengetikan perintah berikut pada command line interface
```
python main.py
```
Setelah itu akan muncul window GUI yang sama dengan metode pertama.

## Author
Muhammad Naufal Satriandana 13520068