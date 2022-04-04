from . import views
from django.urls import path

app_name='blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='list'),
    path('detail/<slug:slug>/', views.PostDetail.as_view(), name='detail'),
    path('create/', views.PostCreate.as_view(), name='create'),
    path('draft/', views.PostDraft.as_view(), name='draft'),
    path('update/<slug>/', views.PostUpdate.as_view(), name='update'),
]