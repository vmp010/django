from django import forms

class addcategoryF(forms.Form):
    addcategoryR=forms.CharField(max_length=20)
    addcategoryE=forms.CharField(max_length=20)