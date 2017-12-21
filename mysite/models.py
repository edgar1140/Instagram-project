from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='Instagram/static/Instagram/images')