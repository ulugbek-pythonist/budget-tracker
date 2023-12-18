import decimal
from django.db import models

from django.contrib.auth.models import User



class Wallet(models.Model):
    owner = models.OneToOneField(User,on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=15,decimal_places=2,default=decimal.Decimal(0))

    def __str__(self) -> str:
        return self.owner.get_username()
    
    def income(self,amount):
        self.balance = self.balance + amount

    def expense(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False


class Income(models.Model):
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE)
    source = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=15,decimal_places=2)
    date_operation = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.wallet.owner.get_username()


class Expense(models.Model):
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE)
    destination = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=15,decimal_places=2)
    date_operation = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.wallet.owner.get_username()
    

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(null=True,blank=True,upload_to='profiles/')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True,null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)