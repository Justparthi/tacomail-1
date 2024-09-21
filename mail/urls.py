from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="panda"),
    path('dashboard/', views.dashboard, name="panda about"),
    path('login/', views.login, name="panda login"),
    path('signup/', views.signup, name="panda signup")
]
