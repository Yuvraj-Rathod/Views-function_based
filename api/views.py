from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

#GET
@api_view(['GET'])
def hello_world(request):
    return Response({'msg':'hello world'})

#POST 
@api_view(['POST'])
def hello_world(request):
    if request.method == 'POST':
        print(request.data)
        return Response({'msg':'hello world'})
    
