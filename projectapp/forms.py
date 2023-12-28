from django import forms
from projectapp.models import CategoryE,CategoryR,Record_E1,Record_R1,DepositGoal
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError 
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
class registF(UserCreationForm):
        username = forms.CharField(label='username', min_length=5, max_length=150)  
        email = forms.EmailField(label='email')  
        password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
        password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)  
  
        def username_clean(self):  
            username = self.cleaned_data['username'].lower()  
            new = User.objects.filter(username = username)  
            if new.count():  
                raise ValidationError("User Already Exist")  
            return username  
  
        def email_clean(self):  
            email = self.cleaned_data['email'].lower()  
            new = User.objects.filter(email=email)  
            if new.count():  
                raise ValidationError(" Email Already Exist")  
            return email  
  
        def clean_password2(self):  
            password1 = self.cleaned_data['password1']  
            password2 = self.cleaned_data['password2']  
  
            if password1 and password2 and password1 != password2:  
                raise ValidationError("Password don't match")  
            return password2  
  
        def save(self, commit = True):  
            user = User.objects.create_user(  
                self.cleaned_data['username'],  
                self.cleaned_data['email'],  
                self.cleaned_data['password1']  
        )  
            return user  

class DepositGoalForm(forms.ModelForm):
    class Meta:
        model = DepositGoal
        fields = ['goal_amount', 'deadline']