from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
# def index(request):
# return HttpResponse("Hello world.")


class HomeView(TemplateView):
    template_name = 'home.html'
