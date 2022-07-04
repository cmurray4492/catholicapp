"""Views file for Catholic App Members Sub App"""
# from django.http import HttpResponse
from django.shortcuts import render


def member_home(request):
    """Members home page should list all or set of members"""
    return render(request, 'members/member_home.html')


def member_profile(request):
    """Profile page for the current loged in member"""
    return render(request, 'members/member_profile.html')
