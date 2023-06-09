from django import forms
from .models import Article


# Create your forms

class UserPostForm(forms.ModelForm):

    class Meta:
        model = Article
        exclude = ('author','created','published',)

        widget = {
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'article':forms.Textarea(attrs={'class':'form-control editable medium-editor-textarea post-content'}),
        }





 
