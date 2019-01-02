from django.shortcuts import render,redirect
from Dashboard.models import Utilisateur
from django.contrib import messages

# Create your views here.
def login(request):
    return render(request,"component/login_register/login.html")

def doLogin(request):
    login = request.POST.get('login')
    password = request.POST.get('password')
    print(login)
    print(password)
    user = Utilisateur.objects.get(login=login)
    print(user)
    message = "Login ou mot de passe incorrecte"
    messages.error(request,message)
    response = render(request,"component/login_register/login.html")
    if user.password == password:
        request.session['user_id'] = user.id
        messages.info(request,"OK")
        response = redirect('dashborad:index')
    return response

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

def index (request):
    id = request.session['user_id']
    user = Utilisateur.objects.get(id=id)
    context ={
        'user':user,
    }
    return render(request,"index.html",context)
