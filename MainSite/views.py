from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def personal_first(request):
    return render(request, 'MainSite/index.html', {})

def programming(request):
    return render(request, 'MainSite/programming.html', {})

def construction(request):
    return render(request, 'MainSite/under_construction.html', {})



