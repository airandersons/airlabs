from django.contrib import admin
from . models import Testimonials, Blog, Post, PostAuthor, PostCategory, PostComments

admin.site.register(Testimonials)
admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(PostAuthor)
admin.site.register(PostCategory)
admin.site.register(PostComments)
