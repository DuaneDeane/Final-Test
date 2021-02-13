"""Final URL Configuration

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
# from django.conf.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import path

from accounts import views as accounts_views


urlpatterns = [
    path(r'', accounts_views.home, name='home'),
    path(r'login/', accounts_views.login_page, {'template_name': 'login.html'}, name='login'),
    path(r'logout/', accounts_views.logout_page, {'next_page': 'login'}, name='logout'),
    path(r'signup/', accounts_views.signup, name='signup'),
]