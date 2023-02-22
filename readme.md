![banner](static/image/0.jpg)

# REST API aplikasi Mobile "Mark My Face"

#### **Author : @GedeYudaAditya**

### Version 0.0

<p>Menggunakan teknologi framework django rest API</p>
<br>

## Tentang API

---

<p>
API ini digunakan untuk mengelola data gambar yang masuk melalui request post dari aplikasi mobile "Mark My Face" lalu akan mengembalikan data hasil proses ke aplikasi pengirim request.
</p>

<p>
Menggunakan framework REST API Django, berikut ini merupakan list package yang direkomendasikan :
</p>

```
Package               Version
--------------------- --------
asgiref               3.6.0
Django                4.1.6
djangorestframework   3.14.0
numpy                 1.24.2
opencv-contrib-python 4.7.0.68
Pillow                9.4.0
pip                   23.0
pytz                  2022.7.1
setuptools            65.5.0
sqlparse              0.4.3
tzdata                2022.7
```

<p>Aplikasi ini masih dalam proses pengembangan, belum banyak hal yang terjadi.</p>
<br>

## Dokumentasi Pembuatan Project

---

Untuk dapat menjalankan API anda perlu meng-install beberapa package terlebih dahulu, namun sebelum itu anda perlu membuat **Virtual Env**.

```
$ python -m venv Env
```

Aktifkan Env yang telah di buat menggunakan perintah berikut (tergantung dimana anda menempatkan folder env yang di buat)

```
..\Env\Scripts\activate.bat
```

Lalu install package pada virtual env yang telah di buat

1. Instal package Django menggunakan pip install

   ```
   (Env) $ pip install django
   ```

2. Instal package Django Rest API menggunakan pip install

   ```
   (Env) $ pip install djangorestframework
   ```

3. Tambahkan package OpenCV untuk mempermudah pemrosesan gambar pada python

   ```
   (Env) $ pip install opencv
   ```

Lalu anda dapat membuat project baru dengan menjalankan perintah `django-admin startproject aplication_name` pada virtual env yang telah di buat.

Jalankan server menggunakan `python manage.py runserver`
<br>
<br>

## Release Note Ver.0.0

---

API List Function :

1. Url `http:/localhost/get_test` [Get]
   - Untuk melakukan testing get.
2. Url `http:/localhost/add_test` [Post]
   - Untuk melakukan testing post.
3. Url `http:/localhost/detect_face` [Post]
   - Untuk melakukan deteksi wajah dan menyimpan nya ke database.
4. Url `http:/localhost/rec_face` [Post]
   - Melakukan pencocokan wajah
5. Url `http:/localhost/get_face` [Get]
   - Memberikan list wajah yang telah terekam
