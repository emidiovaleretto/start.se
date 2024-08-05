from django.shortcuts import render


def registration(request):
    if request.method == "GET":
        return render(request, "users/registration.html")
