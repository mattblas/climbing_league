"""mysite URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from climbing_ligue.views import (
    home,
    add_route_view,
    test,
    user_home,
    add_user_route_view,
    update_edition_view,
    add_new_edition_view,
    update_round_view,
    sign_up_new_edition_view,
    )

from members.views import(
    registration_view,
    logout_view,
    login_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('add_route/', add_route_view, name='add_route'),
    path('test/', test, name='test'),
    path('user_home/', user_home, name='user_home'),
    path('add_user_route/', add_user_route_view, name='add_user_route'),
    path('update_edition/', update_edition_view, name='update_edition'),
    path('update_round/', update_round_view, name='update_round'),
    path('add_new_edition/', add_new_edition_view, name='add_new_edition'),
    path('sign_up_new_edition/', sign_up_new_edition_view, name='sign_up_new_edition'),
]
urlpatterns += staticfiles_urlpatterns()