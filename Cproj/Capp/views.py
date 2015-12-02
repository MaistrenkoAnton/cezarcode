from django.shortcuts import render
from .forms import ShifrForm


def index(request):
    data = request.POST.get('shifr')
    rotate = request.POST.get('ROT')
    context = {
        'form': ShifrForm,
        'data': data,
    }
    return render(request, 'content.html', context)

