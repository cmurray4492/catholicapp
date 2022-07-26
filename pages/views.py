""" View file for the Pages app """
# from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm


def home(request):
    '''View for the Home page route'''
    return render(request, 'pages/home.html')


def about(request):
    '''View for the About page route'''
    return render(request, 'pages/about.html')


def contact(request):
    '''View for the Contact Us page route'''
    return render(request, 'contact.html')


class signup(generic.CreateView):
    """Auth Sign Up Class"""
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'
