from django.shortcuts import render, get_object_or_404
from .models import Post    # Importamos la base de datos
# Create your views here.


def renderPost(request):
    posts = Post.objects.all()  #Select chido
    return render(request, 'post.html', {'posts': posts})


def postDetail(request, postID):
    post = get_object_or_404(Post, pk=postID)
    return render(request, 'postDetail.html', {'post': post})



