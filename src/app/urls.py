from django.conf.urls import url
from .views import (
	AppTemplateView,
	MyView
	)


urlpatterns = [
    url(r'^app/$',AppTemplateView.as_view()),
    url(r'^app/myview/$',MyView.as_view(template_name = "home.html")),
]