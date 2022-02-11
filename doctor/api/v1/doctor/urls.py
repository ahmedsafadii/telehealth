from doctor.api.v1.doctor import views
from django.urls import path

urlpatterns = [
    path('sign_up', views.SignUp.as_view()),
    path('sign_in', views.SignIn.as_view()),
    path('profile', views.Profile.as_view()),
    path('get_code', views.GetCode.as_view()),
    path('update_profile', views.UpdateProfile.as_view()),
    path('get_my_availability_slots', views.GetMyAvailableSlot.as_view()),
    path('logout', views.Logout.as_view()),
]
