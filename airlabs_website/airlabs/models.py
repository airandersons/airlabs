from django.db import models
from django.utils import timezone

class Testimonials(models.Model):
    class Meta:
        db_table = 'airlabs_testimonials'
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
    class Meta:
        db_table = 'airlabs_blog'
    title = models.CharField(max_length=100)

class PostAuthor(models.Model):
    class Meta:
        db_table = 'airlabs_post_author'
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

class PostCategory(models.Model):
    class Meta:
        db_table = 'airlabs_post_category'
    name = models.CharField(max_length=30)

class Post(models.Model):
    class Meta:
        db_table = 'airlabs_post'
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
    class Meta:
        db_table = 'airlabs_post_comments'
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=50)
    author_email = models.EmailField(max_length=320)
    author_image = models.ImageField(upload_to='images/', blank=True, null=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author_name} on {self.post.title}"

