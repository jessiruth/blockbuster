
# Blockbuster
Blockbuster merupakan aplikasi yang digunakan untuk memanajemen data film. Aplikasi ini dibuat menggunakan bahasa pemrograman Python dan menggunakan framework Django. Aplikasi ini dibuat untuk memenuhi tugas besar mata kuliah Pemrograman Berbasis Platform yang diselenggarakan oleh Fakultas Ilmu Komputer, Universitas Indonesia.

## Author
- Nama: Jessica Ruth Damai Yanti Manurung
- NPM: 2206031302
- Kelas: Pemrograman Berbasis Platform C

# Tugas 2: Implementasi Model-View-Template (MVT) pada Django

## *Step-by-step* Implementasi MVT

### 1. *Setup virtual environment* untuk Django
Sebelum memulai membuat aplikasi, saya membuat *virtual environment* untuk Django menggunakan perintah berikut:
```
python -m venv env
```
Setelah *virtual environment* dibuat, saya mengaktifkannya menggunakan perintah berikut:
```
env\Scripts\activate.bat
```

### 2. *Setup* Django
Setelah *virtual environment* diaktifkan, saya membuat berkas `requirements.txt` yang berisi daftar *package* yang dibutuhkan untuk membuat aplikasi. Berikut isi dari berkas `requirements.txt`:
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
Pillow
```
Setelah itu, saya menginstall *package* yang dibutuhkan menggunakan perintah berikut:
```
pip install -r requirements.txt
```
Setelah *package* terinstall, saya membuat *project* Django bernama `blockbuster` menggunakan perintah berikut:
```
django-admin startproject blockbuster .
```
### 3. Konfigurasi Proyek untuk *Deployment*
Setelah *project* dibuat, saya melakukan konfigurasi untuk *deployment* dengan cara menambahkan `*` pada `ALLOWED_HOSTS` pada berkas `blockbuster/settings.py` agar dapat diakses dari luar. Berikut isi dari berkas `blockbuster/settings.py`:
```
...
ALLOWED_HOSTS = ['*']
...
```
### 4. Membuat *app* `main`
Setelah konfigurasi selesai, saya membuat *app* `main` menggunakan perintah berikut:
```
python manage.py startapp main
```
Setelah *app* dibuat, saya melakukan konfigurasi pada `INSTALLED_APPS` pada berkas `blockbuster/settings.py` dengan menambahkan `main`. Berikut isi dari berkas `blockbuster/settings.py`:
```
...
INSTALLED_APPS = [
    ...,
    "main",
]
...
```
### 5. Membuat *model* `Item`
Setelah *app* dibuat, saya membuat *model* `Item` pada berkas `main/models.py`. Berikut isi dari berkas `main/models.py`:
```
...
class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.FloatField()
    year = models.IntegerField()
    genre = models.CharField(max_length=255)
    duration = models.IntegerField()
    rating = models.FloatField()
    image = models.ImageField(upload_to='images/')
```
Setelah *model* dibuat, saya melakukan migrasi menggunakan perintah berikut:
```
python manage.py makemigrations
python manage.py migrate
```
### 6. Membuat *template* `index.html`
Setelah migrasi selesai, saya membuat *template* `index.html` pada berkas `main/templates/index.html`. Berikut isi dari berkas `main/templates/index.html`:
```
<h1> Blockbuster </h1>
<h2> A simple movie database </h2>

<h4> Name: </h4>
<p> Jessica Ruth Damai Yanti Manurung </p>
<h4> NPM: </h4>
<p> 2206082783 </p>
<h4> Class: </h4>
<p> PBP C </p>
```
