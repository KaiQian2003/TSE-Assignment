from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .forms import DeliveryDriverRegistrationForm

from django.contrib.auth.decorators import login_required

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        return(redirect('/menu'))
    else:
        return render(
            request,
            'app/index.html',
            {
                'title':'Home Page',
                'year': datetime.now().year,
            }
        )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Dr. Yeoh.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'ABC System',
            'message':'This application processes ...',
            'year':datetime.now().year,
        }
    )

@login_required
def menu(request):
    check_employee = request.user.groups.filter(name='employee').exists()

    context = {
            'title':'Main Menu',
            'is_employee': check_employee,
            'year':datetime.now().year,
        }
    context['user'] = request.user

    return render(request,'app/menu.html',context)

def deliverymenu(request):
    delivery_items = [
        {'name': 'Item 1', 'price': 10.99},
        {'name': 'Item 2', 'price': 8.49},
        {'name': 'Item 3', 'price': 12.99},
    ]

    context = {
        'title': 'Delivery Menu',
        'delivery_items': delivery_items,
        'year': datetime.now().year,
    }
    return render(request, 'app/delivery_menu.html', context)

def delivery_driver_registration(request):
    if request.method == 'POST':
        form = DeliveryDriverRegistrationForm(request.POST)
        if form.is_valid():
            # Save the form data to create a new delivery driver account
            form.save()
            # Redirect to a success page or back to the menu
            return redirect('menu')
    else:
        form = DeliveryDriverRegistrationForm()

    return render(request, 'app/delivery_driver_registration.html', {'form': form})
    