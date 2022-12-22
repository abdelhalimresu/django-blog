from django.shortcuts import render
from django.http import HttpResponse

from blog.forms import PostForm

# Create your views here.
def add_post(request):
    if request.method == 'POST':
        post = PostForm(request.POST)
        if post.is_valid():
            post = post.save(commit=False)
            post.author = request.user.profile
            post.save()
            return HttpResponse('OK')
        else:
            return HttpResponse('ERROR')
    else:
        form = PostForm()
        return render(request, 'post_add.html', {'form': form})
