from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class UserCustomer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    Country = models.CharField(max_length=100)
    ZipCode = models.CharField(max_length=12)
    phoneNo = models.CharField(max_length=100) 
    creditCard = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username

class Stocks(models.Model):
    Symbol = models.CharField(max_length=100)
    Company = models.CharField(max_length=100)
    Price = models.CharField(max_length=100)
    Currency = models.CharField(max_length=100)
    Open = models.CharField(max_length=100)
    Close = models.CharField(max_length=100)
    High = models.CharField(max_length=100)
    Low = models.CharField(max_length=100)
    DayChange = models.CharField(max_length=100)
    StockExchange = models.CharField(max_length=100)
    Date = models.DateField(auto_now=True)

class Purchased(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    identifier = models.CharField(max_length=100)
    Quantity = models.CharField(max_length=100)
    Investment = models.CharField(max_length=100)
    Date = models.DateField(auto_now=True)

class Currency(models.Model):
    Name = models.CharField(max_length=100)
    Base = models.CharField(max_length=100)
    Price = models.CharField(max_length=100)
    Date = models.DateField(auto_now=True)