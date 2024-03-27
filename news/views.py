from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class PostList(ListView):
    model = Post
    ordering = '-datetime'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10  # количество записей на странице

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time'] = datetime.utcnow()
        context['next_sale'] = None
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time'] = datetime.utcnow()
        context['next_sale'] = None
        return context


class SearchList(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'search'
    filterset_class = PostFilter
    #paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewCreateView(CreateView):
    model = Post
    template_name = 'create.html'
    context_object_name = 'create'
    form_class = PostForm

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/news/article/create/':
            post.field_choice = 'AR'
        post.save()
        return super().form_valid(form)


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'edit.html'
    context_object_name = 'edit'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/news/article/<int:pk>/edit/':
            post.update = 'AR'
        else:
            "Здесь редактируются только статьи."
        post.save()
        return super().form_valid(form)


class PostDelete(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('post_list')
    context_object_name = 'delete'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/news/article/<int:pk>/delete/':
            post.field_choice = 'AR'
        post.save()
        return super().form_valid(form)
