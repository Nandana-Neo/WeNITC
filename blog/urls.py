from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView,
                    LikeView,
                    blogpost_list,
                    get_posts_by_dateListView
                    )
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('',PostListView.as_view(), name='blog-home'),
    path('user/<str:username>',UserPostListView.as_view(), name='user-posts'),
    path('about/',views.about,name='blog-about'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name='post-delete'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('like/<int:pk>',LikeView,name='like_post'),

    path('events/',TemplateView.as_view(template_name='blog/events.html'),name='events'),

    path('calendar/<str:date>/', get_posts_by_dateListView.as_view(), name='get_posts_by_date'),
    path('api/posts/',blogpost_list,name='blogpost-list')
]
