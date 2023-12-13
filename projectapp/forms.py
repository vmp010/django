from django import forms

class addcategoryF(forms.Form):
    addcategoryR=forms.CharField(max_length=20,required=True)
    addcategoryE=forms.CharField(max_length=20,required=True)
class delcheckbox(forms.Form):
    delcheckboxR=forms.BooleanField(required=False)
    delcheckboxE=forms.BooleanField(required=False)