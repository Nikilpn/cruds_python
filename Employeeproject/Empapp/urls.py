from django.urls import path
from Empapp import views
urlpatterns=[
    path('',views.employee_page,name="employee_page"),
    path('save_employee_page/',views.save_employee_page,name="save_employee_page"),
    path('display_employee_page/', views.display_employee_page, name="display_employee_page"),
    path('edit_employee_page/<int:emp_id>/', views.edit_employee_page, name="edit_employee_page"),
    path('update_employee/<int:emp_id>/', views.update_employee, name="update_employee"),
    path('delete_emp/<int:emp_id>/', views.delete_emp, name="delete_emp"),
]