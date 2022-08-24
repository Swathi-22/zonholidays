from django.shortcuts import render

# Create your views here.

def index(request):
    context = {

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
    context = {

    }
    return render(request,'web/gallary.html',context)



def contact(request):
    context = {

    }
    return render(request,'web/contact.html',context)