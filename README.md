
# Blockbuster
Blockbuster merupakan aplikasi yang digunakan untuk memanajemen data film. Aplikasi ini dibuat menggunakan bahasa pemrograman Python dan menggunakan framework Django. Aplikasi ini dibuat untuk memenuhi tugas besar mata kuliah Pemrograman Berbasis Platform yang diselenggarakan oleh Fakultas Ilmu Komputer, Universitas Indonesia.

## Author
- Nama: Jessica Ruth Damai Yanti Manurung
- NPM: 2206082783
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

# Tugas 3: Implementasi Form dan Data Delivery pada Django

## *Step-by-step* Implementasi Form dan Data Delivery

### 0. Implementasi *Skeleton* sebagai Kerangka *Views*
Sebelum memulai, saya membuat *skeleton* sebagai kerangka *views* dengan membuat *folder* `templates` pada *root folder* dan membuat berkas `base.html` pada *folder* `templates`. Berikut isi dari berkas `base.html`:
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
```
Setelah itu, saya mengubah berkas `main/templates/index.html` menjadi sebagai berikut:
```
{% extends 'base.html' %}

{% block meta %}
    <title>Blockbuster</title>
{% endblock meta %}

{% block content %}
    <h1> Blockbuster </h1>
    <h2> A simple movie database </h2>

    <h4> Name: </h4>
    <p> {{ name }} </p>
    <h4> NPM: </h4>
    <p> {{ npm }} </p>
    <h4> Class: </h4>
    <p> {{ class }} </p>
{% endblock content %}
```
Buka `settings.py` dan tambahkan `templates` pada `DIRS` pada `TEMPLATES`. Berikut isi dari berkas `settings.py`:
```
...
TEMPLATES = [
    {
        ...,
        "DIRS": [BASE_DIR / "templates"],
        ...,
    },
]
...
```

### 1. Membuat *input* `form` untuk *model* `Item`
Selanjutnya, saya membuat *input* `form` untuk *model* `Item` pada berkas `main/forms.py`. Berikut isi dari berkas `main/forms.py`:
```
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
```
Setelah itu, saya membuka berkas `main/views.py` dan mengubahnya menjadi sebagai berikut:
```
from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

# Create your views here.
def index(request):
    items = Item.objects.all()
    context = {
        "name": "Jessica Ruth Damai Yanti Manurung",
        "npm": "2206082783",
        "class": "PBP C",
        "items": items,
    }
    return render(request, 'index.html', context)

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ItemForm()
    return render(request, 'form.html', {'form': form})
```
Setelah itu, saya membuat *template* `form.html` pada berkas `main/templates/form.html`. Berikut isi dari berkas `main/templates/form.html`:
```
{% extends 'base.html' %}

{% block meta %}
    <title>Blockbuster</title>
{% endblock meta %}

{% block content %}
    <h1> Blockbuster </h1>
    <h2> A simple movie database </h2>

    <form method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
{% endblock content %}
```
Setelah itu, saya membuat *url* `create_item` pada berkas `main/urls.py`. Berikut isi dari berkas `main/urls.py`:
```
...
urlpatterns = [
    ...,
    path('create/', views.create_item, name='create'),
]
```
Setelah itu, saya mengubah berkas `main/templates/index.html` menjadi sebagai berikut:
```
{% extends 'base.html' %}

{% block meta %}
    <title>Blockbuster</title>
{% endblock meta %}

{% block content %}
    <h1> Blockbuster </h1>
    <h2> A simple movie database </h2>

    <h4> Name: </h4>
    <p> {{ name }} </p>
    <h4> NPM: </h4>
    <p> {{ npm }} </p>
    <h4> Class: </h4>
    <p> {{ class }} </p>

    <table>
        <tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Description</th>
            <th>Price</th>
            <th>Year</th>
            <th>Genre</th>
            <th>Duration</th>
            <th>Rating</th>
            <th>Image</th>
        </tr>
        {% for item in items %}
        <tr>
            <td>{{ item.name }}</td>
            <td>{{ item.amount }}</td>
            <td>{{ item.description }}</td>
            <td>{{ item.price }}</td>
            <td>{{ item.year }}</td>
            <td>{{ item.genre }}</td>
            <td>{{ item.duration }}</td>
            <td>{{ item.rating }}</td>
            <td><img src="{{ item.image.url }}" alt="Image" width="100" height="100"></td>
        </tr>
        {% endfor %}
    </table>

    <a href="{% url 'main:create' %}">Create Item</a>
{% endblock content %}
```
Setelah itu, berkas `settings.py` perlu dimodifikasi untuk mengatur berkas *media*. Berikut isi dari berkas `settings.py`:
```
...
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```
Lalu, saya membuat *url* `media` pada berkas `blockbuster/urls.py`. Berikut isi dari berkas `blockbuster/urls.py`:
```
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
Setelah itu, saya mengubah *unit test* pada berkas `main/tests.py` menjadi sebagai berikut:
```
...
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
        self.assertEqual(ponyo.image, '/media/images/Ponyo_(2008).png')
        ponyo.image.delete()
```
Dengan ini, *input* `form` untuk *model* `Item` telah selesai dibuat.

### 2. Menampilkan data dari *model* `Item` dalam format XML, JSON, XML *by* ID, dan JSON *by* ID
Untuk menampilkan data dari *model* `Item` dalam format XML, JSON, XML *by* ID, dan JSON *by* ID, saya membuat *view* `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id` pada berkas `main/views.py` serta meng-*import* `HttpResponse` dari `django.http` dan `serializers` dari `django.core`. Berikut isi dari berkas `main/views.py`:
```
...
from django.http import HttpResponse
from django.core import serializers
...
def show_xml(request):
    items = Item.objects.all()
    data = serializers.serialize('xml', items)
    return HttpResponse(data, content_type='application/xml')

def show_json(request):
    items = Item.objects.all()
    data = serializers.serialize('json', items)
    return HttpResponse(data, content_type='application/json')

def show_xml_by_id(request, id):
    item = Item.objects.get(id=id)
    data = serializers.serialize('xml', [item])
    return HttpResponse(data, content_type='application/xml')

def show_json_by_id(request, id):
    item = Item.objects.get(id=id)
    data = serializers.serialize('json', [item])
    return HttpResponse(data, content_type='application/json')
```
Dengan ini, *view* untuk menampilkan data dari *model* `Item` dalam format XML, JSON, XML *by* ID, dan JSON *by* ID telah selesai dibuat.

### 3. Menambahkan *routing* untuk *view* `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id`
Setelah *view* dibuat, saya membuat *url* `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id` pada berkas `main/urls.py`. Berikut isi dari berkas `main/urls.py`:
```
...
urlpatterns = [
    ...,
    path('show/xml/', views.show_xml, name='show_xml'),
    path('show/json/', views.show_json, name='show_json'),
    path('show/xml/<int:id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('show/json/<int:id>/', views.show_json_by_id, name='show_json_by_id'),
]
```
### 4. Melakukan *Testing* untuk *view* `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id` menggunakan *Postman*
Setelah *url* dibuat, saya melakukan *testing* untuk *view* `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id` menggunakan *Postman*. Berikut adalah hasil *testing* yang telah dilakukan:
- *Testing* untuk *view* `show_xml`:
[![image](https://i.postimg.cc/W44dRgkh/xml.png)](https://i.postimg.cc/W44dRgkh/xml.png)
- *Testing* untuk *view* `show_json`:
[![image](https://i.postimg.cc/RZ43RjC1/json.png)](https://i.postimg.cc/RZ43RjC1/json.png)
- *Testing* untuk *view* `show_xml_by_id`:
[![image](https://i.postimg.cc/hG3fKvLM/xmlid.png)](https://i.postimg.cc/hG3fKvLM/xmlid.png)
- *Testing* untuk *view* `show_json_by_id`:
[![image](https://i.postimg.cc/tChZFXbC/jsonid.png)](https://i.postimg.cc/tChZFXbC/jsonid.png)
- *Testing* untuk *view* `index`:
[![image](https://i.postimg.cc/9QbDNJz6/html.png)](https://i.postimg.cc/9QbDNJz6/html.png)

## Menjawab Pertanyaan-Pertanyaan
### 1. Apa perbedaan antara form `POST` dan form `GET` dalam Django?
Dalam Django, ada perbedaan antara penggunaan form `POST` dan form `GET`. Ini berkaitan dengan bagaimana data dikirimkan antara halaman web dan server. Berikut adalah perbedaan antara kedua metode tersebut:
1. Form `POST`:
- Metode `POST` digunakan untuk mengirimkan data yang sensitif atau data yang akan mengubah status di server.
- Data yang dikirimkan menggunakan metode `POST` tidak akan ditampilkan di URL.
- Metode `POST` cocok digunakan untuk mengirimkan data seperti formulir pendaftaran, formulir login, dan lain-lain.
2. Form `GET`:
- Metode `GET` digunakan untuk mengambil data dari server.
- Data yang dikirimkan menggunakan metode `GET` akan ditampilkan di URL sehingga dapat dilihat oleh pengguna.
- Metode `GET` cocok digunakan untuk mengambil data seperti hasil pencarian, halaman detail, dan lain-lain.

### 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
XML, JSON, dan HTML merupakan format yang digunakan untuk mengirimkan data. Berikut adalah perbedaan utama antara ketiganya:
1. XML (Extensible Markup Language):
- XML dikembangkan sebagai alat serialisasi data dan fokus pada penyimpanan data dengan cara yang mudah untuk dapat dibaca mesin.
- XML menggunakan struktur pohon untuk menyimpan data dengan *namespace* untuk kategori data yang berbeda.
- XML memiliki sintaksis yang lebih kompleks dan memakan banyak ruang.
- XML mendukung semua tipe data JSON dan tipe-tipe tambahan seperti *Boolean*, tanggal, citra, dan *namespace*.
- XML lebih cocok untuk struktur dokumen kompleks yang memerlukan pertukaran data.
2. JSON (JavaScript Object Notation):
- JSON didesain untuk pertukaran data dan menyediakan format yang lebih sederhana serta ringkas.
- JSON menggunakan struktur *key-value* untuk menyimpan data.
- JSON memiliki sintaksis yang lebih padat, lebih mudah dibaca dan ditulis.
- JSON memiliki ukuran file yang lebih kecil dan transmisi data yang lebih cepat.
- JSON umumnya merupakan pilihan yang lebih baik untuk API, aplikasi seluler, dan penyimpanan data.
3. HTML (Hypertext Markup Language):
- HTML adalah bahasa markup yang digunakan untuk membuat halaman web.
- HTML memiliki tanda standar yang harus digunakan semua orang.
- HTML menggunakan pengetikan dinamis, yang memungkinkan perubahan pada halaman web dengan data masuk baru.
- HTML bekerja dengan XML untuk menyajikan data yang konsisten dan relevan bagi pengunjung situs web.

Dalam konteks pengiriman data, XML lebih cocok untuk struktur dokumen kompleks yang memerlukan pertukaran data, sedangkan JSON lebih cocok untuk pertukaran data yang sederhana dan ringkas seperti API, aplikasi seluler, dan penyimpanan data. HTML digunakan untuk membuat halaman web dan bekerja dengan XML untuk menyajikan data yang konsisten dan relevan bagi pengunjung situs web.

### 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena memiliki beberapa keunggulan dan fitur yang membuatnya menjadi format yang populer. Berikut adalah beberapa alasan mengapa JSON sering digunakan:
1. Ringan dan Mudah Dibaca: JSON menggunakan format teks yang sederhana dan mudah dibaca oleh manusia. Struktur data JSON menggunakan pasangan nama dan nilai yang intuitif, seperti objek dan array, sehingga lebih mudah dipahami dan dianalisis.
2. Kompatibilitas dengan Bahasa Pemrograman: JSON didukung oleh hampir semua bahasa pemrograman. Hal ini membuatnya menjadi format yang ideal untuk pertukaran data antara aplikasi yang ditulis dalam bahasa pemrograman yang berbeda. Objek JSON dapat dengan mudah diubah menjadi objek atau struktur data yang sesuai dengan bahasa pemrograman yang digunakan.
3. Dukungan untuk Struktur Data Terkelompok dan Bersarang: JSON memungkinkan penggunaan struktur data terkelompok dan bersarang. Ini berarti kita dapat menyimpan data dengan tingkat kompleksitas yang tinggi dan mengatur data dalam hierarki yang berbeda. Ini sangat berguna ketika kita perlu mengirim atau menerima data yang memiliki relasi atau tingkat kedalaman yang kompleks.
4. Mendukung Tipe Data Umum: JSON mendukung tipe data umum seperti string dan angka.Selain itu, JSON juga mendukung tipe data khusus seperti null. Ini membuatnya cukup fleksibel dalam merepresentasikan berbagai jenis data.
5. Mendukung Pemrosesan Data Secara Efisien: JSON memiliki dukungan yang baik untuk pemrosesan data. Banyak bahasa pemrograman memiliki library atau modul JSON built-in atau pihak ketiga yang memungkinkan pengolahan data JSON dengan mudah. Misalnya, di Java, kita dapat menggunakan library Jackson atau Gson untuk membaca dan menulis data JSON.

Dalam kesimpulannya, JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena kemampuannya yang ringan, mudah dibaca, dan kompatibel dengan banyak bahasa pemrograman. JSON juga mendukung struktur data terkelompok dan bersarang, serta memiliki dukungan yang baik untuk pemrosesan data. Semua ini menjadikan JSON sebagai format yang populer dan efisien untuk pertukaran data antara aplikasi web modern.
