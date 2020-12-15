from django.urls import path
from . import views
app_name = 'employee_app'


urlpatterns = [
    path('', views.SaveEmpView.as_view(), name='save-employee'),
    path('update-employee/<emp_id>/', views.update_emp, name='update_emp'),
    path('update-employee-save/<emp_id>/', views.save_update_emp, name='update_emp_save'),
    path('delete-employee/<emp_id>/', views.delete_emp, name='delete-employee'),
]

