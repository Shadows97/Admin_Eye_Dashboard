from django.contrib import admin
from django.urls import path

from Dashboard import views
app_name="dashborad"
urlpatterns = [
    path('login/', views.login,name='login'),
    path('register/', views.register, name='registe'),
    path('registrer/do',views.doRegistry,name='doRegistry')

]