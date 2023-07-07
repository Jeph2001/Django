from django.db import models


# Create your models here.
class Collecting(models.Model):
    full_name = models.CharField(null=False, max_length=100)
    phone_number = models.CharField(max_length=20)
    marital_status = models.CharField(max_length=10, default='single')
    location = models.CharField(max_length=20, default='Kigali or other')
    status = models.CharField(max_length=50, default='employed or student or unemployed')
    email = models.EmailField(max_length=100)
    email_password = models.CharField(max_length=100)




    

