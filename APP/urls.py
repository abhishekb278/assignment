from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('signup/',views.sign,name='sign'),
    path('login/',views.login_,name='login'),
    path('show_data/<int:upk>/',views.show_data.as_view(),name='show_data'),
]