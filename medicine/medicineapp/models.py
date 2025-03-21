from django.db import models
from employee.models import Employee
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name

class Medicine(models.Model):

    name = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    unit_price = models.IntegerField()
    pack_size = models.IntegerField()
    total_pack = models.IntegerField()
    status = models.CharField(max_length=30,choices=(('AVAILABLE','Available'),('OUTOFSTOCK','Out of Stock')))
    def __str__(self):
        return self.name

class MedicineStock(models.Model):
    medicine_name = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    total_pack = models.IntegerField()
    purchase_price = models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return self.medicine_name

class Order(models.Model):
    order_no = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=10)
    customer_email = models.CharField(max_length=100)
    medicine_name = models.ForeignKey(Medicine,on_delete=models.CASCADE)
    total_pack = models.IntegerField()
    order_amount = models.IntegerField()
    order_date = models.DateField()
    ordered_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    def __str__(self):
        return self.order_no