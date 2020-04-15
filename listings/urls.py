from django.urls import path

from . import views

# First parameter is the URL Path.
# Second parameter is the method we want to connect this to the view
# Third parameter is the name
# What ( path('') ) means, is that we don't want anything in the URL Path(meaning this will be our home page)
urlpatterns = [
    path('', views.listings, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search')
]
