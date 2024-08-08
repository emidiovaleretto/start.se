from django.shortcuts import render


def register_business(request):
    if request.method == 'GET':
        return render(request, '')