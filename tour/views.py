from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def russian(request):
    return render(request, 'index_ru.html')


def uzbek(request):
    return render(request, 'index_uz.html')
