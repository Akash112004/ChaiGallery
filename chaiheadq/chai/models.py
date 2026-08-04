# # Create your models here.
from django.db import models


class Tea(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    image = models.ImageField(upload_to='tea_images/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    