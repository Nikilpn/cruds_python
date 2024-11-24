from django.shortcuts import render,redirect
from Empapp.models import Employeedb

# Create your views here.
def employee_page(request):
    return render(request,"employee.html")
def save_employee_page(request):
    if request.method=="POST":
        na=request.POST.get('e-name')
        ag=request.POST.get('e-age')
        mob=request.POST.get('e-mobile')
        em=request.POST.get('e-email')
        dept=request.POST.get('e-department')
        obj=Employeedb(NAME=na,AGE=ag,MOBILE=mob,EMAILID=em,DEPARTMENT=dept)
        obj.save()
        return redirect(employee_page)
def display_employee_page(request):
    data=Employeedb.objects.all()
    return render(request,"display_employee.html",{'data':data})
def edit_employee_page(request,emp_id):
    data=Employeedb.objects.get(id=emp_id)
    return render(request,"employee_edit.html",{'data':data})

def update_employee(request,emp_id):
    if request.method=="POST":
        na = request.POST.get('e-name')
        ag = request.POST.get('e-age')
        mob = request.POST.get('e-mobile')
        em = request.POST.get('e-email')
        dept = request.POST.get('e-department')
        obj = Employeedb.objects.filter(id=emp_id).update(NAME=na,AGE=ag,MOBILE=mob,EMAILID=em,DEPARTMENT=dept)
        return redirect(display_employee_page)
def delete_emp(request,emp_id):
    x=Employeedb.objects.filter(id=emp_id)
    x.delete()
    return redirect(display_employee_page)