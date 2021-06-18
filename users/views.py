from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect

from users.forms import CreateUserForm, LoginForm


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'


class LogoutView(auth_views.LogoutView):
    template_name = 'registration/logged_out.html'


def create_user_view(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task-list")
    else:
        form = CreateUserForm()

    return render(request, "create_user.html", {"form": form})