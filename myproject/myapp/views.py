from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm

# READ - Show all employees
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

# CREATE - Add new employee
def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})

# UPDATE - Edit employee
def employee_update(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})

# DELETE - Remove employee
def employee_delete(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee_confirm_delete.html', {'employee': employee})

