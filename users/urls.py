from django.urls import path

from users.views import  create_user_view, LoginView, LogoutView


urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("create/", create_user_view, name="user-create"),

]
