from django import forms
from samapp.models import itdesk,up_load

class itdeskform(forms.ModelForm):
    class Meta:
        model=itdesk
        fields="__all__"

class uploadform(forms.ModelForm):
    class Meta:
        model=up_load
        fields="__all__"