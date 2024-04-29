
from django.shortcuts import render
from shop.models import Books

# Create your views here.
def home(request):
    books=Books.objects.all()
    print(books)
    return render(request,'home.html',{'books':books})

def cart(request):

    return render(request,'cart.html')