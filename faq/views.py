from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import Faq

class FaqView(View):
    def get(self, request):
        return HttpResponse('Hello')
    
    
