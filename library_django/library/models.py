from django.db import models
from django.contrib.auth.models import User, timezone
from django.urls import reverse
from users.models import Profile


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=2000)
    image = models.ImageField(default='articles/news.jpg', upload_to='articles')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})
