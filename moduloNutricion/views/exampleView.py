from django.shortcuts import render, request, redirect
class Nutriologo(View):
    def get(self, request):
        return render(request, 'pruebaNutri.html')