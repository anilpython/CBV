from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.views.generic.base import View, TemplateResponseMixin, ContextMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Person
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import Http404


# class LoginRequiredMixin(object):
#     @classmethod
#     def as_view(cls, *kwargs):
#         view = super(LoginRequiredMixin, cls).as_view(**kwargs)
#         return login_required(view)
#   (or)
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super(MyView, self).dispatch(request, *args, **kwargs)

class MultipleObjectMixin(object):
    def get_object(self, queryset=None, *args, **kwargs):
        slug = self.kwargs.get("slug")
        if slug:
            try:
                obj = self.model.objects.get(slug=slug)
            except self.model.MultipleObjectsReturned:
                obj = self.get_queryset().first()
            except:
                raise Http404
            return obj
        raise Http404

class AppTemplateView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(AppTemplateView, self).get_context_data(**kwargs)
        context['title'] = "Home Page"
        return context

class MyView(ContextMixin, TemplateResponseMixin, View):
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['title'] = "Some Base View"
        return self.render_to_response(context)

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(MyView, self).dispatch(request, *args, **kwargs)

class PersonDetailView(MultipleObjectMixin, DetailView):
    template_name = "detail.html"    
    lookup_field = "slug"
    model = Person

    # def get_object(self, queryset=None, *args, **kwargs):
    #     slug = self.kwargs.get("slug")
    #     if slug:
    #         try:
    #             obj = self.model.objects.get(slug=slug)
    #         except self.model.MultipleObjectsReturned:
    #             obj = self.get_queryset().first()
    #         except:
    #             obj = None
    #         return obj
    #     return None

class PersonListView(ListView):
    model = Person
    template_name = "list.html"

    def get_queryset(self, *args, **kwargs):
        qs = super(PersonListView, self).get_queryset(*args, **kwargs).filter()[:3]
        return qs

class PersonCreateView(CreateView):
    model = Person
    template_name = 'form.html'
    fields = ["name","age"]
    # success_url = "/app/person/"

    # def form_valid(self, form):
    #     form.instance.added_by = self.request.user
    #     return super(PersonCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("app:list")

class PersonUpdateView(UpdateView):
    model = Person
    fields = ['name','age','slug'] # form_class = PersonModelForm
    template_name = "form.html"