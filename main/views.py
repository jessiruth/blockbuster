from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "name": "Jessica Ruth Damai Yanti Manurung",
        "npm": "2206082783",
        "class": "PBP C",
    }
    return render(request, 'index.html', context)