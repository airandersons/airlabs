from django.db import models
from django.utils import timezone

class Testimonials(models.Model):
    """
    This data model is to create a table for testimonials.
    """
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=30)
    comment = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100)

class PostAuthor(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

class PostCategory(models.Model):
    name = models.CharField(max_length=30)

class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    short_detail = models.CharField(max_length=150)
    post_detail = models.TextField()
    post_author = models.ForeignKey(PostAuthor, on_delete=models.CASCADE, related_name='posts')
    post_category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, related_name='posts')
    post_date = models.DateField(auto_now_add=True)
    post_image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.post_author}"

class PostComments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=50)
    author_image = models.ImageField(upload_to='images/')
    comment = models.TextField()

