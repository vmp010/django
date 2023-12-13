from django.shortcuts import render,redirect
from projectapp.models import RecordE,RecordR,CategoryE,CategoryR
from projectapp.forms import addcategoryF,delselect
# Create your views here.
def recordall_and_cashflow(request):
    recordE=RecordE.objects.all()
    recordR=RecordR.objects.all()
    
    recordAllE=RecordE.objects.filter()
    recordAllR=RecordR.objects.filter()
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

