from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', 
                           required=True,
                           widget=forms.TextInput(
                               attrs={
                                   'class':'form-control',
                                   'placeholder':'Escriba el Nombre'
                               }
                            ),
                           min_length=3,
                           max_length=100
                           )
    email = forms.EmailField(label='Email',
                             required=True,
                           widget=forms.EmailInput(
                               attrs={
                                   'class':'form-control',
                                   'placeholder':'Correo'
                               }
                            ),
                           min_length=3,
                           max_length=100
                           )
    content = forms.CharField(label='Mensaje',
                              required=True,
                              widget=forms.Textarea(
                               attrs={
                                   'class':'form-control',
                                   'rows':3,
                                   'placeholder':'Escriba el mensaje'
                                    }
                                ),
                              min_length=10,
                              max_length=200
                            )
    