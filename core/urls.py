"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth.views import LogoutView
from django.urls import include, path

from blog.views import LoginUser, UserCreateView
from core import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = [
    path("", RedirectView.as_view(pattern_name="blog:posts"), name="index_redirect"),
    path("admin/", admin.site.urls),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("blog/", include("blog.urls")),
    path(
        "login/",
        LoginUser.as_view(template_name="registration/login.html"),
        name="login",
    ),
]

if settings.DEBUG:
    urlpatterns += (
        [
            path("__debug__/", include("debug_toolbar.urls")),
        ]
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
