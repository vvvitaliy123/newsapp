from django.db import models


class Post(models.Model):
    # Props:
    title = models.CharField(max_length=100)
    about = models.TextField(max_length=256)
    content = models.TextField(max_length=1024)
    author = models.CharField(max_length=100)
    image = models.FileField(upload_to='images/', null=True)
    publish = models.DateTimeField(auto_now_add=True)
    source = models.URLField()

    # Presenter:
    def __str__(self):
        return str(self.title)
