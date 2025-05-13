from django.urls import path
from . import views

urlpatterns = [
    path('postes/', views.blog, name='postes'),
]
