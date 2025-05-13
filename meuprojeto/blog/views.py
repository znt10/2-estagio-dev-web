from django.views.generic import ListView
from .models import Post  

class Post_ver(ListView):
    model = Post
    template_name = 'blog/teste.html'
    context_object_name = 'posts'
