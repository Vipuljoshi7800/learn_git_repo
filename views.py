from django.http import Http404
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Choice,Question
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import requests
from rest_framework.views import APIView
# Create your views here.
def function(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = '******'.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def getting_id(request,id):
    return HttpResponse(id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context={
        'latest_question_list':latest_question_list
    }
    return render(request,'index.html',{'context':context})

def page_not_found(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("QUESTION DOES NOT EXIST")
        # pass
    return render(request,'detail.html',{'question':question})

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'detail.html', {'question': question})


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail.html', {'question': question})

@api_view(['GET','POST'])
def example(request):
    print("user is  :",request.user)
    print("admin is  :",request.auth)
    if request.method == 'GET':
        print(request.method)
        return Response(data={'message':'hello from Django'},status=status.HTTP_200_OK)
    elif request.method=='POST':
        print("============")
        print(request.data)
        return Response(data=request.data,status=status.HTTP_200_OK)
    else: 
        return Response(data = "Resquest method is not right")


@api_view(['POST'])
def hello_world(request):
    return Response({"this is message using rest framework"})

class Message(APIView):
    def get(self,request):
        print("hit by api call")
        return Response(data = "this is class base views GET()",status=status.HTTP_200_OK)
    
    def post(self,request):
        print("this is posst method")
        return Response(data="this is class base views POST()",status=status.HTTP_200_OK)
    
    def put(self,request):
        print("this is put method")
        return Response(data="this is class base views Put()",status=status.HTTP_200_OK)
    
    def delete(self,request):
        print("this is delete method")
        return Response(data="this is class base views Delete()",status=status.HTTP_200_OK)
    
    def patch(self,request):
        print("this is patch method")
        return Response(data="this is class base views patch()",status=status.HTTP_200_OK)
    

    def update(self,request):
        print("this is update method")
        return Response(data="this is class base views update()",status=status.HTTP_200_OK)
    
    
