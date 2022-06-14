from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path("login",views.login,name='login'),
     path('logout',views.logout,name='logout'),
     path('signup/',views.signup,name='signup'),
     path('course',views.course,name='course'),
     path('show',views.show,name='show'),
     path('assign',views.assign,name='assign'),
     path('video',views.video,name='video'),
     path('notes',views.notes,name='notes'),
     path('files',views.files,name='files'),
     path('', views.homes ,name='homes'),
]