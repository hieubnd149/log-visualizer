from rest_framework import generics
from django.shortcuts import render
from django.http import HttpResponse

from .models import Question
from .serializers import QuestionSerializer

def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': question_list}
    return render(request, 'logparser/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % (question_id))

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def adminPage(request):
    return render(request, 'logparser/adminpage.html', {})

def logView(request):
    context = {'anyerror': True}
    return render(request, 'logparser/logview.html', context)


class CreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        serializer.save()