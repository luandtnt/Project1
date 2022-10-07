from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Question
# Create your views here.

def index(request):
    myname='luan'
    taisan=['ip','lap','pc']
    context={'name':myname,'taisan':taisan}
    return render(request, "polls/index.html",context)

def base(request):
    return render(request, "polls/base.html")

def viewquestion(request):
    list_question= Question.objects.all()
    context={'list_questionn' : list_question}
    return render(request , "polls/index.html",context)

def detailview(request,id):
    q = Question.objects.get(pk=id)
    return render(request, "polls/detail_question.html", {'qs':q})