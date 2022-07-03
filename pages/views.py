""" View file for the Pages app """
# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    '''View for the Home page route'''
    return render(request, 'pages/home.html')


def about(request):
    '''View for the About page route'''
    return render(request, 'pages/about.html')
