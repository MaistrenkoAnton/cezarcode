# -*- coding: utf-8 -*-
from .models import Note
from django import forms


class ShifrForm(forms.ModelForm):
    shifr = forms.CharField(label='',
                            widget=forms.Textarea(attrs={'class': 'form-control'}),
                            )
    label = forms.CharField(label='', error_messages={'required': 'Напишите описание:'})

    class Meta():
        model = Note
        fields = '__all__'