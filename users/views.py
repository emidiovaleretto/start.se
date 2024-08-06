from django.urls import reverse
from django.shortcuts import render, redirect


def registration(request):
    if request.method == "GET":
        return render(request, "users/registration.html")
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_enter_password = request.POST.get('re-enter-password')

        users = Users.objects.filter(username=username)

        if not password == re_enter_password or len(password) < 6 or users.exists():
            return redirect(reverse('users:registration'))

        user = User.object.create_user(
            username=username,
            password=password
        )

        return redirect(reverse('users:signin'))


def signin(request):
    ...
