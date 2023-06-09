from django import forms
from .models import Client

# Create your forms

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

        # widgets = {
        #     'name':forms.TextInput(attrs={'class':'form-control'}),
        #     'phone':forms.TextInput(attrs={'class':'form-control'})
        # }