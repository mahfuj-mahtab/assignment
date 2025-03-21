
from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path("login/", employeeLogin,name = 'employee-login'),
    path("dashboard/", employeeDashboard,name = 'employee-dashboard'),
    path("dashboard/categories", AllCategories,name = 'category'),
    path("dashboard/category/add/", AddCategory,name = 'add_category'),
    path("dashboard/category/delete/<int:c_id>/", DeleteCategory,name = 'delete_category'),
    path("dashboard/medicines", AllMedicine,name = 'medicine'),
    path("dashboard/medicine/add/", AddMedicine,name = 'add_medicine'),
    path("dashboard/medicine/delete/<int:m_id>/", DeleteMedicine,name = 'delete_medicine'),
    path("dashboard/medicines/stocks", AllMedicineStock,name = 'medicine_stock'),
    path("dashboard/medicines/low-stocks", AllLowStocks,name = 'low_stocks'),
    path("dashboard/orders", AllOrders,name = 'order'),
    path("dashboard/order/add/", AddOrder,name = 'add_order'),
]
