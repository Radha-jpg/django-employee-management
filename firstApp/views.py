from django.shortcuts import render, redirect
from firstApp.models import Employee

def employeeView(request):
    data = Employee.objects.all()
    return render(request, 'employees.html', {'employees': data})


def addEmployeeView(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        sal = request.POST.get('sal')

        Employee.objects.create(id=id, name=name, sal=sal)
        return redirect('/firstApp/emps/')  # Redirect to employee list after adding

    return render(request, 'add_employee.html')
