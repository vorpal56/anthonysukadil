from django import forms
class ContactForm(forms.Form):
    # email=forms.CharField(widget =forms.)

    email=forms.CharField(widget = forms.TextInput(
        attrs={
            'class':'form-control',
            'type':'email',
            'style': "width: 100%",
            'placeholder':"email@example.com",
        }
    ), required = True)
    subject=forms.CharField(widget = forms.TextInput(
        attrs={
            'class':'form-control',
            'style': "width: 100%",
        }
    ), required = True)
    message=forms.CharField(widget = forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ), required= True)