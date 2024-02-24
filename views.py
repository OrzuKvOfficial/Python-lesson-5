# views.py

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'calculator.html')

def calculate(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operation = request.POST['operation']

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                return HttpResponse('Error! Division by zero.')

        return render(request, 'calculator.html', {'result': result})

    return HttpResponse('Invalid request method.')
