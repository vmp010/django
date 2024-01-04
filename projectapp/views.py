from django.shortcuts import render,redirect
from django_pandas import io
import pandas as pd
import matplotlib.pyplot as plt
from django.shortcuts import render
import json
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout



from .models import Record_E1,Record_R1,CategoryE,CategoryR,DepositGoal
from projectapp.forms import addcategoryF,loginF,addrecordF,registF,editRrecordF,editErecordF,DepositGoalForm,DateFilterForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.conf import settings





# Create your views here.
def registe(request):
    if request.method =='POST':
         registerform=registF(request.POST)
         if registerform.is_valid():
            registerform.save()
            return redirect('login')
    else:
        registerform=registF()
    context={'registerform':registerform}    
    return render(request,'regist.html',context)
def loginpage(request):
    getdatabase=User.objects.all()
    if request.method =='POST':
        cName=request.POST['cName']
        password=request.POST['password']
        user=authenticate(request,username=cName,password=password)
        if user is not None:
            login(request,user)
            return redirect('/index')
            
            
    return render(request,'login.html',locals())

@login_required
def recordall_and_cashflow(request):
    # if request.user.is_authenticated:
    #      user=request.user
    #      user_data = User.objects.filter(id=user.id)
    deposit_goal = DepositGoal.objects.filter(user=request.user).first()
    corrent_user=request.user
    recordAllE=Record_E1.objects.filter(user=corrent_user).order_by('date')
    recordAllR=Record_R1.objects.filter(user=corrent_user).order_by('date')
    income_list=[record.cash for record in recordAllR]
    outcome_list=[record.cash for record in recordAllE]
    income=sum(income_list) if len(income_list)!=0 else 0
    outcome=sum(outcome_list) if len(outcome_list)!=0 else 0
    net = income -outcome
    form = DateFilterForm(request.GET or None)
    dataE=None
    dataR=None
    if form.is_valid():
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        if start_date and end_date:
            dataE = recordAllE.filter(date__range=(start_date, end_date))
            dataR = recordAllR.filter(date__range=(start_date, end_date))

        elif start_date:
            dataE = recordAllE.filter(date__gte=start_date) # gte:大於等於
            dataR = recordAllR.filter(date__gte=start_date)
        elif end_date:
            dataE = recordAllE.filter(date__lte=end_date) # lte:小於等於
            dataR = recordAllR.filter(date__lte=end_date)
    else:
        dataE = recordAllE
        dataR = recordAllR
    if 'cancel' in request.GET:
        return redirect('index')  # 或者重置表单并重新加载页面
    if deposit_goal:
        goal_amount = deposit_goal.goal_amount
        if goal_amount == 0:
            goal_percent = 0
        else:
            goal_percent = net / (goal_amount * 100)
            goal_percent = round(goal_percent, 2)
    else:
        goal_amount = 0
        goal_percent = 0
    return render(request,'index.html',locals())
    # else:
    #     return redirect('login')
@login_required
def addcategory(request):
    if request.method == 'POST':   
            categoryR=request.POST['addcategoryR']
            categoryE=request.POST['addcategoryE']
            unitR=CategoryR.objects.get_or_create(category=categoryR)
            # unitR.save() get_otcreate 會自動儲存
            unitE=CategoryE.objects.get_or_create(category=categoryE)
            # unitE.save() get_otcreate 會自動儲存
            return redirect('/index')
    return render(request,'addcategory.html',locals())


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
            user=request.user
            date=request.POST['date']
            description=request.POST['description']
            categoryE=request.POST['categoryE']
            cash=request.POST['cash']
            unit=Record_E1.objects.create(user=user,date=date,description=description,categoryE=categoryE,cash=cash)
            unit.save()#寫入資料庫
            return redirect('/index')
    else:
        addrecord=addrecordF()
        messages='新增支出紀錄'
    return render(request,'addErecord.html',locals())
@login_required
def addRrecord(request):
    cRselect=CategoryR.objects.all()
    if request.method=='POST':
            user=request.user
            date=request.POST['date']
            description=request.POST['description']
            categoryR=request.POST['categoryR']
            cash=request.POST['cash']
            unit=Record_R1.objects.create(user=user,date=date,description=description,categoryR=categoryR,cash=cash)
            unit.save()#寫入資料庫
            return redirect('/index')
    else:
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
def chart_data(request):
    corrent_user = request.user
    recordAllE = Record_E1.objects.filter(user=corrent_user)
    recordAllR = Record_R1.objects.filter(user=corrent_user)
    categoryR_totals = {}
    categoryE_totals = {}
    for item in recordAllR:
        category = item.categoryR
        cash = item.cash
        categoryR_totals[category] = categoryR_totals.get(category, 0) + cash
    for i in recordAllE:
        category = i.categoryE
        cash = i.cash
        categoryE_totals[category] = categoryE_totals.get(category, 0) + cash
    # 打印数据，检查是否正确获取

    chart_data = {
        # 'dataE': [{'label': record.categoryE, 'value': record.cash} for record in recordAllE],
        # 'dataR': [{'label': record.categoryR, 'value': record.cash} for record in recordAllR],
        'categoryR_totals': categoryR_totals,
        'categoryE_totals': categoryE_totals,
    }
    return render(request, 'charts.html', chart_data)



@login_required
def confirm_logout(request):
    if request.method == 'POST':
        if 'confirm_logout' in request.POST:
            # 如果用户确认登出，则执行登出操作
            from django.contrib.auth import logout
            logout(request)
            return redirect('login')  # 登出后重定向到首页或其他页面
        else:
            # 用户取消登出，重定向到某个页面或显示其他信息
            return redirect('index')  # 取消登出后重定向到首页或其他页面
    return render(request, 'confirm_logout.html')

@login_required
def set_deposit_goal(request):
    deposit_goal = DepositGoal.objects.filter(user=request.user).first()

    if request.method == 'POST':
        form = DepositGoalForm(request.POST)
        if form.is_valid():
            new_goal_amount = form.cleaned_data['goal_amount']
            if deposit_goal:
                deposit_goal.goal_amount = new_goal_amount
            else:
                # 如果存款目标不存在，创建一个新的存款目标
                deposit_goal = DepositGoal(user=request.user, goal_amount=new_goal_amount)
            deposit_goal.save()
            return redirect('index')  # 设置存款目标成功后重定向到首页或其他页面
    else:
        form = DepositGoalForm()
    context = {
        'deposit_goal': deposit_goal,
        'form': form,
    }
    return render(request, 'set_deposit_goal.html', context)