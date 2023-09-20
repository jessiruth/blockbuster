from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
from django.http import HttpResponse
from django.core import serializers

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
            return redirect('main:index')
    else:
        form = ItemForm()
    return render(request, 'form.html', {'form': form})

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
