
from django.urls import path
from myapp import views


urlpatterns = [
    path('',views.employee_page,name="employee_page"),
    path('save_empoyee_page/',views.save_empoyee_page,name="save_employee_page"),
    path('display_page/', views.display_page, name="display_page"),
    path('edit_page/<int:empid>/', views.edit_page, name="edit_page"),
    path('update_page/<int:upid>/', views.update_page, name="update_page"),
    path('delete_page/<int:del_id>/', views.delete_page, name="delete_page"),
]
