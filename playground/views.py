from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# takes request -> return reponse


def say_hi(request):
    return render(request, "hi.html", {'name': 'Adrien'})
