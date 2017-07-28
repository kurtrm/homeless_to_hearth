"""View page for our homeless to hearth app."""
from __future__ import unicode_literals
from django.core.files.storage import default_storage
from django.db.models.fields.files import FieldFile
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import render
import operator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from searchlist.models import Resource
from taggit.models import Tag
from django.contrib import messages


class CreateResource(LoginRequiredMixin, CreateView):
    """Class-based view to create new resources."""

    template_name = 'searchlist/resource_form.html'
    model = Resource
    fields = ['main_category', 'org_name',
              'description', 'street', 'city', 'state', 'zip_code', 'website',
              'phone_number', 'image', 'tags']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """Save form if valid."""
        self.object = form.save(commit=False)
        self.object.save()
        return super(CreateResource, self).form_valid(form)


class EditResource(LoginRequiredMixin, UpdateView):
    """Class-based view to edit resources."""

    template_name = 'searchlist/resource_form.html'
    model = Resource
    fields = ['main_category', 'org_name',
              'description', 'street', 'city', 'state', 'zip_code', 'website',
              'phone_number', 'image', 'tags']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """Save form if valid."""
        self.object = form.save(commit=False)
        self.object.save()
        return super(EditResource, self).form_valid(form)

    def get_context_data(self, **kwargs):
        """."""
        context = super(EditResource, self).get_context_data(**kwargs)
        context["edit"] = True
        return context


class DeleteResource(LoginRequiredMixin, DeleteView):
    """Class-based view for deleting resources."""

    template_name = 'searchlist/delete_resource.html'
    success_message = "Resource was deleted successfully."
    model = Resource
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteResource, self).delete(request, *args, **kwargs)


class HomePageView(ListView):
    """Class home page view."""

    template_name = "searchlist/home.html"
    model = Resource

    def get_context_data(self, **kwargs):
        """Get context to populate page with resources."""

        main_category = [
            ("Crisis", "Crisis"),
            ("Addiction", "Addiction"),
            ("Childcare", "Childcare"),
            ("Youth Services", "Youth Services"),
            ("Veteran", "Veteran"),
            ("Rehabilitation", "Rehabilitation"),
            ("Mental/Physical Disability", "Mental/Physical Disability"),
            ("Education", "Education"),
            ("Employment", "Employment"),
            ("Finances", "Finances"),
            ("Clothing/Housewares", "Clothing/Housewares"),
            ("Food", "Food"),
            ("Healthcare", "Healthcare"),
            ("Shelter", "Shelter"),
            ("Legal", "Legal"),
            ("Identification", "Identification"),
            ("Spiritual", "Spiritual")
        ]

        context = super(HomePageView, self).get_context_data(**kwargs)
        context['choices'] = [category[0] for category in main_category]
        context['tags'] = Tag.objects.all()
        return context


class ResourceDetailView(DetailView):
    """Detail view for one organization."""

    template_name = "searchlist/resource_detail.html"
    model = Resource
    context_object_name = "resource"
