from django.shortcuts import render,redirect
from projectapp.models import RecordE,RecordR,CategoryE,CategoryR
# Create your views here.
def recordall(request):
    recordE=RecordE.objects.all()
    recordR=RecordR.objects.all()
    return render(request,"index.html",locals())