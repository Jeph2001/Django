from django import forms
from .models import Collecting


class CollectingForm(forms.ModelForm):
    

    class Meta:
        model = Collecting
        fields = "__all__"

