from django import forms
from .models import TakePicture
from .models import ChoosePicture

class UploadFirst(forms.ModelForm):
    class Meta:
        model = TakePicture
        fields = ['take_pic']
    take_pic = forms.ImageField(required=True)

class UploadSecond(forms.Form):
    class Meta:
        model = ChoosePicture
        fields = ['choose_pic']
    choose_pic = forms.ImageField(required=True)
