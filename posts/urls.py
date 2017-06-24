from django.conf.urls import url
from posts import views

urlpatterns = [
    url(r'^api/posts/$', views.post_list),
]