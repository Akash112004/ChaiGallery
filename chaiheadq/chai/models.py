# # Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Tea(models.Model):
    CATEGORY_CHOICES = [
        ('masala', 'Masala & Spiced'),
        ('green', 'Green & Fresh'),
        ('herbal', 'Herbal & Floral'),
        ('black', 'Strong & Black'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='teas'
    )

    name = models.CharField(max_length=100)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='masala'
    )

    description = models.TextField(blank=True)

    image = models.ImageField(upload_to='tea_images/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} - {self.name}'