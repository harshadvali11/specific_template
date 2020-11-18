from django.shortcuts import render

# Create your views here.

# content of views.py file
def first(request):
    return render(request,'app1/first.html',context={'name':'Ashu','age':2})