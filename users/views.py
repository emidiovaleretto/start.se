from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.messages import constants


def registration(request):
    if request.method == "GET":
        return render(request, "users/registration.html")
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_enter_password = request.POST.get('re-enter-password')

        users = User.objects.filter(username=username)

        if not password == re_enter_password or len(password) < 6 or users.exists():
            messages.add_message(
                request,
                constants.ERROR,
                "Error!"
            )
            return redirect(reverse('registration'))

        user = User.objects.create_user(
            username=username,
            password=password
        )
        
        messages.add_message(
            request,
            constants.SUCCESS,
            "Sucess!"
        )
        return redirect(reverse('signin'))


def signin(request):
    return render(request, "users/signin.html")
