"""backend URL Configuration

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

from .view import (GetNguongCanhBao, PostNguongCanhBao, UpdateNguongCanhBao,
                   DeleteNguongCanhBao, GetFactchibao, GetFactlichsugia, GetFactchibao_detail,
                   GetFactlichsugia_detail, UpdateUserView, DeleteUserView, LoginView, GetNguongCanhBao_Detail)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/account/login/", LoginView.as_view(), name="LoginAccount"),
    path(
        "api/nguongcanhbao/all/",
        GetNguongCanhBao.as_view(),
        name="GetNguongCanhBao",
    ),
    path(
        "api/nguongcanhbao/<int:matk>/",
        GetNguongCanhBao_Detail.as_view(),
        name="GetNguongCanhBaoChiTiet",
    ),
    path(
        "api/nguongcanhbao/create/",
        PostNguongCanhBao.as_view(),
        name="PostNguongCanhBao",
    ),
    path(
        "api/nguongcanhbao/update/<int:id>/",
        UpdateNguongCanhBao.as_view(),
        name="UpdateNguongCanhBao",
    ),
    path(
        "api/nguongcanhbao/delete/<int:id>/",
        DeleteNguongCanhBao.as_view(),
        name="DeleteNguongCanhBao",
    ),
    path(
        "api/chibao/all/",
        GetFactchibao.as_view(),
        name="GetFactchibao",
    ),
    path(
        "api/lichsugia/all/",
        GetFactlichsugia.as_view(),
        name="GetFactlichsugia",
    ),
    path(
        "api/chibao/<str:mack>/<str:loaichibao>/<str:ngaygiaodich>",
        GetFactchibao_detail.as_view(),
        name="GetFactchibao_detail",
    ),
    path(
        "api/lichsugia/<str:mack>/<str:ngaygiaodich>",
        GetFactlichsugia_detail.as_view(),
        name="GetFactlichsugia_detail",
    ),
    path(
        "api/account/update/<int:id>/",
        UpdateUserView.as_view(),
        name="UpdateUserView",
    ),
    path(
        "api/account/delete/<int:id>/",
        DeleteUserView.as_view(),
        name="DeleteUserView",
    ),
]
