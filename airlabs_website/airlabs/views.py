from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from . models import Testimonials, Post, PostCategory, PostAuthor, PostComments, Blog
from . forms import TestimonialsForm, PostCommentForm

def index(request):
    testimonies = Testimonials.objects.all()
    posts = Post.objects.select_related('post_author', 'blog','post_category').order_by('-post_date')[:3]
    template = loader.get_template('airlabs/index.html')
    context = {'testimonies': testimonies, 'posts': posts}
    return HttpResponse(template.render(context, request))

def about(request):
    return render(request, 'airlabs/about.html', {})

def services(request):
    return render(request, 'airlabs/service.html', {})

def contact(request):
    return render(request, 'airlabs/contact.html', {})

def blog(request):
    posts = Post.objects.select_related('post_author', 'blog','post_category').order_by('-post_date')[:3]
    template = loader.get_template('airlabs/blog.html')
    context = {'posts': posts}
    return HttpResponse(template.render(context, request))

def projects(request):
    return render(request, 'airlabs/project.html', {})

def team(request):
    return render(request, 'airlabs/team.html', {})

def notfound(request):
    return render(request, 'airlabs/404.html', {})

def testimonial(request):
    return render(request, 'airlabs/testimonial.html')

def blog_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()[:2] # Get comments related to post
    form = PostCommentForm()
    context = {'post': post, 'comments': comments, 'form': form}

    if request.method == 'POST':
        form = PostCommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False) # Don't save yet
            comment.post = post # Assign post to the comment
            comment.save()
            return redirect('airlabs/blog_detail', post_id=post.id)
        
    return render(request, 'airlabs/blog_detail.html', context)

def upload_image(request):
    if request.method == 'POST':
        form = TestimonialsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app/index.html')  # Redirect to a success page
    else:
        form = TestimonialsForm()
    return render(request, 'admin.html', {'form': form})
