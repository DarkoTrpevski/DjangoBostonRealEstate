from django.shortcuts import render
from listings.models import Listing
from listings.choices import price_choices, bedroom_choices, state_choices
from listings.models import Realtor
# Create your views here.

# We add the templates folder in settings.py in the TEMPLATES array >'DIRS'


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]

    # Pass the string arrays( dictionaries ) to the context, to be used instead of static stuff in the homepage search form
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    # The ( context ) value will be send to the html, so we can access it there
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.order_by('hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)
