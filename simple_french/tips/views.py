from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from .models import Tip

# Create your views here.
class TipListView(ListView):
    model = Tip
    context_object_name = 'tips'

class TipDetailView(DetailView):
    model = Tip

class TipUpdateView(UpdateView):
    fields = ['title', 'content',]
    model = Tip