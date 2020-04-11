from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, states_choices
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def index(request):
    listings_home = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings_home' : listings_home,
        'state_choices' : states_choices,
        'bedroom_choices' : bedroom_choices,
        'price_choices' : price_choices
    }

    
    return render(request, 'pages/index.html', context)

def about(request):

    realtors = Realtor.objects.order_by('-hire_date')

    realtor_mvp = Realtor.objects.all().filter(is_mvp=True)[0]

    realtor_context = {
        'realtors' : realtors,
        'realtor_mvp' : realtor_mvp
    }

    

    return render(request, 'pages/about.html', realtor_context)