# posts/urls.py
from django.urls import path
from .views import PostListView, PostUpdateView, PostDetailView, PostDeleteView


urlpatterns = [
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'), # new
    path('<int:pk>/', PostDetailView.as_view(), name='post'), # new
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'), # new
    path('', PostListView.as_view(), name='home'),
]