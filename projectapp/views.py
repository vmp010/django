from django.shortcuts import render,redirect
from projectapp.models import Record_E,Record_R,CategoryE,CategoryR,login_1
from projectapp.forms import addcategoryF,delselect,loginF,addrecordF,delRrecordF
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
def regist(request):
    getdatabase=login_1.objects.all()
    if request.method =='POST':
        cName=request.POST['cName']
        cEmail=request.POST['cEmail']
        password=request.POST['password']
       
        for check in getdatabase:
            if check.cName == cName and check.password == password :
                messages='已註冊過帳號' 
            elif check.cEmail == cEmail:
                messages='已註冊過此email'
        else:
            unit=login_1.objects.create(cName=cName,cEmail=cEmail,password=password)
            unit.save()
        return redirect('login')
        
    else:
        messages='請輸入用戶名、密碼及email'
    return render(request,'regist.html',locals())

def delRrecord(request,mode=None,id=None):
    delform=delRrecordF(request)
    if delform.is_valid():
        if mode=='del': #按按鈕
            unit=Record_R.objects.get(id=id)
            unit.date=delform.cleaned_data.get['date']
            unit.description=delform.cleaned_data.get['description']
            unit.categoryR=delform.cleaned_data.get['categoryR']
            unit.cash=delform.cleaned_data.get['cash']
            unit.delete()
            messages='已刪除'
            return redirect('/index')
        else:   #網址
            try:
                unit=Record_R.objects.get(id=id)
                strdata=str(unit.date)
                strdata2=strdata.replace("年","-")
                strdata2=strdata.replace('月',"-")
                strdata2=strdata.replace('日',"-")
                unit.date=strdata2
            except:
                messages='此紀錄不存在'
    else:
        delform=delRrecordF()
    return render(request,'delRrecord.html',locals())

def delErecord(request,mode=None,id=None):
    if mode=='del': #按按鈕
        unit=Record_E.objects.get(id=id)
        unit.date=request.GET['date']
        unit.description=request.GET['description']
        unit.categoryE=request.GET['categoryE']
        unit.cash=request.GET['cash']
        unit.delete()
        messages='已刪除'
        return redirect('/index')
    else:   #網址
        try:
            unit=Record_E.objects.get(id=id)
            strdata=str(unit.date)
            strdata2=strdata.replace("年","-")
            strdata2=strdata.replace('月',"-")
            strdata2=strdata.replace('日',"-")
            unit.date=strdata2
        except:
            messages='此紀錄不存在'
    return render(request,'delErecord.html',locals())


