
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

### 7. Membuat *view* `index`
Setelah *template* dibuat, saya membuat *view* `index` pada berkas `main/views.py`. Berikut isi dari berkas `main/views.py`:
```
...
def index(request):
    context = {
        "name": "Jessica Ruth Damai Yanti Manurung",
        "npm": "2206082783",
        "class": "PBP C",
    }
    return render(request, 'index.html', context)
```
Setelah *view* dibuat, saya melakukan modifikasi pada *template* `index.html` dengan menambahkan *context* yang telah dibuat. Berikut isi dari berkas `main/templates/index.html`:
```
<h1> Blockbuster </h1>
<h2> A simple movie database </h2>

<h4> Name: </h4>
<p> {{ name }} </p>
<h4> NPM: </h4>
<p> {{ npm }} </p>
<h4> Class: </h4>
<p> {{ class }} </p>
```

### 8. Membuat *url* `index`
Setelah *view* dibuat, saya membuat *url* `index` pada berkas `main/urls.py`. Sebelum itu, saya mengimpor *views* yang telah dibuat dan membuat `app_name` untuk *app* `main`. Berikut isi dari berkas `main/urls.py`:
```
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
]
```

### 9. Mengonfigurasi *url* pada *project*
Setelah *url* dibuat, saya melakukan konfigurasi pada `urlpatterns` pada berkas `blockbuster/urls.py` dengan menambahkan *url* dari *app* `main`. Sebelum itu, saya mengimpor `include` dari `django.urls`. Berikut isi dari berkas `blockbuster/urls.py`:
```
...
from django.urls import path, include

urlpatterns = [
    ...,
    path('', include('main.urls')),
]
```
### 10. Membuat Unit *Test*
Setelah konfigurasi selesai, saya membuat unit *test* pada berkas `main/tests.py`. Berikut isi dari berkas `main/tests.py`:
```
from django.test import TestCase, Client
from .models import Item

# Create your tests here.
class MainTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        Item.objects.create(
            name='Ponyo on the Cliff by the Sea',
            amount=10,
            description='Ponyo on the Cliff by the Sea is a 2008 Japanese animated fantasy film written and directed by Hayao Miyazaki, animated by Studio Ghibli for the Nippon Television Network, Dentsu, Hakuhodo DY Media Partners, Buena Vista Home Entertainment, Mitsubishi, and distributed by Toho.',
            price=30000,
            year=2008,
            genre='Fantasy, Adventure, Family',
            duration=101,
            rating=7.7,
            image='images/Ponyo_(2008).png',
        )
        
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'Jessica Ruth Damai Yanti Manurung')
        self.assertContains(response, '2206082783')
        self.assertContains(response, 'PBP C')
        
    def test_item(self):
        ponyo = Item.objects.get(name='Ponyo on the Cliff by the Sea')
        self.assertEqual(ponyo.name, 'Ponyo on the Cliff by the Sea')
        self.assertEqual(ponyo.amount, 10)
        self.assertEqual(ponyo.description, 'Ponyo on the Cliff by the Sea is a 2008 Japanese animated fantasy film written and directed by Hayao Miyazaki, animated by Studio Ghibli for the Nippon Television Network, Dentsu, Hakuhodo DY Media Partners, Buena Vista Home Entertainment, Mitsubishi, and distributed by Toho.')
        self.assertEqual(ponyo.price, 30000)
        self.assertEqual(ponyo.year, 2008)
        self.assertEqual(ponyo.genre, 'Fantasy, Adventure, Family')
        self.assertEqual(ponyo.duration, 101)
        self.assertEqual(ponyo.rating, 7.7)
        self.assertEqual(ponyo.image, 'images/Ponyo_(2008).png')
        
```
Setelah unit *test* dibuat, saya menjalankan unit *test* menggunakan perintah berikut:
```
python manage.py test
```
Hasil dari unit *test* adalah sebagai berikut:
```
Found 2 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.038s

OK
Destroying test database for alias 'default'...
```

### 11. Melakukan *Deployment* ke Adaptable
Setelah unit *test* selesai, saya melakukan *deployment* ke Adaptable dengan langkah-langkah sebagai berikut:
1. *Login* ke [Adaptable](https://adaptable.io/)
2. Klik *New App* dan pilih *Connect an Existing Repository*
3. Pilih `jessiruth/blockbuster` sebagai *repository* dan pilih *branch* `main`
4. Pilih *Python App Template* sebagai *template*
5. Pilih *PostgreSQL* sebagai *database*
6. Pilih *Python 3.10* sebagai *Python Version*
7. Ketik `python manage.py migrate && gunicorn blockbuster.wsgi` pada *Start Command* dan klik *Next*
8. Ketik `jess-blockbuster` pada *App Name* dan klik *Next*
9. Centang *HTTP Listener on PORT*, lalu klik *DEPLOY APP*
10. Tunggu hingga *deployment* selesai
11. Klik *VISIT APP* untuk melihat hasil *deployment*

Berikut adalah hasil *deployment* yang telah dilakukan:
[![image](https://i.postimg.cc/1tLjZwcT/deployment.png)](https://jess-blockbuster.adaptable.app/)
Website dapat diakses melalui [https://jess-blockbuster.adaptable.app/](https://jess-blockbuster.adaptable.app/)

## Menjawab Pertanyaan-Pertanyaan
### 1. Buatlah bagan yang berisi *request client* ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
[![Mekanisme-Django-Framework.jpg](https://i.postimg.cc/X7d4V61X/Mekanisme-Django-Framework.jpg)](https://postimg.cc/xcfWRh2S)

### 2. Jelaskan mengapa kita menggunakan ***virtual environment***? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan ***virtual environment***?
*Virtual environment* digunakan untuk membuat *environment* yang terisolasi sehingga *package* yang digunakan untuk membuat aplikasi tidak akan berbenturan dengan *package* yang digunakan untuk aplikasi lain. Dengan menggunakan *virtual environment*, kita dapat mengatur *package* yang digunakan untuk setiap aplikasi yang kita buat. Selain itu, kita juga dapat mengatur versi dari *package* yang digunakan untuk setiap aplikasi yang kita buat. Oleh karena itu, kita menggunakan *virtual environment* untuk membuat aplikasi web berbasis Django.

Sebenarnya, kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*, namun *package* yang digunakan akan terinstall secara global sehingga dapat berpotensi terjadi *package* yang berbenturan dan tidak dapat mengatur versi dari *package* yang digunakan karena *package* yang digunakan akan terinstall secara global.

### 3. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC, MVT, dan MVVM merupakan arsitektur yang digunakan untuk membangun aplikasi. Perbedaan dari ketiganya adalah sebagai berikut:
- MVC (Model-View-Controller) merupakan arsitektur yang memisahkan aplikasi menjadi 3 bagian, yaitu *model*, *view*, dan *controller*. *Model* berfungsi untuk mengatur data, *view* berfungsi untuk mengatur tampilan, dan *controller* berfungsi untuk mengatur logika. *Controller* berfungsi sebagai penghubung antara *model* dan *view*. *Model* dan *view* tidak saling berhubungan.
- MVT (Model-View-Template) merupakan arsitektur yang memisahkan aplikasi menjadi 3 bagian, yaitu *model*, *view*, dan *template*. *Model* berfungsi untuk mengatur data, *view* berfungsi untuk mengatur logika, dan *template* berfungsi untuk mengatur tampilan. *View* berfungsi sebagai penghubung antara *model* dan *template*. *Model* dan *template* tidak saling berhubungan.
- MVVM (Model-View-ViewModel) merupakan arsitektur yang memisahkan aplikasi menjadi 3 bagian, yaitu *model*, *view*, dan *view model*. *Model* berfungsi untuk mengatur data, *view* berfungsi untuk mengatur tampilan, dan *view model* berfungsi untuk mengatur logika. *View model* berfungsi sebagai penghubung antara *model* dan *view*. *Model* dan *view* tidak saling berhubungan.

Secara umum, perbedaan dari ketiganya adalah pada *controller* dan *view model*. *Controller* pada MVC berfungsi untuk mengatur logika, sedangkan *view model* pada MVVM berfungsi untuk mengatur logika. *Controller* pada MVC berfungsi sebagai penghubung antara *model* dan *view*, sedangkan *view model* pada MVVM berfungsi sebagai penghubung antara *model* dan *view*. *Controller* pada MVC dan *view model* pada MVVM tidak saling berhubungan. Pada MVT, tidak terdapat *controller* maupun *view model*.