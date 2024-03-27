from django.http import HttpResponse
from django.shortcuts import render
from.models import place
from.models import character

# Create your views here.
def demo(request):
     obj1=place.objects.all()
     obj2=character.objects.all()

     return render(request,"index.html",{'result':obj1,'value':obj2})


# def addition(request):
#        x=int( request.GET['num1'])
#        res=x+y
#        return render(request,"result.html",{'result':res})
