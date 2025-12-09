from django.urls import path
from . import views

app_name = "auths"

urlpatterns = [
    path("register/", views.signin_view, name="signin" ),
    path("login/", views.login_view, name="login" ),
    path("logout/", views.logout_view, name="logout" ),
    path("activate_account/uidb64/<uidb64>/token/<token>", views.verify_account, name="activate_acount" ),
]
 