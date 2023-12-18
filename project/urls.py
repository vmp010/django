"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from projectapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.recordall_and_cashflow,name='index'),
    path('addcategory/',views.addcategory),
    path('delcategory/',views.delcategory),
    path('addErecord/',views.addErecord),
    path('addRrecord/',views.addRrecord),
    path('',views.loginpage,name='login'),
    path('registe/',views.registe),
   


    path('delRr/<int:pk>',views.delRr,name='delRr'), #刪除收入紀錄
    path('delEr/<int:pk>',views.delEr,name='delEr'), #刪除支出紀錄
    path('editRr/<int:pk>',views.editRr,name='editRr'), #編輯收入紀錄
    path('editEr/<int:pk>',views.editEr,name='editEr'), #編輯支出紀錄


]
