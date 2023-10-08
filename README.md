
# Blockbuster
Blockbuster merupakan aplikasi yang digunakan untuk memanajemen data film. Aplikasi ini dibuat menggunakan bahasa pemrograman Python dan menggunakan framework Django. Aplikasi ini dibuat untuk memenuhi tugas besar mata kuliah Pemrograman Berbasis Platform yang diselenggarakan oleh Fakultas Ilmu Komputer, Universitas Indonesia.

Website dapat diakses melalui 
- [https://jessica-ruth-tugas.pbp.cs.ui.ac.id/](https://jessica-ruth-tugas.pbp.cs.ui.ac.id/)
- [https://jess-blockbuster.adaptable.app/](https://jess-blockbuster.adaptable.app/) (backup)

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


# Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django

## *Step-by-step* Implementasi Autentikasi, Session, dan Cookies

### 0. Menambahkan pesan total item pada *template*
Sebelum memulai, saya menambahkan pesan total item pada *template* `index.html` pada berkas `main/templates/index.html`. Berikut kode yang saya tambahkan di atas tag `<table>`:
```
{% if items %}
    <p>Total Item: {{ items|length }}</p>
{% endif %}
```

### 1. Membuat fungsi dan form untuk registrasi
Selanjutnya, saya membuat fungsi dan form untuk registrasi pada berkas `main/views.py`. Berikut isi dari berkas `main/views.py`:
```
...
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
...
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('main:login')
    context = {
        'form': UserCreationForm(),
    }
    return render(request, 'register.html', context)
```
Setelah itu, saya membuat *template* `register.html` pada berkas `main/templates/register.html`. Berikut isi dari berkas `main/templates/register.html`:
```
{% extends 'base.html' %}

{% block meta %}
    <title>Blockbuster</title>
{% endblock meta %}

{% block content %}
    <h1> Blockbuster </h1>
    <h2> A simple movie database </h2>

    <h4> Register </h4>
    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
        </table>
        <button type="submit">Register</button>
    </form>

    {% if messages %}
        {% for message in messages %}
            <p>{{ message }}</p>
        {% endfor %}
    {% endif %}
{% endblock content %}
```
Setelah itu, saya membuat *url* `register` pada berkas `main/urls.py`. Berikut isi dari berkas `main/urls.py`:
```
...
urlpatterns = [
    ...,
    path('register/', views.register, name='register'),
]
```

### 2. Membuat fungsi dan form untuk login
Selanjutnya, saya membuat fungsi dan form untuk login pada berkas `main/views.py`. Berikut isi dari berkas `main/views.py`:
```
...
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
...
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}!')
            return redirect('main:index')
    context = {
        'form': AuthenticationForm(),
    }
    return render(request, 'login.html', context)
```
Setelah itu, saya membuat *template* `login.html` pada berkas `main/templates/login.html`. Berikut isi dari berkas `main/templates/login.html`:
```
{% extends 'base.html' %}

{% block meta %}
    <title>Blockbuster</title>
{% endblock meta %}

{% block content %}
    <h1> Blockbuster </h1>
    <h2> A simple movie database </h2>

    <h4> Login </h4>
    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
        </table>
        <button type="submit">Login</button>
    </form>

    {% if messages %}
        {% for message in messages %}
            <p>{{ message }}</p>
        {% endfor %}
    {% endif %}
{% endblock content %}
```
Setelah itu, saya membuat *url* `login` pada berkas `main/urls.py`. Berikut isi dari berkas `main/urls.py`:
```
...
urlpatterns = [
    ...,
    path('login/', views.login_user, name='login'),
]
```

### 3. Membuat fungsi untuk logout
Selanjutnya, saya membuat fungsi untuk logout pada berkas `main/views.py`. Berikut isi dari berkas `main/views.py`:
```
...
from django.contrib.auth import login, logout
...
def logout_user(request):
    logout(request)
    return redirect('main:index')
```
Setelah itu, saya membuat *url* `logout` pada berkas `main/urls.py`. Berikut isi dari berkas `main/urls.py`:
```
...
urlpatterns = [
    ...,
    path('logout/', views.logout_user, name='logout'),
]
```

### 4. Menambahkan *url* `register`, `login`, dan `logout` pada *template*
Selanjutnya, saya menambahkan *url* untuk `register`, `login`, dan `logout` pada *template* `index.html` pada berkas `main/templates/index.html`. Saya juga mengubah *url* `create` menjadi `create_item`. Berikut kode yang saya tambahkan di bawah *table*:
```
{% if user.is_authenticated %}
    <a href="{% url 'main:create' %}">Create Item</a>
    <a href="{% url 'main:logout' %}">Logout</a>
{% else %}
    <a href="{% url 'main:register' %}">Register</a>
    <a href="{% url 'main:login' %}">Login</a>
{% endif %}
```

### 5. Merestrict *view* `create_item` agar hanya dapat diakses oleh pengguna yang sudah *login*
Selanjutnya, saya merestrict *view* `create_item` agar hanya dapat diakses oleh pengguna yang sudah *login* pada berkas `main/views.py`. Berikut isi dari berkas `main/views.py`:
```
...
from django.contrib.auth.decorators import login_required
...
@login_required(login_url='main:login')
def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:index')
    else:
        form = ItemForm()
    return render(request, 'form.html', {'form': form})
```
Selain itu, saya mengubah *forms* pada berkas `main/forms.py` menjadi sebagai berikut:
```
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'amount', 'description', 'price', 'year', 'genre', 'duration', 'rating', 'image']
```

### 6. Menghilangkan *table* *item* pada *template* `index.html` jika pengguna belum *login*
Selanjutnya, saya menghilangkan *table* pada *template* `index.html` jika pengguna belum *login* pada berkas `main/templates/index.html`. Berikut kode yang saya tambahkan:
```
    {% if user.is_authenticated %}
    <table>
        ...
    </table>
    {% endif %}
```

### 7. Menghubungkan model `Item` dengan model `User`
Selanjutnya, saya menghubungkan model `Item` dengan model `User` pada berkas `main/models.py`. Berikut isi dari berkas `main/models.py`:
```
...
from django.contrib.auth.models import User
...
class Item(models.Model):
    ...
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```
> **Catatan:** *Database* perlu di-*migrate* setelah mengubah model. Jika terjadi *error* saat *migrate*, hapus *database* dan *migrate* ulang.

Selain itu, saya mengubah *view* `create_item` pada berkas `main/views.py` menjadi sebagai berikut:
```
...
@login_required(login_url='main:login')
def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('main:index')
    else:
        form = ItemForm()
    return render(request, 'form.html', {'form': form})
```

### 8. Menampilkan informasi pengguna pada *template* `index.html`
Selanjutnya, saya menampilkan informasi pengguna pada *template* `index.html` pada berkas `main/templates/index.html`. Berikut kode yang saya tambahkan di atas *table*:
```
{% if user.is_authenticated %}
    <p>Username: {{ user.username }}</p>
{% endif %}
```
Selain itu, saya menghapus nama, NPM, dan kelas pada *template* `index.html` pada berkas `main/templates/index.html`. Berikut kode yang saya hapus:
```
<h4> Name: </h4>
<p> {{ name }} </p>
<h4> NPM: </h4>
<p> {{ npm }} </p>
<h4> Class: </h4>
<p> {{ class }} </p>
```
Saya juga mengubah *view* `index` pada berkas `main/views.py` menjadi sebagai berikut:
```
...
def index(request):
    if request.user.is_authenticated:
        items = Item.objects.filter(user=request.user)
    else:
        items = []
    context = {
        "items": items,
    }
    return render(request, 'index.html', context)
```

### 9. Menerapkan *cookies* pada proyek
Selanjutnya, saya menerapkan *cookies* pada proyek dengan menambahkan *cookies* pada *view* `login_user` pada berkas `main/views.py`. Berikut isi dari berkas `main/views.py`:
```
...
from datetime import datetime
...
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}!')
            response = redirect('main:index')
            response.set_cookie('last_login', str(datetime.now()))
            return response
    context = {
        'form': AuthenticationForm(),
    }
    return render(request, 'login.html', context)
```
Selain itu, saya menambahkan *cookies* pada *view* `logout_user` pada berkas `main/views.py`. Berikut isi dari berkas `main/views.py`:
```
...
def logout_user(request):
    logout(request)
    response = redirect('main:index')
    response.delete_cookie('last_login')
    return response
```
Selain itu, saya menambahkan *cookies* pada *view* `index` pada berkas `main/views.py`. Berikut isi dari berkas `main/views.py`:
```
...
def index(request):
    if request.user.is_authenticated:
        items = Item.objects.filter(user=request.user)
    else:
        items = []
    context = {
        "items": items,
    }
    response = render(request, 'index.html', context)
    if request.COOKIES.get('last_login'):
        response.set_cookie('last_login', request.COOKIES.get('last_login'))
    return response
```
Selanjutnya, saya menampilkan *cookies* pada *template* `index.html` pada berkas `main/templates/index.html`. Berikut kode yang saya tambahkan di atas *table*:
```
{% if request.COOKIES.last_login %}
    <p>Last Login: {{ request.COOKIES.last_login }}</p>
{% endif %}
```

### 10. Menambahkan *button* untuk menambahkan dan mengurangi *amount* dan menghapus *item*
Selanjutnya, saya membuat fungsi untuk menambahkan dan mengurangi *amount* dan menghapus *item* pada berkas `main/views.py`. Berikut isi dari berkas `main/views.py`:
```
...
@login_required(login_url='main:login')
def add_amount(request, id):
    item = Item.objects.get(id=id)
    if request.user == item.user:
        item.amount += 1
        item.save()
    return redirect('main:index')

@login_required(login_url='main:login')
def reduce_amount(request, id):
    item = Item.objects.get(id=id)
    if request.user == item.user:
        if item.amount > 0:
            item.amount -= 1
            item.save()
        else:
            item.delete()
    return redirect('main:index')

@login_required(login_url='main:login')
def delete_item(request, id):
    item = Item.objects.get(id=id)
    if request.user == item.user:
        item.delete()
    return redirect('main:index')
```
Selain itu, saya menambahkan *url* `add_amount`, `reduce_amount`, dan `delete_item` pada berkas `main/urls.py`. Berikut isi dari berkas `main/urls.py`:
```
...
urlpatterns = [
    ...,
    path('item/add/<int:id>/', views.add_amount, name='add_amount'),
    path('item/reduce/<int:id>/', views.reduce_amount, name='reduce_amount'),
    path('item/delete/<int:id>/', views.delete_item, name='delete_item'),
]
```
Selanjutnya, saya menambahkan *button* untuk menambahkan dan mengurangi *amount* dan menghapus *item* pada *template* `index.html` pada berkas `main/templates/index.html`. Berikut kode yang saya tambahkan di bawah *table*:
```
{% if user.is_authenticated %}
    <table>
        ...
        <tr>
            ...
            <th>Actions</th>
        </tr>
        {% for item in items %}
        <tr>
            ...
            <td>
                <a href="{% url 'main:add_amount' item.id %}">Add</a>
                <a href="{% url 'main:reduce_amount' item.id %}">Reduce</a>
                <a href="{% url 'main:delete_item' item.id %}">Delete</a>
            </td>
        </tr>
        {% endfor %}
    </table>
{% endif %}
```

### Membuat dua akun pengguna dengan masing-masing tiga dummy data
Selanjutnya, saya membuat dua akun pengguna dengan masing-masing tiga dummy data. Berikut adalah hasilnya:
[![akun1](https://i.postimg.cc/dQbkNVCY/andi.png)](https://i.postimg.cc/dQbkNVCY/andi.png)
[![akun2](https://i.postimg.cc/8zH7Cd0p/budi.png)](https://i.postimg.cc/8zH7Cd0p/budi.png)


## Menjawab Pertanyaan-Pertanyaan
### Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?
Django `UserCreationForm` adalah formulir bawaan yang disediakan oleh Django untuk mempermudah proses pembuatan *user* baru dalam aplikasi web yang menggunakan Django. *Class* ini termasuk dalam modul `django.contrib.auth.forms` dan digunakan untuk mengumpulkan data yang diperlukan untuk membuat akun pengguna.
Kelebihan dari Django `UserCreationForm` adalah sebagai berikut:
- Mudah digunakan: Bagi seorang developer aplikasi yang menggunakan Django, `UserCreationForm` sangat mempermudah developer dalam pembuatan alur register yang cepat dan mudah sehingga mempercepat proses pembuatan aplikasi.
- Terintegrasi dengan sistem keamanan Django: Password yang disimpan dari formulir ini akan di hash oleh django sehingga penyimpanan password dapat menjadi lebih aman.
- Memiliki syarat validasi password: Password pada formulir ini memiliki minimum jumlah kata dengan syarat beberapa karakter penting untuk harus tercantum pada password sehingga menjadi lebih kuat.

Namun, Django UserCreationForm juga memiliki beberapa kekurangan:
- Hanya memiliki formulir standar: UserCreationForum hanya menerima input username, email dan password. Apabila memerlukan input lain maka formulir perlu dicustom terlebih dahulu.
- Tidak terverifikasi email: Formulir ini hanya digunakan untuk menerima input sebagai pembuatan user dalam aplikasi, akan tetapi jika diperlukan langkah lebih lanjut seperti verifikasi email maka perogram perlu dikustomisasi lebih lanjut.

### Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi adalah proses memverifikasi identitas pengguna. Dalam konteks aplikasi web, autentikasi biasanya melibatkan pengguna memasukkan kredensial seperti nama pengguna dan kata sandi, yang kemudian sistem verifikasi apakah kredensial tersebut sesuai dengan yang ada dalam basis data. Jika cocok, pengguna dianggap terotentikasi dan dapat mengakses sumber daya yang terlindungi oleh aplikasi web.

Otorisasi, di sisi lain, adalah proses memberikan atau menolak akses ke sumber daya tertentu kepada pengguna yang sudah terotentikasi. Otorisasi menentukan apa yang diizinkan atau tidak diizinkan untuk dilakukan oleh pengguna yang terotentikasi. Otorisasi mengontrol hak akses pengguna.

Autentikasi dan otorisasi sangat penting dalam Django dan aplikasi web pada umumnya. Autentikasi memastikan bahwa hanya pengguna yang sah yang dapat mengakses aplikasi, sedangkan otorisasi memastikan bahwa pengguna hanya dapat melakukan tindakan yang sesuai dengan izin mereka. Kedua proses ini bekerja bersama-sama untuk menjaga keamanan aplikasi web. Autentikasi memastikan bahwa hanya pengguna yang sah yang dapat mengakses aplikasi, sedangkan otorisasi memastikan bahwa pengguna hanya dapat melakukan tindakan yang sesuai dengan izin mereka

### Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data *session* pengguna?
Dalam konteks aplikasi web, cookies adalah sejenis data kecil yang disimpan di browser pengguna oleh server web. Tujuan utamanya adalah untuk menyimpan informasi tentang pengguna dan membantu dalam melacak dan mengidentifikasi pengguna ketika mereka kembali ke situs web.

Django menggunakan cookies dalam konteks *session* pengguna. *session* adalah mekanisme yang digunakan oleh Django dan sebagian besar internet untuk melacak "keadaan" antara situs dan browser tertentu. *session* memungkinkan Anda menyimpan data sembarang per browser, dan data ini tersedia untuk situs setiap kali browser terhubung. Django menggunakan cookie yang berisi id *session* khusus untuk mengidentifikasi setiap browser dan *session*nya dengan situs. Data *session* disimpan dalam basis data situs secara *default*.

### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Dalam pengembangan web, penggunaan cookies membantu dalam mempertahankan status pengguna (seperti status login) dan menyimpan preferensi pengguna. Namun, ada beberapa risiko keamanan yang harus diwaspadai ketika menggunakan cookies. Berikut adalah beberapa risiko keamanan yang harus diwaspadai:
- Eksploitasi cookies: Cookies bisa dieksploitasi untuk melakukan serangan seperti Cross-Site Scripting (XSS) dan Cross-Site Request Forgery (CSRF). Dalam serangan XSS, penyerang bisa mencuri cookies dan menggunakan mereka untuk mengambil alih sesi pengguna. Sementara itu, dalam serangan CSRF, penyerang bisa memanfaatkan cookies untuk melakukan tindakan berbahaya seolah-olah dilakukan oleh pengguna yang sah.
- Pembocoran data: Cookies sering digunakan untuk menyimpan data pengguna, yang jika tidak ditangani dengan benar, bisa membocorkan data pengguna yang sensitif. Misalnya, jika cookies disimpan dalam transmisi yang tidak aman, mereka bisa dibaca oleh pihak ketiga. Oleh karena itu, penting untuk selalu menggunakan koneksi aman (HTTPS, bukan HTTP) saat mengirim cookies
- Pelacakan pengguna: Cookies, khususnya cookies pihak ketiga, bisa digunakan untuk melacak aktivitas penggunaan internet pengguna. Ini bisa menjadi masalah privasi, karena informasi tentang kebiasaan browsing pengguna bisa dikumpulkan tanpa sepengetahuan mereka.


# Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS

## *Step-by-step* Desain Web menggunakan HTML, CSS dan Framework CSS

### 1. Menambahkan *stylesheet* Bootstrap pada *template* `base.html`
Pertama, saya menambahkan *stylesheet* Bootstrap pada *template* `base.html` pada berkas `templates/base.html`. Berikut kode yang saya tambahkan di antara tag `<head>`:
```
...
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>    
```

### 2. Mengkostumisasi *template* `base.html`
Selanjutnya, saya mengkostumisasi *template* `base.html` pada berkas `templates/base.html`. Berikut kode yang saya tambahkan di antara tag `<body>`:
```
<body style="background-color: #F8E8EE;">
    {% block content %}
    {% endblock content %}
</body>
```

### 3. Mengkostumisasi *template* `login.html`
Selanjutnya, saya mengkostumisasi *template* `login.html` pada berkas `main/templates/login.html`. Berikut kode yang saya tambahkan di *block* `content`:
```
    <section class="vh-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-12 col-md-8 col-lg-6 col-xl-5">
                <div class="container-fluid mt-5">
                    <div class="row">
                        <div class="col-12">
                            <h1 class="text-center" style="color: #F2BED1;">Blockbuster</h1>
                        </div>
                    </div>
                </div>
              <div class="card text-white" style="border-radius: 1rem; background-color: #F2BED1;">
                <div class="card-body p-5 text-center">
      
                  <form class="mb-md-5 mt-md-4 pb-5" method="POST">
                    {% csrf_token %}
      
                    <h2 class="fw-bold mb-4 text-uppercase">Login</h2>
      
                    <div class="form-outline form-white mb-4">
                        <label class="form-label" for="username">Username</label>
                      <input type="text" name="username" required id="username" class="form-control form-control-lg" />
                    </div>
      
                    <div class="form-outline form-white mb-4">
                        <label class="form-label" for="password">Password</label>
                      <input type="password" name="password" required id="password" class="form-control form-control-lg" />
                    </div>

                    <button class="btn btn-outline-light btn-lg px-5" type="submit">Login</button>
      
                  </form>
                  {% if messages %}
                    {% for message in messages %}
                        {% if message.tags == 'error' %}
                            <div class="alert alert-danger" role="alert">
                                {{ message }}
                            </div>
                        {% else %}
                            <div class="alert alert-success" role="alert">
                                {{ message }}
                            </div>
                        {% endif %}
                    {% endfor %}
                  {% endif %}
                  <div>
                    <p class="mb-0">Don't have an account? <a href="{% url "main:register" %}" class="text-white-50 fw-bold">Sign Up</a></p>
                  </div>
                </div>
              </div>
            </div>
        </div>
    </section>
```

### 4. Mengkostumisasi *template* `register.html`
Selanjutnya, saya mengkostumisasi *template* `register.html` pada berkas `main/templates/register.html`. Berikut kode yang saya tambahkan di *block* `content`:
```
<section class="vh-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-12 col-md-8 col-lg-6 col-xl-5">
            <div class="container-fluid mt-5">
                <div class="row">
                    <div class="col-12">
                        <h1 class="text-center" style="color: #F2BED1;">Blockbuster</h1>
                    </div>
                </div>
            </div>
          <div class="card text-white" style="border-radius: 1rem; background-color: #F2BED1;">
            <div class="card-body p-5 text-center">
  
              <form class="mb-md-5 mt-md-4 pb-5" method="POST">
                {% csrf_token %}
  
                <h2 class="fw-bold mb-4 text-uppercase">Register</h2>
  
                <div class="form-outline form-white mb-4">
                    <label class="form-label" for="username">Username</label>
                  <input type="text" name="username" required id="username" class="form-control form-control-lg" />
                </div>
  
                <div class="form-outline form-white mb-4">
                    <label class="form-label" for="password1">Password</label>
                  <input type="password" name="password1" required id="password1" class="form-control form-control-lg" />
                </div>
  
                <div class="form-outline form-white mb-4">
                    <label class="form-label" for="password2">Password Confirmation</label>
                  <input type="password" name="password2" required id="password2" class="form-control form-control-lg" />
                </div>

                <button class="btn btn-outline-light btn-lg px-5" type="submit">Register</button>
  
              </form>
              {% if messages %}
                {% for message in messages %}
                    {% if message.tags == 'error' %}
                        <div class="alert alert-danger text-white" role="alert">
                            <p>{{ message }}</p>
                        </div>
                    {% else %}
                        <div class="alert alert-success text-white" role="alert">
                            <p>{{ message }}</p>
                        </div>
                    {% endif %}
                {% endfor %}
              {% endif %}
              <div>
                <p class="mb-0">Have an account already? <a href="{% url "main:login" %}" class="text-white-50 fw-bold">Login</a></p>
              </div>
            </div>
          </div>
        </div>
    </div>
</section>
```

### 5. Mengkostumisasi *template* `form.html`
Selanjutnya, saya mengkostumisasi *template* `form.html` pada berkas `main/templates/form.html`. Berikut kode yang saya tambahkan di *block* `content`:
```
    <section class="vh-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-12 col-md-8 col-lg-6 col-xl-5">
                <div class="container-fluid mt-5">
                    <div class="row">
                        <div class="col-12">
                            <h1 class="text-center" style="color: #F2BED1;">Blockbuster</h1>
                        </div>
                    </div>
                </div>
              <div class="card text-white" style="border-radius: 1rem; background-color: #F2BED1;">
                <div class="card-body p-5 text-center">
      
                  <form class="mb-md-5 mt-md-4 pb-5" method="POST" enctype="multipart/form-data">
                    {% csrf_token %}
      
                    <h2 class="fw-bold mb-4 text-uppercase">Add Movie</h2>
      
                    <div class="form-outline form-white mb-4">
                        <label class="form-label" for="name">Name</label>
                      <input type="text" name="name" required id="name" class="form-control form-control-lg" />
                    </div>
      
                    <div class="form-outline form-white mb-4">
                        <label class="form-label" for="amount">Amount</label>
                      <input type="number" name="amount" required id="amount" class="form-control form-control-lg" />
                    </div>
      
                    <div class="form-outline form-white mb-4">
                        <label class="form-label" for="description">Description</label>
                      <textarea name="description" required id="description" class="form-control form-control-lg" rows="4"></textarea>
                    </div>
      
                    <div class="form-outline form-white mb-4">
                        <label class="form-label" for="price">Price</label>
                      <input type="number" name="price" required id="price" class="form-control form-control-lg" />
                    </div>
      
                    <div class="form-outline form-white mb-4">
                        <label class="form-label" for="year">Year</label>
                      <input type="number" name="year" required id="year" class="form-control form-control-lg" />
                    </div>
      
                    <div class="form-outline form-white mb-4">
                        <label class="form-label" for="genre">Genre</label>
                      <input type="text" name="genre" required id="genre" class="form-control form-control-lg" />
                    </div>
      
                    <div class="form-outline form-white mb-4">
                        <label class="form-label" for="duration">Duration</label>
                      <input type="number" name="duration" required id="duration" class="form-control form-control-lg" />
                    </div>
      
                    <div class="form-outline form-white mb-4">
                        <label class="form-label" for="rating">Rating</label>
                      <input type="number" name="rating" required id="rating" class="form-control form-control-lg" step="0.1" />
                    </div>
      
                    <div class="form-outline form-white mb-4">
                        <label class="form-label" for="image">Image</label>
                      <input type="file" name="image" accept="image/*" required id="image" class="form-control form-control-lg" />
                    </div>

                    <button class="btn btn-outline-light btn-lg px-5" type="submit">Add</button>
      
                  </form>
                  {% if messages %}
                    {% for message in messages %}
                        {% if message.tags == 'error' %}
                            <div class="alert alert-danger" role="alert">
                                {{ message }}
                            </div>
                        {% else %}
                            <div class="alert alert-success" role="alert">
                                {{ message }}
                            </div>
                        {% endif %}
                    {% endfor %}
                  {% endif %}
                  <div>
                    <p class="mb-0">Don't have an account? <a href="{% url "main:register" %}" class="text-white-50 fw-bold">Sign Up</a></p>
                  </div>
                </div>
              </div>
            </div>
        </div>
    </section>
```
Lalu, saya mengubah *form* pada berkas `main/forms.py` menjadi sebagai berikut:
```
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'amount', 'description', 'price', 'year', 'genre', 'duration', 'rating', 'image', 'user']
```
Dan saya mengubah *view* `create_item` pada berkas `main/views.py` menjadi sebagai berikut:
```
...
@login_required(login_url='main:login')
def create_item(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['user'] = request.user.id
        files = request.FILES.copy()
        form = ItemForm(data, files)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('main:index')
    return render(request, 'form.html')
```

### 6. Mengkostumisasi *template* `index.html`
Selanjutnya, saya mengkostumisasi *template* `index.html` pada berkas `main/templates/index.html`. Berikut kode yang saya tambahkan di *block* `content`:
```
<section class="text-center">
    <div class="container pt-5">
        <h1 style="color: #F2BED1">Blockbuster</h1>
        <h3>Movie Database</h3>
        <p class="lead text-muted"> This is a simple movie database where you can add and delete for movies. </p>
        <p>
            {% if user.is_authenticated %}
                <p class="lead text-muted">Username: {{ user.username }}<br/>
                Last Login: {{ request.COOKIES.last_login }}</p>
                <a href="{% url 'main:create' %}" class="btn btn-outline-dark my-2">Create Item</a>
                <a href="{% url 'main:logout' %}" class="btn btn-outline-secondary my-2">Logout</a>
            {% else %}
                <a href="{% url 'main:register' %}" class="btn btn-outline-dark my-2">Register</a>
                <a href="{% url 'main:login' %}" class="btn btn-outline-secondary my-2">Login</a>
            {% endif %}
        </p>
    </div>
</section>
{% if user.is_authenticated %}
    <section>
        <div class="container">
            {% if items %}
                <p class="lead text-muted">Total Item: {{ items|length }}</p>
            {% endif %}
            <div class="row row-cols-3">
                {% for item in items %}
                <div class="col-md-6 col-lg-4 mb-5">
                    <div class="card text-white" style="border-radius: 1rem; background-color: #F2BED1;">
                        <img src="{{ item.image.url }}" class="card-img-top" alt="Image" style="border-radius: 1rem 1rem 0 0;">
                        <div class="card-body">
                            <h5 class="card-title" style="color: #B0578D">{{ item.name }}</h5>
                            <p class="card-text">{{ item.description }}</p>
                            <p class="card-text">Amount: {{ item.amount }}</p>
                            <p class="card-text">Price: {{ item.price }}</p>
                            <p class="card-text">Year: {{ item.year }}</p>
                            <p class="card-text">Genre: {{ item.genre }}</p>
                            <p class="card-text">Duration: {{ item.duration }}</p>
                            <p class="card-text" style="color: #EBE76C;"><b>Rating: {{ item.rating }}</b></p>
                            <a href="{% url 'main:add_amount' item.id %}" class="btn btn-outline-dark my-2">Add</a>
                            <a href="{% url 'main:reduce_amount' item.id %}" class="btn btn-outline-secondary my-2">Reduce</a>
                            <a href="{% url 'main:delete_item' item.id %}" class="btn btn-outline-danger my-2">Delete</a>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
    </section>
{% endif %}
```
Dengan ini, desain web menggunakan HTML, CSS dan Framework CSS telah selesai dibuat.


## Menjawab Pertanyaan-Pertanyaan
### Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
Element selector adalah salah satu jenis selector CSS yang digunakan untuk memilih elemen HTML tertentu. Element selector dapat digunakan untuk memilih elemen berdasarkan tag name, class, atau ID.

Manfaat dari setiap element selector:
- Type selector: Manfaat type selector adalah untuk memilih elemen berdasarkan tag name. Misalnya, untuk memilih semua elemen `<h1>`, kita dapat menggunakan selector `h1`.
- Class selector: Manfaat class selector adalah untuk memilih elemen berdasarkan class. Misalnya, untuk memilih semua elemen dengan class `my-class`, kita dapat menggunakan selector `.my-class`.
- ID selector: Manfaat ID selector adalah untuk memilih elemen berdasarkan ID. Misalnya, untuk memilih elemen dengan ID `my-id`, kita dapat menggunakan selector `#my-id`.

Waktu yang tepat untuk menggunakan setiap element selector:
- Type selector: Type selector adalah pilihan yang tepat untuk memilih elemen berdasarkan tag name. Misalnya, untuk menerapkan gaya yang sama pada semua elemen `<h1>`, kita dapat menggunakan type selector `h1`.
- Class selector: Class selector adalah pilihan yang tepat untuk memilih elemen berdasarkan class. Misalnya, untuk menerapkan gaya yang sama pada semua elemen yang memiliki class `my-class`, kita dapat menggunakan class selector `.my-class`.
- ID selector: ID selector adalah pilihan yang tepat untuk memilih elemen berdasarkan ID. Misalnya, untuk menerapkan gaya yang unik pada elemen dengan ID `my-id`, kita dapat menggunakan ID selector `#my-id`.

### Jelaskan HTML5 Tag yang kamu ketahui.
HTML5 Tag adalah tag yang digunakan untuk membuat struktur dan konten sebuah dokumen HTML. HTML5 Tag terdiri dari dua jenis, yaitu:
- Structural Tags: Tag ini digunakan untuk menentukan struktur dari dokumen HTML. Misalnya, `<body>`, `<header>`, `<main>`, dan `<footer>`.
- Content Tags: Tag ini digunakan untuk menentukan konten dari dokumen HTML. Misalnya, `<p>`, `<h1>`, `<img>`, dan `<video>`.
Berikut adalah beberapa HTML5 Tag yang saya ketahui:

1. Structural Tags:
- `<html>`: Tag ini digunakan untuk mendefinisikan dokumen HTML.
- `<head>`: Tag ini digunakan untuk menyimpan informasi tentang dokumen HTML, seperti judul, meta tag, dan stylesheet.
- `<body>`: Tag ini digunakan untuk menyimpan konten utama dari dokumen HTML.
- `<header>`: Tag ini digunakan untuk menyimpan bagian header dari dokumen HTML.
- `<main>`: Tag ini digunakan untuk menyimpan bagian utama dari dokumen HTML.
- `<footer>`: Tag ini digunakan untuk menyimpan bagian footer dari dokumen HTML.
- `<nav>`: Tag ini digunakan untuk menyimpan bagian navigasi dari dokumen HTML.
- `<section>`: Tag ini digunakan untuk menyimpan bagian dari dokumen HTML yang memiliki hubungan tematik.
- `<article>`: Tag ini digunakan untuk menyimpan bagian dari dokumen HTML yang berisi konten independen.
- `<aside>`: Tag ini digunakan untuk menyimpan bagian dari dokumen HTML yang berisi konten tambahan.

2. Content Tags:
- `<p>`: Tag ini digunakan untuk membuat paragraf.
- `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`: Tag ini digunakan untuk membuat judul dengan ukuran teks yang berbeda-beda.
- `<img>`: Tag ini digunakan untuk memasukkan gambar ke dalam dokumen HTML.
- `<video>`: Tag ini digunakan untuk memasukkan video ke dalam dokumen HTML.
- `<audio>`: Tag ini digunakan untuk memasukkan audio ke dalam dokumen HTML.
- `<a>`: Tag ini digunakan untuk membuat tautan.
- `<b>`: Tag ini digunakan untuk membuat teks tebal.
- `<i>`: Tag ini digunakan untuk membuat teks miring.
- `<u>`: Tag ini digunakan untuk membuat teks bergaris bawah.
- `<strong>`: Tag ini digunakan untuk membuat teks dengan bobot yang lebih tinggi.
- `<em>`: Tag ini digunakan untuk membuat teks dengan penekanan.
- `<abbr>`: Tag ini digunakan untuk membuat singkatan.
- `<blockquote>`: Tag ini digunakan untuk membuat kutipan.
- `<code>`: Tag ini digunakan untuk membuat kode.
- `<pre>`: Tag ini digunakan untuk membuat kode yang tidak akan diformat oleh browser.
- `<ol>`: Tag ini digunakan untuk membuat daftar urut.
- `<ul>`: Tag ini digunakan untuk membuat daftar tidak urut.
- `<li>`: Tag ini digunakan untuk membuat item dalam daftar.
- `<table>`: Tag ini digunakan untuk membuat tabel.
- `<tr>`: Tag ini digunakan untuk membuat baris dalam tabel.
- `<td>`: Tag ini digunakan untuk membuat sel dalam tabel.
- `<th>`: Tag ini digunakan untuk membuat sel header dalam tabel.

Selain tag-tag yang disebutkan di atas, masih banyak lagi HTML5 Tag yang bisa digunakan untuk membuat dokumen HTML yang lebih kompleks dan interaktif.

### Jelaskan perbedaan antara margin dan padding.
Margin dan padding adalah properti CSS yang digunakan untuk mengatur jarak antara elemen HTML dengan elemen HTML lainnya. Perbedaan antara margin dan padding adalah sebagai berikut:
- Margin: Margin adalah jarak antara elemen HTML dengan elemen HTML lainnya. Margin memiliki empat sisi, yaitu top, right, bottom, dan left. Margin dapat diatur menggunakan properti CSS `margin`, `margin-top`, `margin-right`, `margin-bottom`, dan `margin-left`.
- Padding: Padding adalah jarak antara elemen HTML dengan konten di dalamnya. Padding memiliki empat sisi, yaitu top, right, bottom, dan left. Padding dapat diatur menggunakan properti CSS `padding`, `padding-top`, `padding-right`, `padding-bottom`, dan `padding-left`.

### Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
Tailwind CSS dan Bootstrap adalah dua framework CSS yang populer untuk membangun situs web dan aplikasi web. Keduanya menawarkan berbagai fitur dan keuntungan, tetapi juga memiliki beberapa perbedaan utama.

Perbedaan antara Tailwind CSS dan Bootstrap:
- Pendekatan: Tailwind CSS adalah framework CSS berbasis utilitas, sedangkan Bootstrap adalah framework CSS berbasis komponen.
- Ukuran: Tailwind CSS memiliki ukuran file yang lebih kecil daripada Bootstrap.
- Fleksibilitas: Tailwind CSS menawarkan lebih banyak fleksibilitas daripada Bootstrap.
- Kesesuaian: Tailwind CSS lebih cocok untuk proyek-proyek yang membutuhkan kustomisasi yang lebih tinggi, sedangkan Bootstrap lebih cocok untuk proyek-proyek yang membutuhkan pembuatan situs web atau aplikasi web yang cepat.

Kapan sebaiknya menggunakan Bootstrap daripada Tailwind:
- Jika Anda membutuhkan situs web atau aplikasi web yang cepat dan mudah dibangun: Bootstrap adalah pilihan yang baik jika Anda membutuhkan situs web atau aplikasi web yang cepat dan mudah dibangun. Bootstrap menawarkan berbagai komponen siap pakai yang dapat Anda gunakan untuk membuat situs web atau aplikasi web yang lengkap.
- Jika Anda membutuhkan situs web atau aplikasi web yang responsif: Bootstrap adalah pilihan yang baik jika Anda membutuhkan situs web atau aplikasi web yang responsif. Bootstrap menggunakan grid responsive yang dapat Anda gunakan untuk membuat situs web atau aplikasi web yang terlihat bagus di semua perangkat.

Kapan sebaiknya menggunakan Tailwind daripada Bootstrap:
- Jika Anda membutuhkan situs web atau aplikasi web yang unik dan kustom: Tailwind adalah pilihan yang baik jika Anda membutuhkan situs web atau aplikasi web yang unik dan kustom. Tailwind menawarkan lebih banyak fleksibilitas daripada Bootstrap, sehingga Anda dapat membuat situs web atau aplikasi web yang benar-benar sesuai dengan kebutuhan Anda.
- Jika Anda membutuhkan situs web atau aplikasi web yang ringan: Tailwind adalah pilihan yang baik jika Anda membutuhkan situs web atau aplikasi web yang ringan. Tailwind memiliki ukuran file yang lebih kecil daripada Bootstrap, sehingga situs web atau aplikasi web Anda akan dimuat lebih cepat.

Pada akhirnya, pilihan antara Tailwind dan Bootstrap tergantung pada kebutuhan dan preferensi Anda. Jika Anda membutuhkan situs web atau aplikasi web yang cepat dan mudah dibangun, Bootstrap adalah pilihan yang baik. Jika Anda membutuhkan situs web atau aplikasi web yang unik dan kustom, Tailwind adalah pilihan yang baik.


# Tugas 6: JavaScript dan Asynchronous JavaScript

## *Step-by-step* JavaScript dan Asynchronous JavaScript

### 1. Membuat fungsi untuk mengembalikan data JSON
Pertama, saya membuat fungsi untuk mengembalikan data JSON pada berkas `main/views.py`. Berikut kode yang saya tambahkan:
```
...
@login_required(login_url='main:login')
def get_item_json(request):
    items = Item.objects.filter(user=request.user)
    data = serializers.serialize('json', items)
    return HttpResponse(data)
```

### 2. Membuat fungsi untuk menambahkan data
Selanjutnya, saya membuat fungsi untuk menambahkan data pada berkas `main/views.py`. Berikut kode yang saya tambahkan:
```
...
from django.views.decorators.csrf import csrf_exempt
...
@login_required(login_url='main:login')
@csrf_exempt
def create_ajax(request):
    if request.method == 'POST':
        new_item = Item(
            name=request.POST.get('name'),
            amount=request.POST.get('amount'),
            description=request.POST.get('description'),
            price=request.POST.get('price'),
            year=request.POST.get('year'),
            genre=request.POST.get('genre'),
            duration=request.POST.get('duration'),
            rating=request.POST.get('rating'),
            image=request.FILES.get('image'),
            user=request.user
        )
        new_item.save()

        return HttpResponse('Item added', status=201)
    return HttpResponseNotFound()
```

### 3. Membuat fungsi untuk menghapus data
Selanjutnya, saya membuat fungsi untuk menghapus data pada berkas `main/views.py`. Berikut kode yang saya tambahkan:
```
...
@login_required(login_url='main:login')
@csrf_exempt
def delete_ajax(request, id):
    if request.method == 'DELETE':
        item = Item.objects.get(id=id)
        if item.user == request.user:
            item.delete()
            return HttpResponse('Item deleted', status=204)

        return HttpResponseForbidden()
    return HttpResponseNotFound()
```

### 4. Menambahkan *routing* untuk fungsi yang telah dibuat
Selanjutnya, saya menambahkan *routing* untuk fungsi yang telah dibuat pada berkas `main/urls.py`. Berikut kode yang saya tambahkan:
```
...
urlpatterns = [
    ...
    path('get-item-json/', views.get_item_json, name='get_item_json'),
    path('create-ajax/', views.create_ajax, name='create_ajax'),
    path('delete-ajax/<int:id>/', views.delete_ajax, name='delete_ajax'),
]
```

### 5. Menampilkan data JSON menggunakan AJAX
Sebelum itu, saya mengubah berkas *template* `base.html` pada berkas `templates/base.html`. Berikut kode yang saya ubah di bawah *block* `content`:
```
...
{% block script %}
{% endblock script %}
```
Selanjutnya, saya menampilkan data JSON menggunakan AJAX pada berkas *template* `index.html` pada berkas `main/templates/index.html`. Berikut kode yang saya ubah pada *block* `content`:
```
...
{% if user.is_authenticated %}
    <section id="items"></section>
{% endif %}
```
Dan berikut kode yang saya tambahkan pada *block* `script`:
```
    {% if user.is_authenticated %}
    <script>
        async function getItems() {
            return fetch("{% url 'main:get_item_json' %}")
                .then(response => response.json())
        }

        async function refreshItems() {
            document.getElementById("items").innerHTML = ""
            const items = await getItems()
            const length = Object.keys(items).length
            let html = '<div class="container">'
            html += '<p class="lead text-muted">Total Item: ' + length + '</p>'
            html += '<div class="row row-cols-3">';
            items.forEach((item) => {
                html += '<div class="col-md-6 col-lg-4 mb-5">'
                html += '<div class="card text-white" style="border-radius: 1rem; background-color: #F2BED1;">'
                html += '<img src="/media/' + item.fields.image + '" class="card-img-top" alt="Image" style="border-radius: 1rem 1rem 0 0;">'
                html += '<div class="card-body">'
                html += '<h5 class="card-title" style="color: #B0578D">' + item.fields.name + '</h5>'
                html += '<p class="card-text">' + item.fields.description + '</p>'
                html += '<p class="card-text">Amount: ' + item.fields.amount + '</p>'
                html += '<p class="card-text">Price: ' + item.fields.price + '</p>'
                html += '<p class="card-text">Year: ' + item.fields.year + '</p>'
                html += '<p class="card-text">Genre: ' + item.fields.genre + '</p>'
                html += '<p class="card-text">Duration: ' + item.fields.duration + '</p>'
                html += '<p class="card-text" style="color: #EBE76C;"><b>Rating: ' + item.fields.rating + '</b></p>'
                html += '<a href="/item/add/' + item.pk + '" class="btn btn-outline-dark mx-2">Add</a>'
                html += '<a href="/item/reduce/' + item.pk + '" class="btn btn-outline-secondary mx-2">Reduce</a>'
                html += '<a href="/item/delete/' + item.pk + '" class="btn btn-outline-danger mx-2">Delete</a>'
                html += '</div>'
                html += '</div>'
                html += '</div>'
            })
            html += '</div>'
            html += '</div>'
            document.getElementById("items").innerHTML = html
        }

        refreshItems();
        </script>
    {% endif %}
```

### 6. Menambahkan fungsi untuk menambahkan data menggunakan AJAX
Selanjutnya, saya membuat modal untuk menambahkan data menggunakan AJAX pada berkas *template* `index.html` pada berkas `main/templates/index.html`. Berikut kode yang saya tambahkan di bawah *section* `items`:
```
    <button type="button" class="btn btn-outline-dark" data-bs-toggle="modal" data-bs-target="#modalItem" style="position: fixed; bottom: 2rem; right: 2rem; border-radius: 1rem;">Add Movie</button>

    <div class="modal modal-lg fade" id="modalItem" tabindex="-1" aria-labelledby="modalItemLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content text-center text-white" style="border-radius: 1rem; background-color: #F2BED1;">
                <div class="modal-header">
                    <h5 class="modal-title" id="modalItemLabel" style="color: #B0578D;">Add Movie</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" style="color: #B0578D;"></button>
                </div>
                <div class="modal-body">
                    <form id="createItemForm" onsubmit="return false;">
                        {% csrf_token %}
                        <div class="form-outline form-white mb-4">
                            <label class="form-label" for="name">Name</label>
                        <input type="text" name="name" required id="name" class="form-control form-control-lg" />
                        </div>
        
                        <div class="form-outline form-white mb-4">
                            <label class="form-label" for="amount">Amount</label>
                        <input type="number" name="amount" required id="amount" class="form-control form-control-lg" />
                        </div>
        
                        <div class="form-outline form-white mb-4">
                            <label class="form-label" for="description">Description</label>
                        <textarea name="description" required id="description" class="form-control form-control-lg" rows="4"></textarea>
                        </div>
        
                        <div class="form-outline form-white mb-4">
                            <label class="form-label" for="price">Price</label>
                        <input type="number" name="price" required id="price" class="form-control form-control-lg" />
                        </div>
        
                        <div class="form-outline form-white mb-4">
                            <label class="form-label" for="year">Year</label>
                        <input type="number" name="year" required id="year" class="form-control form-control-lg" />
                        </div>
        
                        <div class="form-outline form-white mb-4">
                            <label class="form-label" for="genre">Genre</label>
                        <input type="text" name="genre" required id="genre" class="form-control form-control-lg" />
                        </div>
        
                        <div class="form-outline form-white mb-4">
                            <label class="form-label" for="duration">Duration</label>
                        <input type="number" name="duration" required id="duration" class="form-control form-control-lg" />
                        </div>
        
                        <div class="form-outline form-white mb-4">
                            <label class="form-label" for="rating">Rating</label>
                        <input type="number" name="rating" required id="rating" class="form-control form-control-lg" step="0.1" />
                        </div>
        
                        <div class="form-outline form-white mb-4">
                            <label class="form-label" for="image">Image</label>
                        <input type="file" name="image" accept="image/*" required id="image" class="form-control form-control-lg" />
                        </div>

                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-outline-dark" id="createItem" data-bs-dismiss="modal">Create</button>
                </div>
            </div>
        </div>
    </div>
{% endif %}
```
Dan berikut kode yang saya tambahkan pada *block* `script`:
```
...
function createItem() {
    fetch("{% url 'main:create_ajax' %}", {
        method: "POST",
        body: new FormData(document.getElementById("createItemForm"))
    }).then(() => {
        refreshItems()
    })

    document.getElementById("createItemForm").reset()
    return false
}

document.getElementById("createItem").onclick = createItem
```

### 7. Menambahkan fungsi untuk menghapus data menggunakan AJAX
Selanjutnya, saya menambahkan fungsi untuk menghapus data menggunakan AJAX pada berkas *template* `index.html` pada berkas `main/templates/index.html`. Berikut kode yang saya tambahkan pada *block* `script`:
```
function deleteItem(id) {
    fetch("{% url 'main:delete_ajax' 0 %}".replace("0", id), {
        method: "DELETE",
        body: new FormData()
    }).then(() => {
        refreshItems()
    })

    return false
}
```
Dan berikut kode yang saya ubah pada *block* `content`:
> Sebelum diubah:
```
<a href="/item/delete/{{ item.pk }}" class="btn btn-outline-danger mx-2">Delete</a>
```
> Setelah diubah:
```
'<button type="button" class="btn btn-outline-danger mx-2" onclick="deleteItem(' + item.pk + ')">Delete</button>'
```

### Melakukan perintah `collectstatic`
Sebelumnya saya mengatur `STATIC_ROOT` pada berkas `blockbuster/settings.py` menjadi sebagai berikut:
```
STATIC_ROOT = BASE_DIR / "static"
```
Lalu, saya melakukan perintah `collectstatic` pada terminal:
```
python manage.py collectstatic
```

### Melakukan *deployment* ke PaaS PBP Fasilkom UI
1. Pertama, saya menambahkan `django-environ` pada berkas `requirements.txt`.
2. Selanjutnya, saya membuat berkas `Procfile` pada direktori utama. Berikut kode yang saya tambahkan:
```
release: django-admin migrate --noinput
web: gunicorn blockbuster.wsgi
```
3. Lalu, saya membuat berkas `pbp-deploy.yml` pada direktori baru bernama `.github/workflows`. Berikut kode yang saya tambahkan:
```
name: Deploy

on:
  push:
    branches:
      - main
      - master

jobs:
  Deployment:
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
    - name: Cloning repo
      uses: actions/checkout@v4
      with:
        fetch-depth: 0

    - name: Push to Dokku server
      uses: dokku/github-action@master
      with:
        branch: 'main'
        git_remote_url: ssh://dokku@${{ secrets.DOKKU_SERVER_IP }}/${{ secrets.DOKKU_APP_NAME }}
        ssh_private_key: ${{ secrets.DOKKU_SSH_PRIVATE_KEY }}
```
4. Selanjutnya, saya membuat berkas `.dockerignore` pada direktori utama. Berikut kode yang saya tambahkan:
```
**/*.pyc
**/*.pyo
**/*.mo
**/*.db
**/*.css.map
**/*.egg-info
**/*.sql.gz
**/__pycache__/
.cache
.project
.idea
.pydevproject
.idea/workspace.xml
.DS_Store
.git/
.sass-cache
.vagrant/
dist
docs
env
logs
src/{{ project_name }}/settings/local.py
src/node_modules
web/media
web/static/CACHE
stats
Dockerfile
.gitignore
Dockerfile
db.sqlite3
**/*.md
logs/
```
5. Lalu, saya membuat berkas `Dockerfile` pada direktori utama. Berikut kode yang saya tambahkan:
```
FROM python:3.10-slim-buster

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    DJANGO_SETTINGS_MODULE=blockbuster.settings \
    PORT=8000 \
    WEB_CONCURRENCY=2

# Install system packages required Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
&& rm -rf /var/lib/apt/lists/*

RUN addgroup --system django \
    && adduser --system --ingroup django django

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Copy project code
COPY . .

RUN python manage.py collectstatic --noinput --clear

# Run as non-root user
RUN chown -R django:django /app
USER django

# Run application
# CMD gunicorn blockbuster.wsgi:application
```
6. Selanjutnya, saya membuka berkas `settings.py` pada direktori `blockbuster`. Berikut kode yang saya tambahkan:
```
...
import environ
import os
... (setelah BASE_DIR)
env = environ.Env()
... (setelah SECRET_KEY)
# Automatically determine environment by detecting if DATABASE_URL variable.
# DATABASE_URL is provided by Heroku if a database add-on is added (e.g. Heroku Postgres).
PRODUCTION = env.bool('PRODUCTION', False)
... (setelah DATABASES)
# Set database settings automatically using DATABASE_URL.
if PRODUCTION:
    DATABASES = {
        'default': env.db('DATABASE_URL')
    }
    DATABASES["default"]["ATOMIC_REQUESTS"] = True
...
```
7. Lalu, saya mengonfigurasi *environment variables* pada Github Actions. Berikut *environment variables* yang saya tambahkan:
```
DOKKU_APP_NAME: jessica-ruth-tugas
DOKKU_SERVER_IP: pbp.cs.ui.ac.id
DOKKU_SSH_PRIVATE_KEY: (private key)
```
8. Selanjutnya, saya melakukan *push* ke Github dan melakukan *deployment* ke PaaS PBP Fasilkom UI.


## Menjawab Pertanyaan-Pertanyaan
### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Perbedaan utama antara asynchronous programming dan synchronous programming adalah cara mereka menangani operasi yang memakan waktu.

Asynchronous programming memungkinkan program untuk melanjutkan eksekusi setelah memulai operasi yang memakan waktu, tanpa menunggu operasi tersebut selesai. Ini dilakukan dengan menggunakan callback, yang adalah fungsi yang dipanggil ketika operasi selesai.

Synchronous programming, di sisi lain, mengharuskan program untuk menunggu operasi yang memakan waktu selesai sebelum melanjutkan eksekusi. Ini dapat menyebabkan program terhenti atau melambat jika operasi memakan waktu lama.

### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Paradigma event-driven programming adalah paradigma pemrograman yang memisahkan antara logika aplikasi dan peristiwa yang terjadi di aplikasi. Dalam paradigma ini, logika aplikasi hanya akan dijalankan ketika terjadi peristiwa tertentu.

Dalam penerapan JavaScript dan AJAX, paradigma event-driven programming digunakan untuk merespons peristiwa yang terjadi di browser, seperti klik, scroll, dan perubahan data. Dengan menggunakan paradigma ini, aplikasi dapat merespons peristiwa secara real-time tanpa harus memuat ulang halaman.

Salah satu contoh penerapan paradigma event-driven programming dalam JavaScript dan AJAX pada tugas ini adalah ketika menambahkan data menggunakan AJAX. Ketika tombol `Create` ditekan, fungsi `createItem()` akan dijalankan. Fungsi ini akan mengirimkan data ke server menggunakan AJAX, dan kemudian memuat ulang data menggunakan fungsi `refreshItems()`.

### Jelaskan penerapan asynchronous programming pada AJAX.
AJAX adalah singkatan dari Asynchronous JavaScript and XML. AJAX adalah teknik yang memungkinkan aplikasi web untuk berkomunikasi dengan server secara asynchronous.

Penerapan asynchronous programming pada AJAX dapat meningkatkan performa dan responsivitas aplikasi web. Dengan menggunakan asynchronous programming, aplikasi web dapat melanjutkan eksekusi setelah memulai operasi yang memakan waktu, tanpa menunggu operasi tersebut selesai. Ini berarti bahwa pengguna dapat berinteraksi dengan aplikasi web saat operasi yang memakan waktu sedang berlangsung.

### Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
Fetch API dan jQuery adalah dua teknologi yang dapat digunakan untuk menerapkan AJAX. Keduanya memiliki kelebihan dan kekurangan masing-masing.

**Fetch API** adalah API JavaScript native yang dapat digunakan untuk membuat permintaan HTTP. Fetch API memiliki beberapa kelebihan, antara lain:
* **Kemudahan penggunaan:** Fetch API lebih mudah digunakan daripada XMLHttpRequest, yang merupakan API JavaScript lama untuk membuat permintaan HTTP.
* **Dukungan Promise:** Fetch API mendukung Promise, yang membuat kode lebih mudah dibaca dan dirawat.
* **Kompatibilitas browser:** Fetch API lebih kompatibel dengan browser modern.

**jQuery** adalah library JavaScript yang menyediakan berbagai fungsi untuk mempermudah pengembangan web. jQuery dapat digunakan untuk menerapkan AJAX, tetapi juga dapat digunakan untuk tugas-tugas lain, seperti manipulasi DOM dan event handling.
jQuery memiliki beberapa kelebihan, antara lain:
* **Kemudahan dipelajari dan digunakan:** jQuery lebih mudah dipelajari dan digunakan daripada Fetch API.
* **Komunitas:** jQuery memiliki komunitas yang besar dan aktif, sehingga ada banyak sumber daya yang tersedia untuk mempelajarinya dan mendapatkan bantuan.
* **Kompatibilitas browser:** jQuery mendukung berbagai browser, termasuk browser lama.

**Teknologi manakah yang lebih baik untuk digunakan?**
Teknologi mana yang lebih baik untuk digunakan menurut saya tergantung pada kebutuhan proyek. Jika membutuhkan API yang mudah digunakan dan mendukung Promise, maka Fetch API adalah pilihan yang baik. Jika membutuhkan API yang didukung oleh komunitas yang besar dan memiliki banyak sumber daya, maka jQuery adalah pilihan yang baik. Oleh karena itu, Fetch API dan jQuery adalah teknologi yang baik untuk digunakan, tergantung pada kebutuhan proyek.
