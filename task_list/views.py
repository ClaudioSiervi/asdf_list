from django.views.generic import ListView, DetailView
from .models import Task
from .forms import CreateUserForm, CreateTaskForm, DetailTaskForm
from datetime import datetime
from django.conf import settings
from django.shortcuts import render, redirect


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

    return render(request, "task_list/users/create_user.html", {"form": form})


class TaskDetailView(DetailView):
    model = Task
    form_class = DetailTaskForm
    template_name = 'task_list/task_detail.html'


def create_task_view(request):
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CreateTaskForm()
    return render(request, "task_list/task_create.html", {"form": form})

# TODO terminar
def detail_task_view(request, pk):
    ...
#     if request.method == "POST":
#         form = DetailTaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("home")
#     else:
#         form = DetailTaskForm()
#     return render(request, "task_list/task_detail.html", {"form": form})