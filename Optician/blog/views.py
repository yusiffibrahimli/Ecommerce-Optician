from django.shortcuts import render
# from .models import blog
from .models import *
from .forms import CommentsForm, ContactUsForm
# Create your views here.

def blog(request):
    # Your view logic here
    blogs = Blog.objects.all()

    if request.POST.get('name'):
        print(request.POST.get('name'))
        print(request.POST.get('email'))
        print(request.POST.get('comments'))

    context = {
        'form' : ContactUsForm(request.POST or None),
        'blogs' : blogs
    }

    return render(request, 'blog.html', context=context)

def blog_details(request,pk):
    blogs = Blog.objects.get(pk=pk)
    print(blogs)

    context = {
        'form' : CommentsForm(),
        'blogs' : blogs
    }
    return render(request, 'blog-details.html', context=context)

def contact(request):
    return render(request, 'contact-us.html') 