from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout


def registration(request):
    if request.method == "GET":
        return render(request, "users/registration.html")
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_enter_password = request.POST.get('re-enter-password')

        if username == '' or password == '' or re_enter_password == '':
            messages.add_message(
                request,
                constants.ERROR,
                'Required fields must be filled in.'
            )

        if not password == re_enter_password:
            messages.add_message(
                request,
                constants.ERROR,
                "Please make sure you passwords match."
            )
            return redirect(reverse('registration'))

        if len(password) < 6:
            messages.add_message(
                request,
                constants.ERROR,
                "Password must be at least 6 characters long."
            )
            return redirect(reverse('registration'))

        users = User.objects.filter(username=username)

        if users.exists():
            messages.add_message(
                request,
                constants.ERROR,
                "A user with that username already exists."
            )
            return redirect(reverse('registration'))

        user = User.objects.create_user(
            username=username,
            password=password
        )
        
        messages.add_message(
            request,
            constants.SUCCESS,
            "Registration completed successfully!"
        )
        return redirect(reverse('signin'))


def signin(request):
    if request.method == "GET":
        return render(request, "users/signin.html")

    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        is_user_authenticated = authenticate(
            request, 
            username=username, 
            password=password
        )

        if is_user_authenticated:
            login(request, is_user_authenticated)
            return redirect(reverse('list_businesses'))

    messages.add_message(
        request,
        constants.ERROR,
        'Incorrect username or password.'
    )

    return redirect(reverse('signin'))


def signout(request):
    logout(request)

    messages.add_message(
            request,
            constants.SUCCESS,
            'You have been successfully logged out.'
        )
    return redirect(reverse('signin'))
