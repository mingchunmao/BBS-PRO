from django.contrib.auth import authenticate, login,logout
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth

def acc_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:        
        login(request, user)
        return HttpResponseRedirect('/')
         
    else:
        return HttpResponseRedirect('login.html')



def Logout(request):
    user = request['user']
    logout(request)
    return HttpResponseRedirect('/')

def Login(request):
    return render_to_response('login.html')