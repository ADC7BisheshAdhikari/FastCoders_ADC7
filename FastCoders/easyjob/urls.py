
from django.urls import path
from .views import *

urlpatterns =[
    path('company/',Company),
    path('applicant/',Applicant),
    path('firstpage/',Firstpage ),

]

