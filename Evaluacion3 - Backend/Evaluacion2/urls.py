"""Evaluacion2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PokeTCG import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    

    #urls cards#
    path('', views.card_list , name='card_list'),
    path('cards/<int:pk>/', views.card_detail, name='card_detail'),
    path('cards/new/', views.card_add, name='card_add'),
    path('cards/<int:pk>/edit/', views.card_edit, name='card_edit'),
    path('cards/<int:pk>/delete/', views.card_delete, name='card_delete'),

]
