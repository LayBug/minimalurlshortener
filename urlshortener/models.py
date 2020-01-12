from django.db import models
from django.urls import reverse


class ShortUrl(models.Model):
    original_url = models.URLField()
    suggested_url_suffix = models.CharField(max_length = 10, blank = True)
    generated_url = models.URLField(blank = True)
    slug = models.CharField(max_length = 12, blank = True)

    def __str__(self):
        return self.original_url

    def get_absolute_url(self):
        return reverse('success', kwargs={'pk':self.pk})
