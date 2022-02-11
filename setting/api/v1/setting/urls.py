from setting.api.v1.setting import views
from django.urls import path

urlpatterns = [
    path('tools', views.Tools.as_view()),
]
