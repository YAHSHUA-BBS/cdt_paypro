from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
import csv

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def tax_checking(request):
    # Add your logic here
    return render(request, 'tax_checking.html')

def headcount_checking(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Please upload a CSV file.')
            return render(request, 'headcount_checking.html')
        
        # Add your CSV processing logic here
        
    return render(request, 'headcount_checking.html')