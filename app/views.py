from django.shortcuts import render

# Create your views here.

from app.models import *
from app.serializers import *
from rest_framework.response import Response
#from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes




@api_view()
def EmployeeJData(request):
    EQS=Employee.objects.all()#LOEO
    EJD=EmployeeSerializer(EQS,many=True)
    return Response(EJD.data)