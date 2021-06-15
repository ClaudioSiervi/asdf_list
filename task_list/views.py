from django.views.generic import ListView, DetailView, DeleteView
from task_list.models import Task
from task_list.forms import CreateTaskForm, UpdateTaskForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from datetime import datetime
from django.conf import settings
from django.urls import reverse_lazy
from django.shortcuts import render


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



def update_task_status_view(request):
    """ View used in task checkbox """

    is_concluded = False

    if request.GET.get('is_concluded'):
        is_concluded = True

    return render(request, 'some_template.html',{
        'is_concluded': is_concluded,
    })
