from django.shortcuts import render
from .models import Gallery,FindPackage
from .forms import ContactForm
from django.http import HttpResponse
import json

# Create your views here.

def index(request):
    find_package=FindPackage.objects.all()
    gallery=Gallery.objects.all()
    forms = ContactForm(request.POST or None)
    if request.method == 'POST':
        if forms.is_valid():
            data = forms.save(commit=False)
            data.referral = "web"
            data.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully submitted"
            }
        else:
            response_data = {
                "status": "false",
                "title": "Form validation error",
                "message": repr(forms.errors)
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "find_package":find_package,
            "forms":forms,
            "gallery":gallery
        }
    return render(request,'web/index.html',context)



def about(request):
    context = {

    }
    return render(request,'web/about.html',context)



def packages(request):
    context = {

    }
    return render(request,'web/packages.html',context)



def packageDetails(request):
    context = {

    }
    return render(request,'web/package-details.html',context)



def gallery(request):
    gallery=Gallery.objects.all()
    context = {
        "gallery":gallery
    }
    return render(request,'web/gallary.html',context)



def contact(request):
    forms = ContactForm(request.POST or None)
    if request.method == 'POST':
        if forms.is_valid():
            data = forms.save(commit=False)
            data.referral = "web"
            data.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully submitted"
            }
        else:
            response_data = {
                "status": "false",
                "title": "Form validation error",
                "message": repr(forms.errors)
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "forms":forms
        } 
        return render(request,'web/contact.html',context)