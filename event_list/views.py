from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet

from django.views.generic import ListView, DetailView, DeleteView, detail
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.forms import BaseModelForm
from django.http import HttpResponse

from event_list.forms import CreateEventForm, UpdateEventForm
from event_list.models import Event
from event_list.facades import create_recurrent_tasks


class CreateEventView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = CreateEventForm
    template_name = 'create_event.html'
    success_url = reverse_lazy('event-list')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        event = form.save(commit=False)
        # add family to event
        event.family = self.request.user.family.first()
        # creates related tasks
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
    template_name = "list_events.html"
    paginate_by = 100

    def get_queryset(self) -> QuerySet:
        # filters events by user family
        return Event.objects.filter(
            family=self.request.user.family.first()
            )


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = datetime.now().date()
        return context


class DeleteEventView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = "delete_event.html"
    success_url = reverse_lazy('event-list')