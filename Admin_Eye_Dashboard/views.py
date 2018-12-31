from django.shortcuts import render
from Admin_Eye_Dashboard import forms
def login(request):
    form = forms.LoginForm(request.POST or None)
    return render(request,"component/login_register/login.html",locals())

def register(request):
    return render(request,"component/login_register/register.html")