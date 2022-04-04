from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Post
from .forms import PostCreateForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView


class PostList(ListView):
    template_name = 'blog/post_list.html' 
    model = Post
    context_object_name = "post_list"
    paginate_by = 12
    ordering = ['-created_on']

    def get_queryset(self):
        return Post.objects.filter(status=1)

class PostDetail(DetailView):
    template_name = 'blog/post_detail.html'
    model = Post
    context_object_name = "post_detail"

class PostCreate(LoginRequiredMixin, CreateView):
    template_name = 'blog/post_create.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.status = 1
        self.object.save()
        return redirect('blog:list')

class PostDraft(LoginRequiredMixin, CreateView):
    template_name = 'blog/post_create.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.status = 0
        self.object.save()
        return redirect('blog:list')

class PostUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'blog/post_update.html'
    context_object_name = "post"
    model = Post
    fields = [
        'title',
        'content',
        'thumb',
        'slug',
    ]
    success_url = reverse_lazy('blog:list')
