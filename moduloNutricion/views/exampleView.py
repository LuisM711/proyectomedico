from django.shortcuts import render, redirect
from django.views import View
class nutriologo(View):
    def get(self, request):
        
        return render(request, 'pruebaNutri.html')