from django import forms

class FormularioContacto (forms.Form):
    nombre_contacto = forms.CharField(label='Nombre', required= True)
    email_contacto = forms.CharField(label='Email', required= True)
    contenido_formulario_contacto = forms.CharField(label='Contenido', required= True, widget=forms.Textarea)