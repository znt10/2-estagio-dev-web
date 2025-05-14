from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from .models import Post
from django.urls import reverse_lazy


class Post_ver(ListView):
    model = Post
    template_name = 'blog/teste.html'
    context_object_name = 'posts'
    paginate_by = 6

class Post_DetailView(DetailView):
    model = Post
    template_name = 'blog/ler_detail.html'
    context_object_name = 'post_detalhe'

class Post_CreateView(CreateView):
    model = Post
    template_name = 'blog/criar_Create.html'
    fields = ['titulo', 'descricao', 'capa']  
    success_url = reverse_lazy('postes')
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
class Post_UpdateView(UpdateView):
    model = Post
    template_name = 'blog/editar_Update.html'
    fields = ['titulo', 'descricao', 'capa'] 
    success_url = reverse_lazy('postes')

class Post_DeleteView(DeleteView):
    model = Post
    template_name = 'blog/deleta_Delete.html'
    context_object_name = 'post_deletar'
    success_url = reverse_lazy('postes')
