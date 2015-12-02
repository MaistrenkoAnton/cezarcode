from django.shortcuts import render
from .forms import ShifrForm


def index(request):

    data = request.POST.get('shifr')
    rot = request.POST.get('ROT')
    form = ShifrForm(request.POST)
    new_data = ''
    if 'shifr_but' in request.POST:
        if form.is_valid():
            for letter in data:
                print(ord(letter))
                if ord(letter) not in range(65, 91) and ord(letter) not in range(97, 123):
                    new_data += letter
                else:
                    if ord(letter) in range(65, 90):
                        if (ord(letter) + int(rot)) > 90:
                            new_data += chr(ord(letter) + int(rot) - 26)
                        else:
                            new_data += chr(ord(letter) + int(rot))
                    else:
                        if (ord(letter) + int(rot)) > 122:
                            new_data += chr(ord(letter) + int(rot)-26)
                        else:
                            new_data += chr(ord(letter) + int(rot))

    elif 'deshifr_but' in request.POST:
        if form.is_valid():
            for letter in data:
                if ord(letter) not in range(65, 91) and ord(letter) not in range(97, 123):
                    new_data += letter
                else:
                    if (ord(letter) - int(rot)) < 97:
                        new_data += chr(ord(letter) - int(rot) + 26)
                    else:
                        new_data += chr(ord(letter) - int(rot))

    context = {
        'form': form,
        'data': new_data,

    }
    return render(request, 'content.html', context)

