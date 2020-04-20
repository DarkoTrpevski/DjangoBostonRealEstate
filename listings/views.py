'''
    This is our views module for our listings APP
'''
from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404
from .models import Listing
from .choices import price_choices, bedroom_choices, state_choices

# Create your views here.
'''
    This is our homepage for our listings APP
'''


def index(request):

    # For no particular order
    # listings = Listing.objects.all()

    # For ordering by date(The minus "-" in the below method means the order is descending)
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    # The ( context ) value will be send to the html, so we can access it there
    return render(request, 'listings/listings.html', context)


'''
    This is our page for single item from current listings in the listings APP
'''


def listing(request, listing_id):
    selected_listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': selected_listing
    }

    return render(request, 'listings/listing.html', context)


'''
    This is our page for searching inside our listings APP
'''


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Search keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    # Search City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(
                city__iexact=city)

    # Search State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(
                state__iexact=state)

    # Search Bedrooms (less than or equal to)
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(
                bedrooms__lte=bedrooms)

    # Search Price (less than or equal to)
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(
                price__lte=price)

    # The 'values' will contain the whole GET request. This will be usefull to keep the search fields
    # full of previous search parameters instead of getting empty search form again.
    context = {
        'listings': queryset_list,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
