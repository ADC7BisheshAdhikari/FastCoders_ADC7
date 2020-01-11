
from django.urls import path
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns =[
    path('company/',Company),
    path('applicant/',Applicant),
    path('firstpage/',Firstpage ),
    path('profilelist/', views.profile_list),
    path('profilelist/upload', views.upload_profile),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

