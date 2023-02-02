from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    images = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} --- {self.images} --- posted at {self.created_at}'

