from django.shortcuts import render
from datetime import datetime
from Home.models import Contact  # Ensure this model is correctly imported
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        "variable": "This is "
    }
    
    return render(request, 'home/index.html', context)

def services(request):
    return render(request, 'services.html')

def service_details(request, service_name):
    # Return the service name for testing purposes
    return render(request, 'service_details.html', {'service_name': service_name})

def about(request):
   #return HttpResponse("This is about page")
    return render(request, 'about.html')

def contact(request):
    # return HttpResponse("This is contact page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        contact = Contact(name=name, email=email, phone=phone, desc=desc, datetime=datetime.today())  
        contact.save()  # Fixed the error here
        messages.success(request, "Your message has been sent successfully!")
        
    return render(request, 'contact.html')

def home(request):  # Renamed function to lowercase
    return render(request, 'home/index.html')  # Render your homepage template here


def pricing(request):
    return render(request, 'home/pricing.html')