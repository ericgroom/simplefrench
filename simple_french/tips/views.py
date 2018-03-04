from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Tip

# Create your views here.
class TipListView(ListView):
    model = Tip
    context_object_name = 'tips'

class TipDetailView(DetailView, DeleteView):
    model = Tip

class TipUpdateView(LoginRequiredMixin, UpdateView):
    fields = ['title', 'content',]
    model = Tip