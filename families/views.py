from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.shortcuts import redirect
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from families.forms import CreateFamilyForm
from families.models import Family


class CreateFamilytView(LoginRequiredMixin, CreateView):
    model = Family
    form_class = CreateFamilyForm
    template_name = 'families/create_family.html'
    success_url = reverse_lazy('task-list')


class ListFamilyView(LoginRequiredMixin, ListView):
    template_name = "families/list_family.html"
    paginate_by = 10

    def get_queryset(self) -> QuerySet:
        # filters events by user family
        return Family.objects.filter(
            id=self.request.user.family.first().id
            )