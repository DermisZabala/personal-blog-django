from django.shortcuts import render, get_object_or_404
from .models import Post # importando el modelo Post
from django.utils import timezone # importando timezone

# Create your views here.


def post_list(request):
    # obtener todos los posts que estan publicados y cuya fecha de publicacion no es futura
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-create_date')

    # el contexto son los datos que pasamos a la plantilla
    context = {
        'posts': posts
    }

    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    # obtener el post especifico por su pk (Primary key)
    # si el post no existe o no esta publicado, devuelve un error 404 (Not Found)
    
    post = get_object_or_404(Post, pk=pk) # usando el pk recibido para buscar el post

    context = {
        'post': post
    }

    return render(request, 'blog/post_detail.html', context)
