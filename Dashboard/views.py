from django.shortcuts import render,redirect
from Dashboard.models import Utilisateur

# Create your views here.
def login(request):
    return render(request,"component/login_register/login.html")

def register(request):
    return render(request,"component/login_register/register.html")

def doRegistry (request):
    login = request.POST.get('login')
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = Utilisateur.objects.create(
        login=login,
        email=email,
        password=password,
        role="Admin"
    )
    return redirect('dashborad:login')

