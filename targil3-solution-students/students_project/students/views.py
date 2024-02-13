from django.shortcuts import render

from django.http import HttpResponse

from .models import Course, Student

def home(request, message=""):
    return render(request, "students/home.html",{"students":Student.objects.all(), 
                                                 "courses":Course.objects.all(),
                                                 "message":message})

def students(request):
    python_course=Course.objects.get(name="python")
    students_in_python=python_course.student_set.all()
    return HttpResponse(", ".join([s.name for s in students_in_python]))

def grades(request):
    return HttpResponse(dict(zip(["tal", "gal", "shoval"],[80,90,100])).items())

def courses(request):
    return HttpResponse(", ".join([c.name for c in Course.objects.all()]))

def students_in_course(request, course_name):
    return HttpResponse(Student.objects.filter(course=Course.objects.get(name=course_name)))

def get_name_by_id(request, student_id):
    return HttpResponse(Student.objects.get(id=student_id).name)    

def get_course_by_student_id(request, student_id):
    student=Student.objects.get(id=student_id)
    return HttpResponse(student.course.name)    

def get_course_by_student_name(request, student_name):
    student=Student.objects.get(name=student_name)
    return HttpResponse(student.course.name)    

def add_student(request, student_name):
    s=Student(name=student_name)
    s.save()
    return home(request, message=f"Student {student_name} was added with id {s.id}")