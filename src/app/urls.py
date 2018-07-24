from django.conf.urls import url
from .views import (
	AppTemplateView,
	MyView,
	PersonDetailView,
	PersonListView,
	PersonCreateView,
	PersonUpdateView,
	)


urlpatterns = [
    url(r'^app/$',AppTemplateView.as_view()),
    url(r'^app/myview/$',MyView.as_view(template_name = "home.html")),
    url(r'^app/person/$',PersonListView.as_view(), name="list"),
    url(r'^app/person/(?P<slug>[-\w]+)/$',PersonDetailView.as_view(), name="detail"),
    url(r'^app/person/(?P<slug>[-\w]+)/update/$',PersonUpdateView.as_view(), name="update"),
    url(r'^app/person/create/create/$',PersonCreateView.as_view(),name="create"),
]