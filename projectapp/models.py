from django.db import models

# Create your models here.
from django.db import models

from django.db.models import CharField,DateField,ForeignKey,IntegerField,EmailField

# Create your models here.
# BALANCE_TYPE = ((u'收入',u'收入'),(u'支出',u'支出'))	#元組 tuple：可以視為不可改變的串列 ((key,value),(key,value))

class CategoryE(models.Model):
    category = CharField(max_length=20)
    
    def __str__(self) :
        return self.category


class CategoryR(models.Model):
    category = CharField(max_length=20)
    
    def __str__(self) :
        return self.category

class Record_E(models.Model):
    date 	= DateField()
    description = CharField(max_length=300,null=True)
    categoryE 	= CharField(max_length=50)	#外來鍵是一個(或數個)指向另外一個表格主鍵的欄位。
    cash 	= IntegerField()
    def __str__(self) :
            return self.description
class Record_R(models.Model):
    date 	= DateField()
    description = CharField(max_length=300,null=True)
    categoryR 	= CharField(max_length=50)#外來鍵是一個(或數個)指向另外一個表格主鍵的欄位。
    cash 	= IntegerField()
    def __str__(self) :
            return self.description
class login_1(models.Model):
     cName= CharField(max_length=8,null=False)
     password=CharField(max_length=50,null=False)
     cEmail=EmailField(max_length=100)
     def __str__(self):
          return self.cName
