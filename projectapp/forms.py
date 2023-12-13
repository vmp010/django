from django import forms
from projectapp.models import CategoryE,CategoryR
class addcategoryF(forms.Form):
    addcategoryR=forms.CharField(max_length=20,required=True)
    addcategoryE=forms.CharField(max_length=20,required=True)
class delselect(forms.Form):
    delR_cat_option=CategoryR.objects.all()
    delselectR=forms.ModelChoiceField(queryset=delR_cat_option)
    delE_cat_option=CategoryE.objects.all()
    delselectE=forms.ModelChoiceField(queryset=delE_cat_option)
class loginF(forms.Form):
    cName=forms.CharField(max_length=20,required=True)
    password=forms.CharField(max_length=32, widget=forms.PasswordInput)
    