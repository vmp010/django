from django.shortcuts import render,redirect
from projectapp.models import RecordE,RecordR,CategoryE,CategoryR
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