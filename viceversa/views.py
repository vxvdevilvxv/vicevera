from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import response

def home(request):
   return render(request, 'home.html')
  