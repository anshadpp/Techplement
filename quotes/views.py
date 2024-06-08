from django.shortcuts import render
from . models import Quotes

# Create your views here.
def index(request):
    return render(request,'index.html')


def search(request):
    query=request.GET['search']
    author = Quotes.objects.filter(Q(place__icontains=query))
    return render(request,"search.html",locals())