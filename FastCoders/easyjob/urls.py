from django.contrib import admin  
from django.urls import path  
from easyjob import views  
from .views import *

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('company/', views.emp, name="company" ),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
] 


urlpatterns += [
    path('applicant/',applicant, name="applicant"),
    path('index/',firstPage, name="index"),
    path('login/',login, name="login"),
    path('search/',search, name="search")


]

