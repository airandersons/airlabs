from django.urls import path
from . import views

app_name = 'main_site'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('projects/', views.projects, name='projects'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('blog_detail/<int:post_id>', views.blog_detail, name='blog_detail'),
    path('notfound/', views.notfound, name='404')
]