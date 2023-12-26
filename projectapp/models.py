from django.db import models

# Create your models here.
from django.db import models

from django.db.models import CharField,DateField,ForeignKey,IntegerField,EmailField
from datetime import datetime,timedelta

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

class Record_E1(models.Model):
    user=ForeignKey('login_1',on_delete=models.CASCADE,null=True)
    date 	= DateField()
    description = CharField(max_length=300,null=True)
    categoryE 	= CharField(max_length=50)	
    cash 	= IntegerField()
    is_settled = models.BooleanField(default=False)  # 新增用來標記是否已經結算的欄位
    def __str__(self) :
            return self.description
    @classmethod
    def monthly_settlementR(cls):
        today = datetime.now()
        first_day_of_this_month = today.replace(day=1)  # 現在這個月的第一天
        last_day_of_last_month = first_day_of_this_month - timedelta(days=1)  # 上個月的最後一天

        if today.day == 1:  # 如果是每月的第一天
            with transaction.atomic():  # 使用交易以確保資料一致性
                # 找到需要結算的交易資料，設定結算條件為上個月的所有資料
                transactions_to_settle = cls.objects.filter(created_at__range=(last_day_of_last_month.replace(day=1), last_day_of_last_month))

                # 將找到的交易設為已結算
                for transaction in transactions_to_settle:
                    transaction.is_settled = True
                    transaction.save()

            # 返回未結算的交易資料，這邊返回的是上個月的未結算交易資料
            unsettled_transactions = cls.objects.filter(is_settled=False, created_at__range=(last_day_of_last_month.replace(day=1), last_day_of_last_month))
            return unsettled_transactions
        else:
            return cls.objects.none()  # 如果不是每月的第一天，返回空查詢集合

class login_1(models.Model):
     cName= CharField(max_length=8,null=False)
     password=CharField(max_length=50,null=False)
     cEmail=EmailField(max_length=100)
     def __str__(self):
          return self.cName
class Record_R1(models.Model):
    user=ForeignKey(login_1,on_delete=models.CASCADE,null=True)
    date 	= DateField()
    description = CharField(max_length=300,null=True)
    categoryR 	= CharField(max_length=50)
    cash 	= IntegerField()
    is_settled = models.BooleanField(default=False)  # 新增用來標記是否已經結算的欄位
    def __str__(self) :
            return self.description
    @classmethod
    def monthly_settlementR(cls):
        today = datetime.now()
        first_day_of_this_month = today.replace(day=1)  # 現在這個月的第一天
        last_day_of_last_month = first_day_of_this_month - timedelta(days=1)  # 上個月的最後一天

        if today.day == 1:  # 如果是每月的第一天
            with transaction.atomic():  # 使用交易以確保資料一致性
                # 找到需要結算的交易資料，設定結算條件為上個月的所有資料
                transactions_to_settle = cls.objects.filter(created_at__range=(last_day_of_last_month.replace(day=1), last_day_of_last_month))

                # 將找到的交易設為已結算
                for transaction in transactions_to_settle:
                    transaction.is_settled = True
                    transaction.save()

            # 返回未結算的交易資料，這邊返回的是上個月的未結算交易資料
            unsettled_transactions = cls.objects.filter(is_settled=False, created_at__range=(last_day_of_last_month.replace(day=1), last_day_of_last_month))
            return unsettled_transactions
        else:
            return cls.objects.none()  # 如果不是每月的第一天，返回空查詢集合
    



