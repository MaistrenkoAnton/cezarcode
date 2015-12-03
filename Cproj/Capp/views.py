from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .forms import ShifrForm


def index(request):
    if request.GET:
        new_data = ''
        data = request.GET.get('text')
        if 'shifr' == request.GET.get('command'):
            step = int(request.GET.get('code'))
        else:
            step = -int(request.GET.get('code'))
        capital_letters = [chr(letter) for letter in range(65, 91)]
        capital_letters_step = [capital_letters[(i+step+26) % 26] for i in range(0, 26)]
        low_letters = [chr(letter) for letter in range(97, 123)]
        low_letters_step = [low_letters[(i+step+26) % 26] for i in range(0, 26)]
        for letter in data:
            if letter in capital_letters:
                new_data += capital_letters_step[(ord(letter)-65) % 26]
            elif letter in low_letters:
                new_data += low_letters_step[(ord(letter)-97) % 26]
            else:
                new_data += letter
        return HttpResponse(JsonResponse({'text': new_data}))
    form = ShifrForm()
    context = {
        'form': form,
    }
    return render(request, 'content.html', context)

