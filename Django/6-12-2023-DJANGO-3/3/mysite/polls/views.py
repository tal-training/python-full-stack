from django.shortcuts import render

from django.http import HttpResponse

from .models import Question

def index(request):
    latest_question_list = Question.objects.all()
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    #  צריך להחזיר טמפלייט עם שאלה
    #  לפי ID
    return render(request, "polls/detail.html", {"question":Question.objects.get(id=question_id)})

