
from django.shortcuts import *

from .forms import AppointmentForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contactus(request):
    return render(request, 'contactus.html')

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            # Display a success message
            messages.success(request, 'Appointment booked successfully!')
            # Redirect to a success page or render a template with the success message
            return redirect('success')  # Assuming you have a 'success' URL name
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form})