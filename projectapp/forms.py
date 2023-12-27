from django import forms
from projectapp.models import CategoryE,CategoryR,Record_E1,Record_R1,login_1
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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
        model=Record_R1
        fields='date','description','categoryR','cash'
        wigits={'date':forms.TextInput(attrs={'class':'form-control'}),
                'description':forms.TextInput(attrs={'class':'form-control'}),
                'categoryR':forms.Select(attrs={'class':'form-control'}),
                'cash':forms.NumberInput(attrs={'class':'form-control'})}
        labels={'date':'日期','description':'說明','categoryR':'類別','cash':'金額'}


class delrecordEF(forms.ModelForm):
    class Meta:
        model=Record_E1
        fields='date','description','categoryE','cash'
        wigits={'date':forms.TextInput(attrs={'class':'form-control'}),
                'description':forms.TextInput(attrs={'class':'form-control'}),
                'categoryE':forms.Select(attrs={'class':'form-control'}),
                'cash':forms.NumberInput(attrs={'class':'form-control'})}
        labels={'date':'日期','description':'說明','categoryE':'類別','cash':'金額'}
class editRrecordF(forms.ModelForm): 
    class Meta:
        model=Record_R1
        fields='date','description','categoryR','cash'
        wigits={'date':forms.TextInput(attrs={'class':'form-control'}),
                'description':forms.TextInput(attrs={'class':'form-control'}),
                'categoryR':forms.Select(attrs={'class':'form-select'}),
                'cash':forms.NumberInput(attrs={'class':'form-control'})}
        labels={'date':'日期','description':'說明','categoryR':'類別','cash':'金額'}
class editErecordF(forms.ModelForm):
    class Meta:
        Choice=CategoryE.objects.all()
        model=Record_E1
        fields='date','description','categoryE','cash'
        wigits={'date':forms.TextInput(attrs={'class':'form-control'}),
                'description':forms.TextInput(attrs={'class':'form-control'}),
                'categoryE':forms.Select(choices=Choice,attrs={'class':'form-select'}),
                'cash':forms.NumberInput(attrs={'class':'form-control'})}
        labels={'date':'日期','description':'說明','categoryE':'類別','cash':'金額'}
class registF(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email' ,'password']  # 定义表单中包含的字段
    

   