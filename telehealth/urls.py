"""telehealth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from doctor.api.v1.doctor import urls as doctor
from setting.api.v1.setting import urls as setting
from booking.api.v1.booking import urls as booking

import environ

env = environ.Env()
environ.Env.read_env()

urlpatterns = i18n_patterns(
    path(env('SECRET_ADMIN_URL') + '/dashboard/', admin.site.urls),
)

# API shall be in domain api.xxx
urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),
    path('api/v1/doctor/', include(doctor.urlpatterns)),
    path('api/v1/setting/', include(setting.urlpatterns)),
    path('api/v1/booking/', include(booking.urlpatterns)),
]

if env('DEBUG'):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
