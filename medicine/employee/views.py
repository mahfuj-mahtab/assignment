from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import *
from medicineapp.models import *
import datetime
# Create your views here.
def employeeLogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            existedUser = Employee.objects.get(email = email)
            print(existedUser.password)
            if(existedUser):
                user = authenticate(request, username=existedUser.username, password=password)
                print(user)
                if user is not None:
                    print('kk')
                    login(request, user)
                    print('hh')
                    return redirect('employee-dashboard')
                else:
                    return render(request,'sign-in.html')

        except Employee.DoesNotExist:
            return render(request,'sign-in.html')
    return render(request,'sign-in.html')
def employeeRegister(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        role = 'ADMIN'
        password = request.POST['password']
        
        employee = Employee(first_name = first_name,last_name = last_name,email = email,phone = 1234567890,role = role,address = '',salary = 15000,image = '',username = email.split('@')[0],password = password)
        employee.save()
        return redirect('employee-dashboard')
    return render(request,'sign-up.html')
def EditEmployee(request,e_id):
    if(request.user.is_authenticated):
        employee = Employee.objects.get(id = e_id)
        if(request.method == 'POST'):
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            phone = request.POST['phone']
            role = request.POST['role']
            image = request.FILES['image']
            employee.first_name = first_name
            employee.last_name = last_name
            employee.email = email
            employee.phone = phone
            employee.role = role
            employee.image = image
            employee.save()
            return redirect('employee')
        return render(request,'edit-employee.html',{'employee' : employee})
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
    import random
    if(request.user.is_authenticated):
        if(request.method == 'POST'):
           
            customer_name = request.POST['customer_name']
            customer_phone = request.POST['customer_phone']
            customer_email = request.POST['customer_email']
            medicine_name = request.POST['medicine_name']
            total_pack = int(request.POST['total_pack'])
            
            ordered_by = request.POST['employee']
            medicine = Medicine.objects.get(id = medicine_name)
            employee = Employee.objects.get(id = ordered_by)
            customer = Customer.objects.filter(email = customer_email).first()
            if(customer is None):
                new_customer = Customer(customer_name = customer_name,customer_address = '',email = customer_email,customer_phone = customer_phone)
                new_customer.save()
            amount = medicine.unit_price * total_pack
            num = random.randint(1000,9999)
            order_no = 'ORD'+str(num)
            new_order = Order(order_no = order_no,customer_name = customer_name,customer_phone = customer_phone,customer_email = customer_email,medicine_name = medicine,total_pack = total_pack,order_amount = amount,order_date = datetime.datetime.now().date(),ordered_by = employee)
            new_order.save()
            return redirect('order')
        medicine = Medicine.objects.all()
        employee = Employee.objects.all()
        return render(request,'add-order.html',{'medicines' : medicine,'employees' : employee})
    return render(request,'sign-in.html')


def DeleteOrder(request,o_id):
    if(request.user.is_authenticated):
        order = Order.objects.get(id = o_id)
        order.delete()
        return redirect('order')
    return render(request,'sign-in.html')

def AllEmployees(request):
    if(request.user.is_authenticated):
        employees = Employee.objects.filter()
        return render(request,'employee.html',{'employees' : employees})
    return render(request,'sign-in.html')
def AddEmployee(request):
    if(request.user.is_authenticated):
        if(request.method == 'POST'):
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            address = request.POST['address']
            phone = request.POST['phone']
            role = request.POST['role']
            image = request.FILES['image']
            employee = Employee(first_name = first_name,last_name = last_name,email = email,phone = phone,role = role,address = address,salary = 15000,image = image,username = email.split('@')[0])
            employee.save()
            return redirect('employee')
        return render(request,'add-employee.html')
    return render(request,'sign-in.html')
def DeleteEmployee(request,e_id):
    if(request.user.is_authenticated):
        employee = Employee.objects.get(id = e_id)
        employee.delete()
        return redirect('employee')
    return render(request,'sign-in.html')

def AllCustomers(request):
    if(request.user.is_authenticated):
        customers = Customer.objects.filter()
        return render(request,'customer.html',{'customers' : customers})
    return render(request,'sign-in.html')
def AddCustomer(request):
    if(request.user.is_authenticated):
        if(request.method == 'POST'):
            customer_name = request.POST['customer_name']
            customer_phone = request.POST['customer_phone']
            customer_address = request.POST['customer_address']
            email = request.POST['customer_email']
            customer = Customer(customer_name = customer_name,customer_address = customer_address,email = email,customer_phone = customer_phone)
            customer.save()
            return redirect('customer')
        return render(request,'add-customer.html')
    return render(request,'sign-in.html')
def EditCustomer(request,c_id):
    if(request.user.is_authenticated):
        customer = Customer.objects.get(id = c_id)
        if(request.method == 'POST'):
            customer_name = request.POST['customer_name']
            customer_phone = request.POST['customer_phone']
            customer_address = request.POST['customer_address']
            email = request.POST['customer_email']
            customer.customer_name = customer_name
            customer.customer_phone = customer_phone
            customer.customer_address = customer_address
            customer.email = email
            customer.save()
            return redirect('customer')
        return render(request,'edit-customer.html',{'customer':customer})
def DeleteCustomer(request,c_id):
    if(request.user.is_authenticated):
        customer = Customer.objects.get(id = c_id)
        customer.delete()
        return redirect('customer')
    return render(request,'sign-in.html')