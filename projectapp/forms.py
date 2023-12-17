from django import forms
from projectapp.models import CategoryE,CategoryR,Record_E,Record_R,login_1
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
    password=forms.CharField(max_length=32, widget=forms.PasswordInput())
class addrecordF(forms.Form):
    date=forms.DateField()
    description=forms.CharField(max_length=50,required=False)
    category=forms.Select()
    cash=forms.NumberInput()

class delrecordRF(forms.ModelForm):
    class Meta:
        model=Record_R
        fields='date','description','categoryR','cash'


class delrecordEF(forms.ModelForm):
    class Meta:
        model=Record_E
        fields='date','description','categoryE','cash'
class editRrecordF(forms.ModelForm): 
    class Meta:
        model=Record_R
        fields='date','description','categoryR','cash'
class editErecordF(forms.ModelForm):
    class Meta:
        model=Record_E
        fields='date','description','categoryE','cash'
class registF(forms.Form):
    cName=forms.CharField(max_length=20,required=True)
    password=forms.CharField(max_length=32, widget=forms.PasswordInput())
    cEmail=forms.EmailField(max_length=100,required=True)

   