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
        self.assertEqual(ponyo.image.url, '/media/images/Ponyo_(2008).png')
        ponyo.image.delete()
        