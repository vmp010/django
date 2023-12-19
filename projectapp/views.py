from django.shortcuts import render,redirect
from django_pandas import io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




from .models import Record_E,Record_R,CategoryE,CategoryR,login_1
from projectapp.forms import addcategoryF,delselect,loginF,addrecordF,delrecordEF,registF,delrecordRF,editRrecordF,editErecordF
# Create your views here.
def recordall_and_cashflow(request):
    recordE=Record_E.objects.all().order_by('date')
    recordR=Record_R.objects.all().order_by('date')
    
    recordAllE=Record_E.objects.filter()
    recordAllR=Record_R.objects.filter()
    income_list=[record.cash for record in recordAllR]
    outcome_list=[record.cash for record in recordAllE]
    income=sum(income_list) if len(income_list)!=0 else 0
    outcome=sum(outcome_list) if len(outcome_list)!=0 else 0

    net = income -outcome
    return render(request,'index.html',locals())
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

def addErecord(request):
    cEselect=CategoryE.objects.all()
    if request.method=='POST':
        addrecord=addrecordF(request.POST)
        if addrecord.is_valid():
            date=request.POST['date']
            description=request.POST['description']
            categoryE=request.POST['categoryE']
            cash=request.POST['cash']
            unit=Record_E.objects.create(date=date,description=description,categoryE=categoryE,cash=cash)
            unit.save()#寫入資料庫
            return redirect('/index')
    else:
        addrecord=addrecordF()
        messages='新增收入紀錄'
    return render(request,'addErecord.html',locals())

def addRrecord(request):
    cRselect=CategoryR.objects.all()
    if request.method=='POST':
        addrecord=addrecordF(request.POST)
        if addrecord.is_valid():
            date=request.POST['date']
            description=request.POST['description']
            categoryR=request.POST['categoryR']
            cash=request.POST['cash']
            unit=Record_R.objects.create(date=date,description=description,categoryR=categoryR,cash=cash)
            unit.save()#寫入資料庫
            return redirect('/index')
    else:
        addrecord=addrecordF()
        messages='新增收入紀錄'
    return render(request,'addRrecord.html',locals())

def loginpage(request):
    getdatabase=login_1.objects.all()
    if request.method =='POST':
        loginform=loginF(request.POST)
        if loginform.is_valid():
            cName=loginform.cleaned_data['cName']
            password=loginform.cleaned_data['password']
            for check in getdatabase:
                if check.cName == cName and check.password == password:
                    messages='帳號密碼正確'
                    return redirect('/index')
                else:
                    messages='帳號密碼錯誤'
    else:
        loginform=loginF()
        messages='請輸入帳號密碼'
    return render(request,'login.html',locals())





def registe(request):
    if request.method =='POST':
        registerform=registF(request.POST)
        if registerform.is_valid():
            cName=registerform.cleaned_data['cName']
            password=registerform.cleaned_data['password']
            cEmail=registerform.cleaned_data['cEmail']
            if login_1.objects.filter(cName=cName).exists():
                messages='已註冊過帳號'
            elif login_1.objects.filter(cEmail=cEmail).exists():
                messages='已註冊過此email'
            else:   
                unit=login_1.objects.create(cName=cName,cEmail=cEmail,password=password)
                unit.save()
                return redirect('login')
    else:
        registerform=registF()
        messages='請輸入帳號密碼'
    return render(request,'regist.html',locals())

def delRr(request,pk=None):
    revenue=Record_R.objects.get(id=pk)
    if request.method =='POST':
        revenue.delete()
        return redirect('/index')
    context={'revenue':revenue}
    return render(request,'delRr.html',context)
def delEr(request,pk=None):
    expense=Record_E.objects.get(id=pk)
    if request.method =='POST':
        expense.delete()
        return redirect('/index')
    context={'expense':expense}
    return render(request,'delEr.html',context)

def editRr(request,pk=None):
    revenue=Record_R.objects.get(id=pk)
    form=editRrecordF(instance=revenue)
    if request.method =='POST':
        form=editRrecordF(request.POST,instance=revenue)
        if form.is_valid():
            form.save()
            return redirect('/index')
    context={'form':form}
    return render(request,'editRr.html',context)
def editEr(request,pk=None):
    expense=Record_E.objects.get(id=pk)
    form=editErecordF(instance=expense)
    if request.method =='POST':
        form=editErecordF(request.POST,instance=expense)
        if form.is_valid():
            form.save()
            return redirect('/index')
    context={'form':form}
    return render(request,'editEr.html',context)

def analysisE(request):
    qs=Record_E.objects.all()
    df=io.read_frame(qs,fieldnames=['date','description','categoryE','cash'])
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
    
  


