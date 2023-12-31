from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        items = Item.objects.filter(user=request.user)
    else:
        items = []
    context = {
        "items": items,
        "user": request.user if request.user.is_authenticated else "",
    }
    response = render(request, 'index.html', context)
    if request.COOKIES.get('last_login'):
        response.set_cookie('last_login', request.COOKIES.get('last_login'))
    return response

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

def logout_user(request):
    logout(request)
    response = redirect('main:index')
    response.delete_cookie('last_login')
    return response

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

@login_required(login_url='main:login')
def get_item_json(request):
    items = Item.objects.filter(user=request.user)
    data = serializers.serialize('json', items)
    return HttpResponse(data)

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

@login_required(login_url='main:login')
@csrf_exempt
def create_flutter(request):
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

        return JsonResponse({'status': True}, status=201)
    return HttpResponseNotFound()