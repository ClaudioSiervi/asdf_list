from django.urls import path

from users.views import  create_user_view, LoginView


urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("users/", create_user_view, name="user-create"),

]
