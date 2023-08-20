from django.urls import path
from . import views




urlpatterns = [
    path('', views.BlogList.as_view(), name='blog-list'),
    path('create/', views.BlogCreate.as_view(), name='blog-create'),
    path('<int:pk>/update/', views.BlogUpdate.as_view(), name='blog-update'),
    path('<int:pk>/comments/', views.CommentList.as_view(), name='comment-list'),
    path('<int:pk>/comments/create/', views.CommentCreate.as_view(), name='comment-create')
]
