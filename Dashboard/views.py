from django.shortcuts import render,redirect
from Dashboard.models import *
from django.contrib import messages

# Create your views here.
def login(request):
    response = render(request,"component/login_register/login.html")
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        user = Utilisateur.objects.get(login=login)
        print(user)
        message = "Login ou mot de passe incorrecte"
        messages.error(request, message)
        response = render(request, "component/login_register/login.html")
        if user.password == password:
            request.session['user_id'] = user.id
            request.session.set_expiry(500)
            response = redirect('dashborad:index')

    return response


def register(request):
    response = render(request,"component/login_register/register.html")
    if request.method == 'POST':
        login = request.POST.get('login')
        email = request.POST.get('email')
        password = request.POST.get('password')
        Utilisateur.objects.create(
            login=login,
            email=email,
            password=password,
            role="Admin"
        )
        messages.info(request,"Enregistrement éffectué")
        response = redirect('dashborad:userShows')

    return response


def index (request):
    response = redirect('dashborad:login')
    print("browser === "+ str(request.user_agent.browser.family))
    try:
        id = request.session['user_id']
        if id:
            user = Utilisateur.objects.get(id=id)
            context = {
                'user': user,
            }
            response = render(request, "index.html", context)
    except:
        response = redirect('dashborad:login')

    return response


def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return redirect('dashborad:login')


def equipementShows(request):
    response = redirect('dashborad:login')
    print("browser === " + str(request.user_agent.browser.family))
    try:
        id = request.session['user_id']
        if id:
            user = Utilisateur.objects.get(id=id)
            equipements = Equipement.objects.all()
            context = {
                'user': user,
                'equipements':equipements
            }
            response = render(request, "equipements/shows.html", context)
    except:
        response = redirect('dashborad:login')
    return response

def usersShows (request):
    response = redirect('dashborad:login')
    print("browser === " + str(request.user_agent.browser.family))
    try:
        id = request.session['user_id']
        if id:
            user = Utilisateur.objects.get(id=id)
            utilisateurs = Utilisateur.objects.all()
            context = {
                'user': user,
                'utilisateurs': utilisateurs
            }
            response = render(request, "users/shows.html", context)
    except:
        response = redirect('dashborad:login')
    return response

def usersEdit (request,id):
    user = Utilisateur.objects.get(id=id)
    context = {
        'user':user
    }
    response = render(request, "users/edit.html",context)
    try:
        id = request.session['user_id']
        if request.method == 'POST':
            login = request.POST.get('login')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user.login = login
            user.password=password
            user.email=email
            user.save()
            messages.info(request, "Enregistrement éffectué")
            response = redirect('dashborad:userShows')
    except:
        response = redirect('dashborad:login')

    return response

def deleteUser(request,id):
    response = None
    try:
        ids = request.session['user_id']
        print(request.method)
        Utilisateur.objects.get(id=id).delete()
        messages.info(request, "Suppression éffectué")
        response = redirect('dashborad:userShows')

    except:
        response = redirect('dashborad:login')

    return response

def profil(request) :
    response = None
    try:
        ids = request.session['user_id']
        user = Utilisateur.objects.get(id=ids)
        context = {
            'user':user
        }
        messages.info(request, "Suppression éffectué")
        response = render(request,'users/profil.html',context)

    except:
        response = redirect('dashborad:login')

    return response
