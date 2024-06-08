from django.shortcuts import render
from . models import Quotes
import random
# Create your views here.
def index(request):
    all_quotes = Quotes.objects.all()


    random_quote = random.choice(all_quotes)
    return render(request,'index.html',{'quote': random_quote})

# def quotes(request):
#     quotes=Quotes.objects.all()
#
#     return render(request)

def search_quotes(request):
    if 'author' in request.GET:
        author_name = request.GET['author']
        # Perform case-insensitive search for quotes by author name
        quotes = Quotes.objects.filter(author__icontains=author_name)
    else:
        quotes = []

    return render(request, 'search.html', {'quotes': quotes})