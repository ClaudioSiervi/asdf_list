from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, DeleteView, detail
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.forms import BaseModelForm
from django.http import HttpResponse

from event_list.forms import CreateEventForm, UpdateEventForm
from event_list.models import Event
from event_list.facades import create_recurrent_tasks


class CreateEventView(CreateView):
    model = Event
    form_class = CreateEventForm
    template_name = 'create_event.html'
    success_url = reverse_lazy('event-list')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        if form.is_valid():
            if form.data["start"] and form.data["finish"]:
                create_recurrent_tasks()

        return super().form_valid(form)


class RetrieveEventView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = "retrieve_event.html"


class UpdateEventlView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = UpdateEventForm
    template_name = 'update_event.html'
    success_url = reverse_lazy('event-list')


class ListEventView(LoginRequiredMixin, ListView):
    model = Event
    template_name = "list_events.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = datetime.now().date()
        return context


class DeleteEventView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = "delete_event.html"
    success_url = reverse_lazy('event-list')