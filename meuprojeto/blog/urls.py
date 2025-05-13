from django.urls import path
from .views import Post_ver 

urlpatterns = [
    path('', Post_ver.as_view(), name='postes'), 
]
