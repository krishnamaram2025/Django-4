from django.shortcuts import render, redirect
# from .models import Employee
# from .forms import EmployeeForm
# from django.db.models import Q

def index(request):
    # employees = Employee.objects.all()
    # context = {
    #     'employees': employees
    # }
    return render(request, 'index.html')

def home(request):
    # employees = Employee.objects.all()
    # context = {
    #     'employees': employees
    # }
    return render(request, 'home.html')

def about(request):
    # employees = Employee.objects.all()
    # context = {
    #     'employees': employees
    # }
    return render(request, 'about.html')

def services(request):
    # employees = Employee.objects.all()
    # context = {
    #     'employees': employees
    # }
    return render(request, 'services.html')

def portfolio(request):
    # employees = Employee.objects.all()
    # context = {
    #     'employees': employees
    # }
    return render(request, 'portfolio.html')
def contact(request):
    # employees = Employee.objects.all()
    # context = {
    #     'employees': employees
    # }
    return render(request, 'contact.html')

