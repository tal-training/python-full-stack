from django.shortcuts import render

from django.http import HttpResponse

from .models import Course

def students(request):
    python_course=Course.objects.get(name="python")
    students_in_python=python_course.student_set.all()
    return HttpResponse(", ".join([s.name for s in students_in_python]))

def grades(request):
    return HttpResponse(dict(zip(["tal", "gal", "shoval"],[80,90,100])).items())

def courses(request):
    return HttpResponse(", ".join([c.name for c in Course.objects.all()]))
