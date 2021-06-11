from django.views.generic import ListView, DetailView, DeleteView
from .models import Task
from .forms import CreateUserForm, CreateTaskForm, UpdateTaskForm
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

    return render(request, "users/create_user.html", {"form": form})


class TaskCreateView(CreateView):
    model = Task
    form_class = CreateTaskForm
    template_name = 'create_task.html'
    success_url = reverse_lazy('task-list')


class RetrieveTasklView(DetailView):
    model = Task
    template_name = 'retrieve_task.html'


class UpdateTaskView(UpdateView):
    model = Task
    form_class = UpdateTaskForm
    template_name = 'update_task.html'
    success_url = reverse_lazy('task-list')


class ListTaskView(ListView):
    model = Task
    template_name = "list_task.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = datetime.now().date()
        context["host"] = settings.HOST
        return context


class DeleteTaskView(DeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_url = reverse_lazy('task-list')