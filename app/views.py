from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'name':'geetha','age':12}
    return render(request,'conditions.html',context=d)