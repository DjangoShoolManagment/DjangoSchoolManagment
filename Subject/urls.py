from django.urls import path
from . import views

urlpatterns = [
     path('AllSubject/', views.subjects, name='AllSubject'),

]