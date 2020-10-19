from django import forms

from .models import FillUpForm


# DataFlair #File_Upload
class Fillup_Form(forms.ModelForm):
    class Meta:
        model = FillUpForm
        fields = (
            'firstName',
            'lastName',
            'email',
            'city',
            'state',
            'pincode',
            'Resume',
        )
