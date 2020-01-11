from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context


# Create your views here.
def Company(request):
    return render(request,'company.html')
def Applicant(request):
    return render(request,'registerform.html')
def Firstpage(request):
    return render(request,'index.html')
