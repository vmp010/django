from django.shortcuts import render, HttpsResponse

# Create your views here.
def frontpage(request):
    return render(request,'app/index.html',{})