from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView
from .models import Post  
from django.urls import reverse_lazy

class Post_ver(ListView):
    model = Post
    template_name = 'blog/teste.html'
    context_object_name = 'posts'
    paginate_by = 4

class Post_DetailView(DetailView):
    model = Post
    template_name = 'blog/ler_detail.html'
    context_object_name = 'post_detalhe'

class Post_CreateView(CreateView):
    model = Post
    template_name = 'blog/criar_Create.html'
    fields = ['titulo', 'conteudo', 'imagem']
    success_url = reverse_lazy('postes_criar')

class Post_UpdateView(UpdateView):
    model = Post
    template_name = 'blog/editar_Update.html'
    fields = ['titulo', 'conteudo', 'imagem']
    success_url = reverse_lazy('posts_editar')
