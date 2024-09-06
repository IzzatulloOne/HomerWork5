from django.shortcuts import render, get_object_or_404
from .models import Avto

def home(request):
    cars = Avto.objects.all()
    return render(request, 'home.html', {'cars': cars})

def about(request):
    return render(request, 'about.html')

def car_detail(request, pk):
    car = get_object_or_404(Avto, pk=pk)
    return render(request, 'car_detail.html', {'car': car})
