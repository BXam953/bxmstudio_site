from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def home(request, *args, **kwargs):
    body = request.body
    return JsonResponse({'message':'Hello World'})