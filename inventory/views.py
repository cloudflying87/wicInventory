from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def login_user(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('checkout')
        else:
            messages.success(request, "Incorrect username or password.")
            return redirect('/')

    else:
        return render(request, 'inventory/signin.html', {})

def checkout(request):
    hello = "Hi"
    title= "Checkout WIC Supplies"
    return render(request, 'inventory/checkout.html', {'title':title,'hello':hello})

def report(request):
    hello = "Report"
    title= "Report"
    return render(request, 'inventory/report.html', {'title':title,'hello':hello})



def logout_user(request):
    logout(request)
    messages.success(request, "You logged out successfully")
    return redirect('/')
