from tkinter import Place

from django.shortcuts import render,redirect
from myapp.models import EmployeeDb

# Create your views here.

def employee_page(request):
    return render(request,"employee.html")
def save_empoyee_page(request):
    if request.method=="POST":
        na=request.POST.get('name')
        ag=request.POST.get('age')
        pl=request.POST.get('place')
    obj=EmployeeDb(Name=na,Age=ag,Place=pl)
    obj.save()
    return redirect(employee_page)

def display_page(request):
    data=EmployeeDb.objects.all()
    return render(request,"display_page.html",{'data':data})

def edit_page(request,empid):
    data=EmployeeDb.objects.get(id=empid)
    return render(request,"edit.html",{'data':data})

def update_page(request,upid):
    if request.method=="POST":
        na=request.POST.get('name')
        ag=request.POST.get('age')
        pl=request.POST.get('place')
    EmployeeDb.objects.filter(id=upid).update(Name=na,Age=ag,Place=pl)
    return redirect(display_page)
def delete_page(request,del_id):
    x=EmployeeDb.objects.filter(id=del_id).delete()
    return redirect(display_page)
