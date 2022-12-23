from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from blog.forms import PostForm
from blog.models import Post

# Create your views here.
@login_required(login_url='/admin/')
def add_post(request):
    if request.method == 'POST':
        post = PostForm(request.POST)
        if post.is_valid():
            post = post.save(commit=False)
            post.author = request.user.profile
            post.save()
            return redirect('/posts')
        else:
            return HttpResponse('ERROR')
    else:
        form = PostForm()
        return render(request, 'post_add.html', {'form': form})


def view_posts(request):
    search = request.GET.get('search')
    # get all posts from the database: post = Post.objects...
    if search:
        posts = Post.objects.filter(
            Q(title__contains=search) | Q(text__contains=search)
            ).order_by('-created_date')
    else:
        posts = Post.objects.all().order_by('-created_date')
    return render(request, 'view_posts.html', {'posts': posts, 'title': 'All Posts'})