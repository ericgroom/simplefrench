from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tip

import pdb

# Create your views here.
class TipListView(ListView):
    model = Tip
    context_object_name = 'tips'

class TipDetailView(DetailView):
    model = Tip

class TipUpdateView(LoginRequiredMixin, UpdateView):
    fields = ['title', 'content',]
    model = Tip

class TipDeleteView(DeleteView):
    model = Tip
    success_url = reverse_lazy('tips:list')
    