from django.shortcuts import render
import random
from .models import Car

def home(request):
    return render(request=request, template_name="cars/index.html", context={"cars":Car.objects.all()})

def add(request):
    Car.objects.create(name=f"car{random.randint(1,100)}", color=random.choice(["red", "green", "yellow"]), price=random.randint(60000, 120000), image_url=f'https://picsum.photos/id/{random.randint(1,250)}/200/300')
    return home(request)