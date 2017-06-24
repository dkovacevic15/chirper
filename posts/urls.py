from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from posts import views

urlpatterns = [
    url(r'^api/posts/$', views.PostList.as_view()),
    url(r'^api/posts/(?P<pk>\d+)/$', views.PostDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)