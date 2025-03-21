from django.db import models
from django.contrib.auth.models import User,AbstractUser,Group, Permission
# Create your models here.
class Employee(AbstractUser):
    role = (
    ('ADMIN','ADMIN'),
    ('MEDICINEMANAGER','MEDICINEMANAGER'),
    ('ORDERMANAGER','ORDERMANAGER'),
    ('CUSTOMER','CUSTOMER'),
    )
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    salary = models.IntegerField(null=True,blank=True)
    image = models.ImageField(upload_to='media/')
    role = models.CharField(choices=role,max_length=30)
    groups = models.ManyToManyField(Group, related_name="employee_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="employee_permissions", blank=True)
    def __str__(self):
        return self.username
    
class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=10)
    customer_address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.customer_name