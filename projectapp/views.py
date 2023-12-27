from django.shortcuts import render,redirect
from django_pandas import io
import pandas as pd
import matplotlib.pyplot as plt
from django.shortcuts import render
import json
from django.contrib import messages
from django.contrib.auth.models import User



from .models import Record_E1,Record_R1,CategoryE,CategoryR,login_1
from projectapp.forms import addcategoryF,loginF,addrecordF,registF,editRrecordF,editErecordF
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login


# Create your views here.
def registe(request):
    if request.method =='POST':
        registerform=registF(request.POST)
        if registerform.is_valid():
            cName=registerform.cleaned_data['username']
            password=registerform.cleaned_data['password']
            cEmail=registerform.cleaned_data['email']
            if User.objects.filter(username=cName).exists():
                messages='已註冊過帳號'
            elif User.objects.filter(email=cEmail).exists():
                messages='已註冊過此email'
            else:   
                unit=User.objects.create(username=cName,email=cEmail,password=password)
                unit.save()
                return redirect('login')
    else:
        registerform=registF()
        messages='請輸入帳號密碼'
    return render(request,'regist.html',locals())
def loginpage(request):
    getdatabase=User.objects.all()
    if request.method =='POST':
        loginform=loginF(request.POST)
        if loginform.is_valid():
            cName=loginform.cleaned_data['cName']
            password=loginform.cleaned_data['password']
            for check in getdatabase:
                if check.username == cName and check.password == password:
                    messages='帳號密碼正確'
                    return redirect('/index')
                else:
                    messages='帳號密碼錯誤'
    else:
        loginform=loginF()
        messages='請輸入帳號密碼'
    return render(request,'login.html',locals())

@login_required
def recordall_and_cashflow(request):
    # if request.user.is_authenticated:
    #      user=request.user
    #      user_data = User.objects.filter(id=user.id)
    recordE=Record_E1.objects.filter().order_by('date')
    recordR=Record_R1.objects.filter().order_by('date')
    
    recordAllE=Record_E1.objects.filter()
    recordAllR=Record_R1.objects.filter()
    income_list=[record.cash for record in recordAllR]
    outcome_list=[record.cash for record in recordAllE]
    income=sum(income_list) if len(income_list)!=0 else 0
    outcome=sum(outcome_list) if len(outcome_list)!=0 else 0

    net = income -outcome
    return render(request,'index.html',locals())
    # else:
    #     return redirect('login')
@login_required
def addcategory(request):
    if request.method == 'POST':
        addform=addcategoryF(request.POST)
        if addform.is_valid():   
            categoryR=addform.cleaned_data['addcategoryR']
            categoryE=addform.cleaned_data['addcategoryE']
            unitR=CategoryR.objects.get_or_create(category=categoryR)
            # unitR.save() get_otcreate 會自動儲存
            unitE=CategoryE.objects.get_or_create(category=categoryE)
            # unitE.save() get_otcreate 會自動儲存
            return redirect('/index')
    return render(request,'addcategory.html',locals())

def get_category_option(request):
    categoryR=CategoryR.objects.all()
    categoryE=CategoryE.objects.all()
    # return render(request,'delcategory.html',locals())
@login_required    
def delcategory(request):
    categoryR=CategoryR.objects.all()
    categoryE=CategoryE.objects.all()
    if request.method =='POST':
        delR=request.POST['delR']
        delE=request.POST['delE']
    try:
        unitR=CategoryR.objects.get(category=delR)
        unitR.delete()
        unitE=CategoryE.objects.get(category=delE)
        unitE.delete()
        return redirect('/index')
    except:
        messange='未接收資料'
    return render(request,'delcategory.html',locals())
@login_required
def addErecord(request):
    cEselect=CategoryE.objects.all()
    if request.method=='POST':
        addrecord=addrecordF(request.POST)
        if addrecord.is_valid():
            date=request.POST['date']
            description=request.POST['description']
            categoryE=request.POST['categoryE']
            cash=request.POST['cash']
            unit=Record_E1.objects.create(date=date,description=description,categoryE=categoryE,cash=cash)
            unit.save()#寫入資料庫
            return redirect('/index')
    else:
        addrecord=addrecordF()
        messages='新增收入紀錄'
    return render(request,'addErecord.html',locals())
@login_required
def addRrecord(request):
    cRselect=CategoryR.objects.all()
    if request.method=='POST':
        addrecord=addrecordF(request.POST)
        if addrecord.is_valid():
            date=request.POST['date']
            description=request.POST['description']
            categoryR=request.POST['categoryR']
            cash=request.POST['cash']
            unit=Record_R1.objects.create(date=date,description=description,categoryR=categoryR,cash=cash)
            unit.save()#寫入資料庫
            return redirect('/index')
    else:
        addrecord=addrecordF()
        messages='新增收入紀錄'
    return render(request,'addRrecord.html',locals())








@login_required
def delRr(request,pk=None):
    revenue=Record_R1.objects.get(id=pk)
    if request.method =='POST':
        revenue.delete()
        return redirect('/index')
    context={'revenue':revenue}
    return render(request,'delRr.html',context)
@login_required
def delEr(request,pk=None):
    expense=Record_E1.objects.get(id=pk)
    if request.method =='POST':
        expense.delete()
        return redirect('/index')
    context={'expense':expense}
    return render(request,'delEr.html',context)
@login_required
def editRr(request,pk=None):
    revenue=Record_R1.objects.get(id=pk)
    form=editRrecordF(instance=revenue)
    if request.method =='POST':
        form=editRrecordF(request.POST,instance=revenue)
        if form.is_valid():
            form.save()
            return redirect('/index')
    context={'form':form}
    return render(request,'editRr.html',context)
@login_required
def editEr(request,pk=None):
    expense=Record_E1.objects.get(id=pk)
    form=editErecordF(instance=expense)
    if request.method =='POST':
        form=editErecordF(request.POST,instance=expense)
        if form.is_valid():
            form.save()
            return redirect('/index')
    context={'form':form}
    return render(request,'editEr.html',context)

@login_required
def analysisE(request):
     qs=Record_E1.objects.all()
     df=io.read_frame(qs,fieldnames=['date','description','categoryE','cash'])
     plt.rc('font', family='Microsoft JhengHei')

     df.set_index('categoryE',inplace=True)
     pd.to_datetime(df['date'])
     fig,ax=plt.subplots(figsize=(10,5))
     ax.plot(df['cash'],marker='o',linestyle='--',color='r')
     ax.set_xlabel('categoryE')
     ax.set_ylabel('cash')
     plt.title('expense')
     plt.grid(axis='y')
     x=plt.show()
     return render(request,'analysisE.html',locals())
def chart_data(request):
    data = [5, 10, 15, 20, 25]
    context = {'data': json.dumps(data)}
    return render(request, 'charts.html', context)    
  


