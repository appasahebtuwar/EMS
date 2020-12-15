
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_GET
from employee_app.forms import EmployeeRegForm
from manager_app.models import Users
from django.views.generic.base import View

class SaveEmpView(View):
    def post(self, request, *args, **kwargs):
        signup_form = EmployeeRegForm(request.POST)
        password = request.POST.get('password')
        if signup_form.is_valid():
            instance = signup_form.save(commit=False)
            instance.set_password(password)
            instance.is_employee = True
            instance.save()
            messages.success(request, 'Account Created successfully.')
            return redirect('/home/')
        else:
            print(signup_form.errors)
            signup_form = EmployeeRegForm(request.POST)
            context = {
                'employee_form': signup_form
            }
            return render(request, 'home.html', context)

@require_GET
def update_emp(request, emp_id=None):
    employee_form = EmployeeRegForm(request.POST or None)
    employee_data = Users.objects.filter(is_employee=True)
    emp_obj = get_object_or_404(Users, id=emp_id)
    update_emp_form = EmployeeRegForm(request.POST or None, instance=emp_obj)

    context = {
        'update_emp_form': update_emp_form,
        'employee_form': employee_form,
        'employee': employee_data,
        'emp_obj': emp_obj
    }
    return render(request, 'home.html', context)

@require_POST
def save_update_emp(request, emp_id=None):
    emp_obj = get_object_or_404(Users, id=emp_id)
    update_emp_form = EmployeeRegForm(request.POST or None, instance=emp_obj)
    employee_form = EmployeeRegForm(request.POST or None)
    employee_data = Users.objects.filter(is_employee=True)

    if update_emp_form.is_valid():
        update_emp_form.save()
        messages.success(request, 'Employee updated.')
        return redirect('/home')
    else:
        print(update_emp_form.errors)
        context = {
            'update_emp_form': update_emp_form,
            'employee_form': employee_form,
            'employee': employee_data,
        }
        return render(request, 'home.html', context)


@require_GET
def delete_emp(request, emp_id=None):
    emp_obj = Users.objects.get(id=emp_id)
    emp_obj.delete()
    messages.success(request, 'Employee deleted.')
    return redirect('/home/')
