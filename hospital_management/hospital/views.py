from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import BookingForm

from .models import Department,Doctor,Slider,About
# Create your views here.
def index(request):
    sliders=Slider.objects.all()
    
    context={
        'sliders':sliders, 
    }
    
    return render(request, 'index.html',context)

def about(request):
    content=About.objects.all()
    con={
        'content':content
    }
    return render(request,"about.html",con)

def booking(request):
    if request.method == "POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,"booking.html",dict_form)

def doctors(request):
    dict_docs={
        'doctors':Doctor.objects.all()
    }
    return render(request,"doctors.html" ,dict_docs)

def contact(request):
    return render(request,"contact.html",)

def department(request):
    dict_dept={
        'dept':Department.objects.all()
    }
    return render(request,"department.html",dict_dept)
