from django.contrib import admin
from django.urls import path

from Dashboard import views
app_name="dashborad"
urlpatterns = [
    path('login/', views.login,name='login'),
    path('register/', views.register, name='registe'),
    path('',views.index,name='index'),
    path('logout/', views.logout, name='logout'),
    path('equipements/all/', views.equipementShows, name='equipementShows'),
    path('users/all/', views.usersShows, name='userShows'),
    path('users/show/<id>', views.usersEdit, name='userEdit'),
    path('users/delete/<id>', views.deleteUser, name='userDelete'),
    path('users/profile', views.profil, name='userProfil'),
    path('equipements/detail/api/info/<id>', views.getInfo,name = 'api'),
    #path('api/info/', views.Disk_data.as_view(), name='api1'),

    path('equipements/detail/<id>', views.equipementDetail,name = 'equipementDetails'),
    path('equipements/portScan/<id>', views.scanPort, name='equipementPortScan'),
    path ('equipements/all/notification/nombre',views.getAlert,name = 'notification'),
    path ('equipements/detail/notification/nombre',views.getAlert,name = 'notification'),
    path ('notification/nombre',views.getAlert,name = 'notification'),
    path ('users/profile/notification/nombre',views.getAlert,name = 'notification'),
    path ('users/show/<id>/notification/nombre',views.getAlert,name = 'notification'),
    path ('users/all/notification/nombre',views.getAlert,name = 'notification'),
    path ('bandeTotal',views.getTotalBandswitch,name = 'bandeTotal'),
    path ('ping',views.pingEquipement,name = 'ping'),
    path ('equipements/all/ping',views.pingEquipement,name = 'ping'),
    path ('equipements/all/etat/<id>',views.getEtat,name = 'etat'),
    path ('historique',views.showsHistorique,name = 'historique'),
    path ('userNombre',views.userActifNombre,name = 'userNombre'),

]