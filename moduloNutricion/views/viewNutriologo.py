from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
import json
class nutriologo(View):
    def get(self, request):
        
        return render(request, 'pruebaNutri.html')