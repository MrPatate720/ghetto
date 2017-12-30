'''
Created on 28 dec. 2017

@author: martins
'''

from django.http import HttpResponse
from django.shortcuts import render_to_response

def welcome(request):
    return render_to_response('welcome.html')

def login(request):
    return render_to_response('login.html')

