from django.shortcuts import render
from django.http import HttpResponse

def show_form(request):
    return render(request, 'form.html')

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        # Ma'lumotlarni olish
        return HttpResponse(f'Ism: {name}, Email: {email}')
    else:
        return HttpResponse('Noto\'g\'ri so\'rov turi!')
