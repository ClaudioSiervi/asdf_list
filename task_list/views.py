from django.views.generic import CreateView, ListView
from .models import Task, User
from .forms import CreateUserForm
from datetime import datetime
from django.conf import settings
from django.shortcuts import redirect, render


class TaskListView(ListView):
    model = Task
    template_name = "task_list/task_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = datetime.now().date()
        context["host"] = settings.HOST
        return context
    
# class CreateUserListView(CreateView):
#     model = User
#     form_class = CreateUserForm
#     template_name = "task_list/users/create.html"

def create_user_view(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CreateUserForm()
        
    return render(request, "task_list/users/create.html", {"form": form})