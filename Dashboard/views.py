from django.shortcuts import render,redirect
from Dashboard.models import Utilisateur
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
            request.session.set_expiry(10)
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
        response = redirect('dashborad:index')

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
