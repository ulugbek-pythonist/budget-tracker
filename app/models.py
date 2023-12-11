import decimal
from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Wallet(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=15,decimal_places=2,default=decimal.Decimal(0))


class Income(models.Model):
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE)
    source = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=15,decimal_places=2)
    date_operation = models.DateTimeField(auto_now_add=True)


class Expense(models.Model):
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE)
    destination = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=15,decimal_places=2)
    date_operation = models.DateTimeField(auto_now_add=True)
