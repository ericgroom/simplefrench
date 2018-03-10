from django.db import models
from django.urls import reverse
import markdown

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, unique=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('guide.Article', null=True, blank=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property 
    def is_root(self):
        return self.parent is None
    
    def children(self):
        return Article.objects.filter(parent=self)

    @property
    def html(self):
        return markdown.markdown(self.body)

    def get_absolute_url(self):
        return reverse('guide:detail', kwargs={'pk': self.pk})
