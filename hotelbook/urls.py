"""hotelbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url,include
from hotelbooking.views import index,quiz,main,advance,quiz_adv
urlpatterns = [
    # url(r'^hotelbooking/',include('hotelbooking.urls')),
    url('index/',index, name='index'),
    url('quiz/',quiz, name='quiz'),
    url('quiz_adv/',quiz_adv, name='quiz_adv'),
    url('main/',main, name='main'),
    url('advance/',advance, name='advance'),
    # url(r'^$',views.Hello, name='Hello'),
    path('admin/', admin.site.urls),
    url('',index, name='index'),
]

