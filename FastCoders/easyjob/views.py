from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from django.core.files.storage import FileSystemStorage
from .models import Profile



# Create your views here.

def Company(request):
    return render(request,'company.html')

def Applicant(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs= FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
    return render(request,'profile.html')
    
def profile_list(request):
    profiles= Profile.object.all()
    return render(request,'profile.html',{'profiles' : profile_list})
   

def upload_profile(request):
     return render(request,'profile.html')


def Firstpage(request):
    return render(request,'index.html')

