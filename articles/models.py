from django.db import models
from django.template.defaultfilters import slugify
from django.utils.safestring import SafeString

import markdown

class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=False)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=140)
    body = models.TextField()
    img_link = models.CharField(max_length=2000)
    slug = models.SlugField()
    shouldDarkenHeader = models.BooleanField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def get_markdown(self):
        return SafeString(markdown.markdown(self.body))

    class Meta:
        ordering = ['-created_at']
