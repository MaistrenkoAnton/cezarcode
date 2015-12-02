from django.shortcuts import render
from .forms import ShifrForm


def index(request):
    new_data = ''
    form = ShifrForm(request.POST)
    if form.is_valid():
        data = request.POST.get('shifr')
        if 'shifr_but' in request.POST:
            step = int(request.POST.get('ROT'))
        else:
            step = -int(request.POST.get('ROT'))

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
    context = {
        'form': form,
        'data': new_data,

    }
    return render(request, 'content.html', context)

