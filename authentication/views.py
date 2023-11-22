from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user:
            if user.is_active:
                auth_login(request, user)
                return JsonResponse({
                    "username": user.username,
                    "status": True,
                    "message": "Login successful! Welcome " + user.username + "!"
                }, status=200)
            else:
                return JsonResponse({
                    "status": False,
                    "message": "Account disabled. Please contact the administrator."
                }, status=401)
        else:
            return JsonResponse({
                "status": False,
                "message": "Invalid login details. Please try again."
            }, status=401)
    else:
        return JsonResponse({
            "status": False,
            "message": "Invalid request"
        }, status=400)


@csrf_exempt
def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return JsonResponse({
            "status": True,
            "message": "Logout successful! See you soon!"
        }, status=200)
    else:
        return JsonResponse({
            "status": False,
            "message": "Invalid request"
        }, status=400)


@csrf_exempt
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        if password != password2:
            return JsonResponse({
                "status": False,
                "message": "Passwords do not match!"
            }, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({
                "status": False,
                "message": "Username already exists!"
            }, status=400)
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return JsonResponse({
            "status": True,
            "message": "Successfully registered as " + username
        }, status=200)
    else:
        return JsonResponse({
            "status": False,
            "message": "Invalid request"
        }, status=400)