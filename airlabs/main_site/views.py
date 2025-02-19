from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

def index(request):
    template = loader.get_template('main_site/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def about(request):
    return render(request, 'main_site/about.html', {})

def service(request):
    return render(request, 'main_site/service.html', {})

def contact(request):
    return render(request, 'main_site/contact.html', {})

def blog(request):
    return render(request, 'main_site/blog.html', {})

def project(request):
    return render(request, 'main_site/project.html', {})

def team(request):
    return render(request, 'main_site/team.html', {})

def notfound(request):
    return render(request, 'main_site/404.html', {})

def testimonial(request):
    return render(request, 'main_site/testimonial.html')
