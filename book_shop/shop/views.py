
from django.http import HttpResponse
from django.shortcuts import render
from .forms import Bookforms
from shop.models import Books

# Create your views here.
def home(request):
    books=Books.objects.all()
    print(books)
    return render(request,'home.html',{'books':books})

def cart(request):
    return render(request,'cart.html')

def book_register(request):
    if request.method =="POST":
        form=Bookforms(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Successfully Registerd")
        
    form=Bookforms()
    return render(request,'bookregister.html',{'form':form})
