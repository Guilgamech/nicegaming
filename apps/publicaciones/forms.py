from django import forms
from django.forms.widgets import TextInput
from .models import Contacto


class contactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
        exclude = ('estado',)

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control form-group row col-md-12 mb-3 ',
                    'placeholder': 'Ingrese su Nombre'

                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control row form-group col-md-12',
                    'placeholder': 'Ingrese su Correo'
                }
            ),
            'asunto': forms.TextInput(
                attrs={
                    'class': 'form-control row form-group col-md-12',
                    'placeholder': 'Ingrese el Asunto'
                }
            ),
            'mensaje': forms.Textarea(
                attrs={
                    'class': 'form-control row form-group col-md-12',
                    'placeholder': 'Ingrese su Mensaje'
                }
            ),
        }


