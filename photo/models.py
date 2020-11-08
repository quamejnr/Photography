from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.urls import reverse
from PIL import Image


class Post(models.Model):
    picture = models.ImageField(upload_to="pictures/")
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=200, default='', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    photographer = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='title', always_update=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})
