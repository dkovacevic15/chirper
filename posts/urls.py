from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from posts import views

urlpatterns = [
    url(r'$^', views.post_list),
    url(r'(?P<pk>\d+)/$', views.post_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)