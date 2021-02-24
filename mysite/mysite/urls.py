"""mysite URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from trips.views import hello_world
from trips.views import home
from trips.views import post_detail
import re

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello_world),
    url(r'^$', home),
    url(r'^post/(?P<pk>\d+)/$', post_detail, name='post_detail'),
]
