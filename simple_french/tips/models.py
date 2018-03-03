from django.db import models
from django.urls import reverse

# Create your models here.
class Tip(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('tips:detail', kwargs={'pk': self.pk})
