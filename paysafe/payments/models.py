from django.db import models

# Create your models here.
class UserInfo(models.Model):
    merchantCustomerId = models.CharField(primary_key=True, max_length=64)
    customerid = models.CharField(max_length=64)
    paymentToken = models.CharField(max_length=64)
    singleUsePaymentHandle = models.CharField(max_length=64)


