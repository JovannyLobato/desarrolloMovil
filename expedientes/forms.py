from django import forms
from .models import Archivo, Persona

class ArchivoForm(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ['archivo']

    def clean_archivo(self):
        archivo = self.cleaned_data.get('archivo')
        if archivo:
            # Validacion de extension
            ext = archivo.name.split('.')[-1].lower()
            if ext not in ['jpg', 'jpeg', 'png', 'gif', 'pdf']:
                raise forms.ValidationError("Solo se permiten imagenes o PDF.")
        return archivo
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'descripcion']
