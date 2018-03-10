from django.db import models
from django.urls import reverse
import markdown

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, unique=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def html(self):
        return markdown.markdown(self.body)

    def get_absolute_url(self):
        return reverse('guide:detail', kwargs={'pk': self.pk})


class TableOfContentsNode(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE, related_name='toc_node')
    is_root = models.BooleanField(default=False)
    parent = models.ForeignKey('TableOfContentsNode', null=True, blank=True, on_delete=models.SET_NULL, related_name='children')
    order = models.IntegerField()

    def as_dict(self, max_depth=3, depth=1):
        if depth <= max_depth:
            return { 
                'article': self.article,
                'children': [child.as_dict(depth=depth+1) for child in list(self.children.all().order_by('order'))]
                 }
        else:
            return {
                'article': self.article,
                'children': []
            }

    def __str__(self):
        return self.article.title
