from django.urls import path
from . import views

app_name = 'blog' # Namespace para las URLs de esta app

# Aqui definimos las URLs especificas del blog
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('blog-<int:pk>/', views.post_detail, name='post_detail'),
]