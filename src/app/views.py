from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.views.generic.base import View, TemplateResponseMixin, ContextMixin


# class LoginRequiredMixin(object):
#     @classmethod
#     def as_view(cls, *kwargs):
#         view = super(LoginRequiredMixin, cls).as_view(**kwargs)
#         return login_required(view)
#   (or)
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super(MyView, self).dispatch(request, *args, **kwargs)

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
