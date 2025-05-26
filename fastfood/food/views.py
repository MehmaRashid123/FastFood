from django.shortcuts import render
from .models import MenuItem
from .models import Deal
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html') 

def menu(request):
    items = MenuItem.objects.filter(is_available=True)
    return render(request, 'menu.html', {'items': items})

def deals_view(request):
    deals = Deal.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'deals.html', {'deals': deals})

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Optional: process or save message here
        messages.success(request, "Your message has been sent!")
    
    return render(request, 'contact.html')