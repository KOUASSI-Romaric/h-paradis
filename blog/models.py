from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to='articlesimg')
    create_at = models.DateTimeField(auto_now_add=True)
    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.title
