from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from . models import Employee
from . serializers import EmployeeSerializer
from rest_framework.views import APIView


class ListEmployeeAPIView(APIView):
    def get(self,request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

class EmployeeDetailAPIView(APIView):
    def get(self,request,pk):
        employees = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(employees, many=False)
        return Response(serializer.data)

class CreateEmployeeAPIView(APIView):
    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class UpdateEmployeeAPIView(APIView):
    def post(self,request,pk):
        employee = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(instance=employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class DeleteEmployeeAPIView(APIView):
    def get(self,request,pk):
        employee = Employee.objects.get(id=pk)
        employee_instance = Employee.objects.get(id=pk)
        employee_instance.delete()
        return Response('Deleted')