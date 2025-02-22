from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from . models import Testimonials, Post, PostCategory, PostAuthor, PostComments, Blog
from . forms import TestimonialsForm

def index(request):
    testimonies = Testimonials.objects.all()
    posts = Post.objects.select_related('post_author', 'blog','post_category').order_by('-post_date')[:3]
    template = loader.get_template('main_site/index.html')
    context = {'testimonies': testimonies, 'posts': posts}
    return HttpResponse(template.render(context, request))

def about(request):
    return render(request, 'main_site/about.html', {})

def services(request):
    return render(request, 'main_site/service.html', {})

def contact(request):
    return render(request, 'main_site/contact.html', {})

def blog(request):
    return render(request, 'main_site/blog.html', {})

def projects(request):
    return render(request, 'main_site/project.html', {})

def team(request):
    return render(request, 'main_site/team.html', {})

def notfound(request):
    return render(request, 'main_site/404.html', {})

def testimonial(request):
    return render(request, 'main_site/testimonial.html')

def blog_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'main_site/blog_detail.html', context)

def upload_image(request):
    if request.method == 'POST':
        form = TestimonialsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app/index.html')  # Redirect to a success page
    else:
        form = TestimonialsForm()
    return render(request, 'admin.html', {'form': form})
