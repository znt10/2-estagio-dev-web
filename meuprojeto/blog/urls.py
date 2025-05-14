from django.urls import path
from .views import Post_ver, Post_DetailView, Post_CreateView, Post_UpdateView

urlpatterns = [
    path('', Post_ver.as_view(), name='postes'),
    path('ler/<int:pk>/', Post_DetailView.as_view(), name='ler_post'),
    path('/criar/', Post_CreateView.as_view(), name='criar_post'),
    path('/<int:pk>/editar', Post_UpdateView.as_view(), name='editar_post'),
    path('/<int:pk>/deletar', Post_UpdateView.as_view(), name='deletar_post')
]

