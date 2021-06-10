from django.views.generic import ListView, DetailView, DeleteView
from .models import Task
from .forms import CreateUserForm, CreateTaskForm, DetailTaskForm, UpdateTaskForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from datetime import datetime
from django.conf import settings
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


def create_user_view(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task-list")
    else:
        form = CreateUserForm()

    return render(request, "task_list/users/create_user.html", {"form": form})


class TaskCreateView(CreateView):
    model = Task
    form_class = CreateTaskForm
    template_name = 'task_list/task_create.html'
    success_url = reverse_lazy('task-list')


class TaskDetailView(DetailView):
    model = Task

class TaskUpdatelView(UpdateView):
    model = Task
    form_class = UpdateTaskForm
    template_name = 'task_list/task_update.html'
    success_url = reverse_lazy('task-list')


class TaskListView(ListView):
    model = Task
    template_name = "task_list/task_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = datetime.now().date()
        context["host"] = settings.HOST
        return context


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')