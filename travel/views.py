from django.shortcuts import render


def home(request):
    name = 'Luke'
    return render(request, 'home.html', {'name': name})
