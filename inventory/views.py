from django.shortcuts import render

def home(request):
    hello = "Hi"
    return render(request, 'inventory/main.html', {'hello':hello})
