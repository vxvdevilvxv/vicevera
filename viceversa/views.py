from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import response

def home(request):
   return render(request, 'home.html')

def reverse(request):
    user_text = request.GET['usertext']
    reversed_text =  user_text[::-1]
    num_of_words = len(user_text.split())
    return render(request, 'reverse.html', {'usertext':user_text, 'num_of_words': num_of_words, 'reversedtext': reversed_text})
  