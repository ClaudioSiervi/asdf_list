from django.views.generic import ListView, DetailView, DeleteView, detail
from .models import Event
from event_list.forms import CreateEventForm, UpdateEventForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from datetime import datetime
from django.urls import reverse_lazy


class CreateEventView(CreateView):
    model = Event
    form_class = CreateEventForm
    template_name = 'create_event.html'
    success_url = reverse_lazy('event-list')


class RetrieveEventView(DetailView):
    model = Event
    template_name = "retrieve_event.html"


class UpdateEventlView(UpdateView):
    model = Event
    form_class = UpdateEventForm
    template_name = 'update_event.html'
    success_url = reverse_lazy('event-list')


class ListEventView(ListView):
    model = Event
    template_name = "list_events.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = datetime.now().date()
        return context


class DeleteEventView(DeleteView):
    model = Event
    template_name = "delete_event.html"
    success_url = reverse_lazy('event-list')