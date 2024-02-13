from django.shortcuts import render, redirect

import contacts.functions as functions
from .models import Contact
from .forms import ContactModelForm, AdminModelForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import django.contrib.auth

@login_required(login_url="/login")
def home(request):
    return render(request, "index.html", {
        "contacts":Contact.objects.all(),
        "form":ContactModelForm(),
        "message":f"welcome"
    })

def admin(request):
    return render(request, "admin.html", {
        "form":AdminModelForm()
    })


def add(request):
    ContactModelForm(request.GET).save()
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
    
def add_user(request):
    try:
        AdminModelForm(request.POST).save()
        message="User added OK"
    except:
        message="problem adding user"
    return render(request, "admin.html", {
        "form":AdminModelForm(),
        "message":message
    })

def login(request):
    if request.method=='GET':
        return render(request=request, template_name="login.html", context={
            "form":AdminModelForm()
        })
    user_dict={t[0]:t[1] for t in list(request.POST.items())}
    user=authenticate(request, **user_dict)
    if user:
        django.contrib.auth.login(request, user)
        return redirect('home')
    return redirect('login')