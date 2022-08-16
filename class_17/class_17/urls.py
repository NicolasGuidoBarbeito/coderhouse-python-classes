"""class_17 URL Configuration

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
from .views import greeting, introduction, now, user, year_of_birth, first_template, second_template

urlpatterns = [
    path('admin/', admin.site.urls),
    path('greeting/', greeting),
    path('introduction/', introduction),
    path('now/', now),
    path('user/<name>', user),
    path('year-of-birth/<int:age>', year_of_birth),
    path('first-template/', first_template),
    path('second-template/', second_template)
]