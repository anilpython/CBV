from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.views.generic.base import View, TemplateResponseMixin, ContextMixin


class AppTemplateView(TemplateView):
	template_name = "home.html"

	def get_context_data(self, **kwargs):
		context = super(AppTemplateView, self).get_context_data(**kwargs)
		context['title'] = "Home Page"
		return context

class MyView(TemplateResponseMixin, ContextMixin, View):
	def get(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		context['title'] = "Some Base View"
		return self.render_to_response(context)