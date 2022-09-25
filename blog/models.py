from django.db import models
from django.utils import timezone

ENTRY_TYPES=[('blog', 0), ('diary', 1)]
# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    content = models.TextField()
    type = models.CharField(choices = ENTRY_TYPES, default = 'blog', max_length=10)
    entry_datetime = models.DateTimeField(blank=False, default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-entry_datetime']