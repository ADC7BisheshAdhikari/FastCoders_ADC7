
from django.urls import path
from .views import *

urlpatterns =[
    path('company/',company),
    path('applicant/',applicant),
    path('firstpage/',firstPage),

]

