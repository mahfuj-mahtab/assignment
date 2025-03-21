from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import *
from medicineapp.models import *
# Create your views here.
def employeeLogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            existedUser = Employee.objects.get(email = email)
            if(existedUser):
                user = authenticate(request, username=existedUser.username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('employee-dashboard')
                else:
                    return render(request,'sign-in.html')

        except Employee.DoesNotExist:
            return render(request,'sign-in.html')
    return render(request,'sign-in.html')

def employeeDashboard(request):
    if(request.user.is_authenticated):
        return render(request,'index.html')
    return render(request,'sign-in.html')
def AllCategories(request):
    if(request.user.is_authenticated):
        categories = Category.objects.filter()
        return render(request,'category.html',{'categories' : categories})
    return render(request,'sign-in.html')
def AddCategory(request):
    if(request.user.is_authenticated):
        if(request.method == 'POST'):
            category = request.POST.get('category')
           
            if(category):
                new_category = Category(category_name = category)
                new_category.save()
                return redirect('category')
        return render(request,'add-medicine-category.html')
    return render(request,'sign-in.html')
def DeleteCategory(request,c_id):
    if(request.user.is_authenticated):
        if(request.method == 'POST'):
            category = Category.objects.get(id = c_id)
            category.delete()
            return redirect('category')
        return render(request,'add-medicine-category.html')
    return render(request,'sign-in.html')
def AllMedicine(request):
    if(request.user.is_authenticated):
        medicine = Medicine.objects.all()
        return render(request,'medicine.html',{'medicines' : medicine})
    return render(request,'sign-in.html')
def AddMedicine(request):
    if(request.user.is_authenticated):
        if(request.method == 'POST'):
            name = request.POST['name']
            brand_name = request.POST['brand_name']
            category = request.POST['category']
            pack_size = request.POST['pack_size']
            unit_price = request.POST['unit_price']
            total_pack = request.POST['total_pack']

           
            if(category and name and brand_name and pack_size and unit_price and total_pack):
                cat = Category(id = category)
                new_medicine = Medicine(name = name,brand_name = brand_name,category = cat,pack_size = pack_size,unit_price = unit_price, total_pack = total_pack)
                new_medicine.save()
                return redirect('medicine')
            else:
                return render(request,'add-medicine.html')
        category = Category.objects.all()
        return render(request,'add-medicine.html',{'categories' : category})
    return render(request,'sign-in.html')

def DeleteMedicine(request,m_id):
    if(request.user.is_authenticated):
        medicine = Medicine.objects.get(id = m_id)
        medicine.delete()
        return redirect('medicine')
    return render(request,'sign-in.html')
def AllMedicineStock(request):
    if(request.user.is_authenticated):
        medicine_stocks = MedicineStock.objects.all()
        return render(request,'medicine-stock.html',{'medicine_stocks' : medicine_stocks})
    return render(request,'sign-in.html')
def AllLowStocks(request):
    if(request.user.is_authenticated):
        medicines = Medicine.objects.filter(total_pack__lt = 11)
        return render(request,'low-stocks.html',{'medicines' : medicines})
    return render(request,'sign-in.html')
def AllOrders(request):
    if(request.user.is_authenticated):
        orders = Order.objects.filter()
        return render(request,'order.html',{'orders' : orders})
    return render(request,'sign-in.html')
def AddOrder(request):
    if(request.user.is_authenticated):
        if(request.method == 'POST'):
            order_no = 'abc'
            customer_name = request.POST['customer_name']
            customer_phone = request.POST['customer_phone']
            customer_email = request.POST['customer_email']
            medicine_name = request.POST['medicine_name']
            total_pack = request.POST['total_pack']
            order_amount = request.POST['order_amount']
            order_date = request.POST['order_date']
            ordered_by = request.POST['ordered_by']
            new_order = Order(order_no = order_no,customer_name = customer_name,customer_phone = customer_phone,customer_email = customer_email,medicine_name = medicine_name,total_pack = total_pack,order_amount = order_amount,order_date = order_date,ordered_by = ordered_by)
            new_order.save()
            return redirect('order')
        medicine = Medicine.objects.all()
        employee = Employee.objects.all()
        return render(request,'add-order.html',{'medicines' : medicine,'employees' : employee})
    return render(request,'sign-in.html')