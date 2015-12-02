# -*- coding: utf-8 -*-
from .models import Note
from django import forms


class ShifrForm(forms.ModelForm):
    shifr = forms.CharField(label='',
                            error_messages={'required': 'Заполните поле для шифрования'},
                            widget=forms.Textarea(attrs={'class': 'form-control'}),
                            )
    label = forms.CharField(label='',
                            error_messages={'required': 'Напишите описание:'})
    ROT = forms.IntegerField(
                            error_messages={'required': 'Укажите глубину шифрования:'}
    )

    class Meta():
        model = Note
        fields = '__all__'