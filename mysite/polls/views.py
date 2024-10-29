from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Question
from django.http import Http404

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, "polls/detail.html", {"question": question})
    return HttpResponse("helllllooooooo")

def results(request, question_id):
    return HttpResponse("You're looking at the response for quesion%s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting for question %s." % question_id)




# Create your views here.
