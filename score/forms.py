from django import forms

class UploadFirst(forms.Form):
    take_pic = forms.ImageField(required=True)

class UploadSecond(forms.Form):
    choose_pic = forms.ImageField(required=True)
