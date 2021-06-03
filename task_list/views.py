from django.views.generic import ListView
from .models import Task
from datetime import datetime
from django.conf import settings

class TaskListView(ListView):
    model = Task
    template_name = 'task_list/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.now().date()
        context["host"] = settings.HOST
        return context