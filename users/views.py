from families.models import Family, FamilyInvite
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

            user = form.save()
            invite = FamilyInvite.objects.filter(guest_email=user.email).first()
            
            if invite is not None:
                # If invite exists, add member to the family host
                invite.family.members.set([user])

            else: 
                # If invite not exists, add member to a new family
                family = Family.objects.create(name="")
                family.members.set([user])

            return redirect("task-list")
    else:

        form = CreateUserForm()

    return render(request, "users/create_user.html", {"form": form})