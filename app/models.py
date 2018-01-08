from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='app/static/Instagram/images')

    def image_url(self):
        return self.photo.url[len('app/static/'):]


# class Comment(models.Model):
#     comment = models.CharField(max_length=220)
#     document = models.ForeignKey(
#         Document, on_delete=models.SET_NULL, blank=True, null=True)