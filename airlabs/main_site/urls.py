from django.urls import path
from . import views

app_name = 'main_site'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('blog/', views.blog, name='blog'),
    path('project/', views.project, name='project'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('notfound/', views.notfound, name='404')
]