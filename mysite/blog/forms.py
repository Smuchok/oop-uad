from .models import Titles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class TitlesForm(ModelForm):
    class Meta:
        model = Titles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва нового блогу',
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Опис'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата',
                'type': 'date',
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст',
            }),


        }