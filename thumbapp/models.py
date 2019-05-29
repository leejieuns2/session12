from django.db import models

class Picture(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="img")
    objects = models.Manager()

    def __str__(self):
        return self.text


