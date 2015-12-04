# -*- coding: utf-8 -*-
from .models import Note
from django import forms


class ShifrForm(forms.ModelForm):
    shifr = forms.CharField(label='',
                            error_messages={'required': 'Заполните поле для шифрования'},
                            widget=forms.Textarea(attrs={'class': 'form-control',
                                                         'ng-model': 'text',
                                                         'onkeyup': 'func()'}),
                            )
    label = forms.CharField(label='',
                            error_messages={'required': 'Напишите описание:'},
                            widget=forms.TextInput(attrs={'ng-model': 'label'}))
    ROT = forms.IntegerField(widget=forms.TextInput(attrs={'ng-model': 'code',
                                                           'type': 'number'}),
                             error_messages={'required': 'Укажите глубину шифрования:'}
                            )

    class Meta():
        model = Note
        fields = '__all__'