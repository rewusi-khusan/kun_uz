from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=500)
    slug = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    video_link = models.CharField(max_length=255, blank=True, null=True)
    published_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    views_count = models.IntegerField(default=0)


    def __str__(self):
        return self.slug