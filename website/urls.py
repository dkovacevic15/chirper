from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(url=reverse_lazy('homepage'))),
    url(r'^home$', views.homepage, name='homepage'),
    url(r'^signup$', views.landingpage, name='landingpage'),
]