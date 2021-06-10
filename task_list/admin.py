from django.contrib import admin

from task_list.models import User, Family, Task
from event_list.models import Event

admin.site.register(User)
admin.site.register(Family) 
admin.site.register(Task) 
admin.site.register(Event) 
