from django.views.generic import ListView
from .models import User

class TaskListView(ListView):
    model = User
    template_name = 'task_list/task_list.html'