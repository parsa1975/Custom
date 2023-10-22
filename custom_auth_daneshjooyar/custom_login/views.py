from django.shortcuts import render
from .models import MyUser
from django.contrib.auth import login
from django.urls import reverse
from django.http import HttpResponseRedirect


def mobile_login(request):
    if request.method == "POST":
        if "mobile" in request.POST:
            mobile = request.POST.get('mobile')
            user = MyUser.objects.get(mobile=mobile)
            login(request,user=user)
            return HttpResponseRedirect(reverse('dashboard'))
        
    return render(request,'mobile_login.html')


def dashboard(request):
    return render(request,'dashboard.html')
