from django.http import JsonResponse
from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView

from Dashboard.models import *
from django.contrib import messages
from Dashboard.serializer import *
from Dashboard.utils import *

# Create your views here.
def login(request):
    response = render(request,"component/login_register/login.html")
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        user = Utilisateur.objects.get(login=login)
        print(user.password)
        message = "Login ou mot de passe incorrecte"
        if user.password == password:
            request.session['user_id'] = user.id
            request.session.set_expiry(3600)
            response = redirect('dashborad:index')
        else:
            messages.error(request, message)
            response = render(request, "component/login_register/login.html")

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
        print("id "+str(id))
        if id:
            user = Utilisateur.objects.get(id=id)
            alerts = Alert.objects.filter(status=False)
            context = {
                'user': user,
                'notif':alerts,
            }
            response = render(request, "index.html", context)
    except KeyError:
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
        if id != None:
            print(1)
            user = Utilisateur.objects.get(id=id)
            equipements = Equipement.objects.all()
            alerts = Alert.objects.filter(status=False)
            context = {
                'user': user,
                'equipements':equipements,
                'notif':alerts,
            }
            response = render(request, "equipements/shows.html", context)
    except KeyError:
        print(2)
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
            alerts = Alert.objects.filter(status=False)
            context = {
                'user': user,
                'utilisateurs': utilisateurs,
                'notif':alerts,
            }
            response = render(request, "users/shows.html", context)
    except KeyError:
        response = redirect('dashborad:login')
    return response

def usersEdit (request,id):
    user = Utilisateur.objects.get(id=id)
    alerts = Alert.objects.filter(status=False)
    context = {
        'user':user,
        'notif':alerts,
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
    except KeyError:
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

    except KeyError:
        response = redirect('dashborad:login')

    return response

def profil(request) :
    response = None
    try:
        ids = request.session['user_id']
        user = Utilisateur.objects.get(id=ids)
        alerts = Alert.objects.filter(status=False)
        context = {
            'user':user,
            'notif':alerts,
        }
        messages.info(request, "Suppression éffectué")
        response = render(request,'users/profil.html',context)

    except KeyError:
        response = redirect('dashborad:login')

    return response
# graph info

def disk_data(request):
    data = Disk_info.objects.all()
    serialize = Disk_Info_Serializer(data,Many=False)
    return JsonResponse(serialize.data,safe=False)

def getInfo(request,id):
    disk = Disk_info.objects.filter(equipement_id=id).last()
    cpu = Cpu_info.objects.filter(equipement_id=id).last()
    ram = Ram_info.objects.filter(equipement_id=id).last()
    byte = Interface_data_info.objects.filter(equipement_id=id).last()
    disk_labels = ["total", "used", "free"]
    cpu_lables = ["current", "min", "max"]
    byte_label = ["send"]
    cpu_infos = cpu.cpu_current_freq
    info = [convert1(disk.total_size), convert1(disk.size_used), convert1(disk.size_free)]
    ram_info = [convert1(ram.ram_total), convert1(ram.ram_used), convert1(ram.ram_free)]
    byte_info1 = [convert2(byte.byte_send), convert2(byte.byte_recv)]
    byte_info2 = [convert2(byte.byte_recv), 5]
    data = {
        'label': disk_labels,
        'default': info,
        'cpuLabel': cpu_lables,
        'cpuInfo': cpu_infos,
        'ramInfo': ram_info,
        'byteLabel': byte_label,
        'byteInfo1': byte_info1,
        'byteInfo2': byte_info2
    }
    return JsonResponse(data)

def getAlert(request):
    alerts = Alert.objects.filter(status=False)
    nmbre = alerts.count()
    print(nmbre)
    alertsData = {
        'nombre':nmbre,

    }
    return JsonResponse(alertsData)

def equipementDetail(request,id) :
    response = None
    try:
        ids = request.session['user_id']
        equipement = Equipement.objects.get(id=id)
        user = Utilisateur.objects.get(id=ids)
        alerts = Alert.objects.filter(status=False)
        context = {
            'equipement':equipement,
            'user': user,
            'notif':alerts,
        }
        response = render(request,'equipements/details.html',context)

    except KeyError:
        response = redirect('dashborad:login')

    return response

def scanPort(request,id):
    response = None
    test =[]
    try:
        ids = request.session['user_id']
        user = Utilisateur.objects.get(id=ids)
        equipement = Equipement.objects.get(id=id)
        resultat = portScan(equipement.adresse_ip)
        alerts = Alert.objects.filter(status=False)
        for resultats in resultat:
            test.append(resultat[resultats])
        context = {
            'equipement': equipement,
            'resultats':test,
            'user': user,
            'notif':alerts,
        }
        response = render(request, 'equipements/portScan.html', context)

    except KeyError:
        response = redirect('dashborad:login')

    return response



