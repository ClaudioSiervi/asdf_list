from datetime import datetime

from django.conf import settings
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from task_list.models import Task
from task_list.forms import CreateTaskForm, UpdateTaskForm


class CreateTaskView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = CreateTaskForm
    template_name = 'create_task.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        task = form.save(commit=False)
        # add family to task
        task.family = self.request.user.family.first()
        return super().form_valid(form)

class RetrieveTasklView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'retrieve_task.html'


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = UpdateTaskForm
    template_name = 'update_task.html'
    success_url = reverse_lazy('task-list')


class ListTaskView(LoginRequiredMixin, ListView):
    template_name = "list_task.html"
    paginate_by = 100

    def get_queryset(self) -> QuerySet:
        # filters tasks by user family
        return Task.objects.filter(family=self.request.user.family.first())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = datetime.now().date()
        context["host"] = settings.HOST
        return context


class DeleteTaskView(LoginRequiredMixin, DeleteView):
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
