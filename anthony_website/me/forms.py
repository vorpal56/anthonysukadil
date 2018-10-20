from django import forms
class ContactForm(forms.Form):
    # email=forms.CharField(widget =forms.)
    email=forms.CharField(widget = forms.TextInput(attrs={
        'class':'form-control',
        
    }), required = True)
    message=forms.CharField(widget = forms.Textarea(
        attrs={
            'class':'form-control'
    }), required= True)