from django import forms
from .models import Album
from datetime import datetime

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'topic', 'year']
        widgets = {
            'name': forms.TextInput(attrs={'id': 'album-name', 'class': 'form-control'}),
            'topic': forms.Select(attrs={'id': 'album-topic', 'class': 'form-select'}),
            'year': forms.NumberInput(attrs={
                'id': 'album-year',
                'class': 'form-control',
                'max': datetime.now().year,
            }),
        }
        labels = {
            'name': 'Назва альбому',
            'topic': 'Оберіть тему',
            'year': 'Рік альбому',
        }

    def clean_year(self):
        year = self.cleaned_data['year']
        current_year = datetime.now().year
        if year > current_year:
            raise forms.ValidationError(f"Рік не може бути ніж {current_year}.")
        return year