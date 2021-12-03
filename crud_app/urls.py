from django.urls import path
from . views import *

urlpatterns = [
    path('',ListEmployeeAPIView.as_view(),name='crud_app'),
    path('detail/<str:pk>/',EmployeeDetailAPIView.as_view(),name='detail'),
    path('create',CreateEmployeeAPIView.as_view(),name='create'),
    path('update/<str:pk>/',UpdateEmployeeAPIView.as_view(),name='update'),
    path('delete/<str:pk>/',DeleteEmployeeAPIView.as_view(),name='delete'),
]