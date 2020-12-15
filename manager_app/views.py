from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic.base import View
from employee_app.forms import EmployeeRegForm

from .models import Users


class Home(View):
    def get(self, request):
        employee_form = EmployeeRegForm(request.POST or None)
        employee_data = Users.objects.filter(is_employee=True).all()
        update_emp_form = EmployeeRegForm(request.POST or None)
        paginator = Paginator(employee_data, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'employee_form': employee_form,
            'employee_data': page_obj,
            'update_emp_form': update_emp_form,
        }
        return render(request, "home.html", context)
