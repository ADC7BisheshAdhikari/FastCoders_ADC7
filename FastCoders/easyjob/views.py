from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from django.core.files.storage import FileSystemStorage




# Create your views here.

def company(request):
    return render(request,'company.html')

def applicant(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs= FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
    return render(request,'registerform.html')

def firstPage(request):
    return render(request,'index.html')
