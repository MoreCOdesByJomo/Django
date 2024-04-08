from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader #for routing your templates
"""def registration(request):
    return HttpResponse("Welcome to Registration")"""
def login(request):
    template=loader.get_template('hospital_login.html')
    return HttpResponse(template.render())
