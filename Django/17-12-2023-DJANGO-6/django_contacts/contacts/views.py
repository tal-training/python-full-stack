from django.shortcuts import render, redirect

import contacts.functions as functions
from .models import Contact

def home(request):
    return render(request, "index.html", {"contacts":Contact.objects.all()})

def add(request):
    name=request.GET["name"]
    phone=request.GET["phone"]
    functions.add(name, phone)
    return redirect('home')

def view(request):
    return str(functions.view())

def delete(request):
    name=request.GET["name"]
    functions.delete(name)
    return redirect('home')

def update(request):
    if request.method=='POST':
        name=request.POST["name"]
        phone=request.POST["phone"]
        functions.update(name=name, phone=phone)
        return redirect('home')
    else:
        return render(template_name="update.html", context={"name":request.GET["name"], "phone":request.GET["phone"]})