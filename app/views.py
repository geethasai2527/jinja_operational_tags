from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'name':'geethas','age':23}
    return render(request,'conditions.html',context=d)