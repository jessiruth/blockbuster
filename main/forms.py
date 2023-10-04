from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'amount', 'description', 'price', 'year', 'genre', 'duration', 'rating', 'image', 'user']