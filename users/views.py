from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect

from users.forms import CreateUserForm, LoginForm


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'


def create_user_view(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task-list")
    else:
        form = CreateUserForm()

    return render(request, "users/create_user.html", {"form": form})