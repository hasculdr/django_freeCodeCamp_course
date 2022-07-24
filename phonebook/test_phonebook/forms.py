from .models import Peeps, Names, Patronymics
from django.forms import ModelForm, TextInput

class PeepsForm(ModelForm):
    class Meta:
        model = Peeps
        fields = ['phone_number','last_name']
        widgets = {
            'phone_number': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Номер телефона',
                },
            ),
            'last_name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Фамилия',
                }
            )
        }

class NamesForm(ModelForm):
    class Meta:
        model = Names
        fields = ['first_name']
        widgets = {
            'first_name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Имя',
                }
            )
        }
    
class PatronymicsForm(ModelForm):
    class Meta:
        model = Patronymics
        fields = ['middle_name']
        widgets = {
            'middle_name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Отчество',
                }
            )
        }
