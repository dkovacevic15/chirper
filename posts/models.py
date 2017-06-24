from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    posted = models.DateTimeField(default=timezone.now)
    liked_by = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    class Meta:
        ordering = ('-posted',)

    def __str__(self):
        return str(self.author) + ': "' + str(self.content) + '"'
