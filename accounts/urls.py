from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/',views.login_user , name="login"),
    path('accounts/register/',views.register,name="register"),
    path("logout/",views.logout_user,name="logout"),
]
