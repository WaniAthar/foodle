"""foodle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.urls.conf import include
from subjects import views

urlpatterns = [
    path('/mvc',views.mvc, name='mvc'),
    path('/B_electronics', views.b_e, name='b_e'),
    path('/prof_com', views.eng, name='english'),
    path('/chemistry', views.chem, name='chemistry'),
    path('/bme', views.bme, name='bme'),
    path('/ds', views.ds, name='ds'),

]
