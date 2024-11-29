from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from app.models import Article


class ArticleListView(ListView):
    template_name='app/home.html'
    model = Article
    context_object_name = 'articles'


class ArticleCreateView(CreateView):
    template_name = 'app/article_create.html'
    model = Article
    fields = ['title', 'status', 'content', 'twitter_post']
    success_url = reverse_lazy('home')

    def form_valid(self ,form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    template_name = 'app/article_update.html'
    model = Article
    fields = ['title', 'status', 'content', 'twitter_post']
    success_url = reverse_lazy('home')
    context_object_name = 'article'


class ArticleDeleteView(DeleteView):
    template_name = 'app/article_delete.html'
    model = Article
    success_url = reverse_lazy('home')
    context_object_name = 'article'