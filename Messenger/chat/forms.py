from django import forms
from django.forms import Form, CharField


class SearchPeopleForm(forms.Form):
    name = forms.CharField(label='', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Пошук', 'class': 'search-input', 'type': 'search', 'autocomplete': 'off'}))

class MessageForm(Form):
    message = CharField(
        max_length= 255,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Повідомлення', 'name': 'message', 'autocomplete': 'off'})
    )