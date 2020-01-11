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





def search1(request):
    if request.method=='POST'
        srch=request.POST['srh']


        if srch:
            match = Post.objects.filter(Q(name__icontains=srch))
        

            if match:
                return render(request,'company.html',{'sr':match}
            else:
                message.error(request,'no result found')
        else:
            return HttpResponseRedirect(/search1/)
    return render(request,'company.html')