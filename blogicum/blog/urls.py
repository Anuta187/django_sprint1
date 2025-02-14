from django.urls import path  # type: ignore
from . import views

app_name = 'blog'

urlpatterns: list[path] = [
    path('', views.index, name='index'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/',
         views.category_posts, name='category_posts')]
