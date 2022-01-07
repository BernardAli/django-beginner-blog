from django.urls import path
from .views import BlogListView, BlogDetailView, AboutView, \
    BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='post_delete'),
    path('new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>', BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update', BlogUpdateView.as_view(), name='post_update'),
    path('about/', AboutView.as_view(), name='about'),
]