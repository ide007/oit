from django.shortcuts import render
from .models import Category, Location, Model


def main(request):
    return render(request, 'mainapp/index.html')


def contact(request):
    return render(request, 'mainapp/contact.html')


def model(request):
    models = Model.objects.all()
    context = {
        'models': models
    }
    return render(request, 'mainapp/index.html', context)