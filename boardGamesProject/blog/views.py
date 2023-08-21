from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Create your views here.

def home(request):
    posts = BlogPost.objects.all()
    return render(request, 'home.html', {'posts': posts})

def detail(request, postId):
    post = get_object_or_404(BlogPost, id=postId)
    if 'recently_read' in request.session:
        for (id, title) in request.session['recently_read']:
            if post.id == id:
                request.session['recently_read'].remove([id, title])
        
        request.session['recently_read'].insert(0, [post.id, post.title])

        if len(request.session['recently_read']) > 4:
            request.session['recently_read'].pop()
    else:
        request.session['recently_read'] = [[post.id, post.title]]

    request.session.modified = True
    
    return render(request, 'detail.html', {'post':post, 'recently_read': request.session['recently_read'][1:]})