from django.urls import path,include
from . import views
urlpatterns = [
    path('healthyfood/',views.process_image, name= "process_image")
]