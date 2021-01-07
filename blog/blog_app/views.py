from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import Blog

# Create your views here.
class BlogListView(ListView):
  model = Blog

class BlogDetailView(DetailView):
  model = Blog

class BlogCreateView(CreateView):
  model = Blog
  fields = ["content"]
  success_url = reverse_lazy("index")