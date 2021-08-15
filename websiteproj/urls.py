from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home1'),
    path('home', views.home, name='home2'),
    path('login', views.passwebsite, name='lgin'),
    path('register', views.registeruser, name='rgstr'),
    path('login/getin', views.verifier, name='getinlog'),
    path('login/home', views.logout),
    path('login/changepass1', views.changepass1),
    path('login/changepass2', views.changepass2),
    path('register/getin', views.usercollector, name='getinreg'),
]



