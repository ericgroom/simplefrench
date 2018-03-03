from django.shortcuts import render
from .models import Tip

# Create your views here.
def index(request):
    context = {
        'tips': Tip.objects.all()
    }
    return render(request, 'tips/feed.html', context=context)