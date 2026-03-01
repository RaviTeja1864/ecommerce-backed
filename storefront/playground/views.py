from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from store import Product



def say_hello(request):

    query_set = Product.objects.all()

    for Product in query_set:
        print(Product)



    return render (request , 'hello.html',{'name':'ravi'})