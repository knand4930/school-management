from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
# from main import EmailBackEnd
from main.EmailBackEnd import EmailBackEnd


def home(request):
    return render(request, 'index.html')


def ShowLoginPage(request):
    return render(request, 'login.html')


def doLogin(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get("email"),
                                         password=request.POST.get("password"))  # EmailBackEnd.
        if user != None:
            login(request, user)
            return HttpResponse("Email: " + request.POST.get("email") + "password : " + request.POST.get("password"))

        else:
            messages.error(request, "Invailed Login Details")
            return HttpResponseRedirect("/")


def GetUserDetails(request):
    if request.user != None:
        return HttpResponse("user: " + request.user.email + " usertype: " + request.user.user_type)
    else:
        return HttpResponse("please Login First")


def Logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
