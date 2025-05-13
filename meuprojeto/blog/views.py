from django.shortcuts import render
from .models import Post  # Certifique-se de importar o modelo

def blog(request):

    posts = Post.objects.all()  

    return render(request, 'blog/teste.html', {'posts': posts})
