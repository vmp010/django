from django.db import models

# Create your models here.
from django.db import models

from django.db.models import CharField,DateField,ForeignKey,IntegerField

# Create your models here.
BALANCE_TYPE = ((u'收入',u'收入'),(u'支出',u'支出'))	#元組 tuple：可以視為不可改變的串列 ((key,value),(key,value))

class Category(models.Model):
    category = CharField(max_length=20)
    
    def __str__(self) :
        return self.category

class Record(models.Model):
    date 	= DateField()
    description = CharField(max_length=300,null=True)
    category 	= ForeignKey(Category,on_delete=models.SET_NULL,null=True)	#外來鍵是一個(或數個)指向另外一個表格主鍵的欄位。
    cash 	= IntegerField()
    balance_type= CharField(max_length=2,choices=BALANCE_TYPE)	#收/支choices只有兩種，已定義在上方的BALANCE_TYPE