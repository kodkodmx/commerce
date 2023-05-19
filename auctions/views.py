from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Listing, User, Categorie, Comment, Bid


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })
    
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def categories(request):
    return render(request, "auctions/categories.html", {
        "categories": Categorie.objects.all()
    })


def category(request, category):
    return render(request, "auctions/category.html", {
        "category": Categorie.objects.get(categories=category),
        "listings": Listing.objects.filter(category=Categorie.objects.get(categories=category))
    })

@login_required
def watchlist(request):
    return render(request, "auctions/watchlist.html", {
        "listings": Listing.objects.filter(watchlist=request.user)
    })

@login_required
def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        starting_bid = request.POST["starting_bid"]
        image_url = request.POST["image_url"]
        category = request.POST["category"]
        owner = request.user
        
        try:
            categorydata = Categorie.objects.get(categories=category)
            newListing = Listing.objects.create(
                title=title,
                description=description,
                price=starting_bid,
                image_url=image_url,
                category=categorydata,
                owner=owner)            
            newListing.save()
        except IntegrityError:
            return render(request, "auctions/create.html", {
                "message": "Listing already exists."
            })
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/create.html", {
            "categories": Categorie.objects.all()
        })
    
def listing(request, listing_id):
    if request.method == "POST":
        bid = request.POST["bid"]
        listing = Listing.objects.get(pk=listing_id)
        newBid = Bid.objects.create(
            bid=bid,
            listing=listing,
            bidder=request.user
        )
        if listing.bids == 0:
            listing.current_bid = listing.price
        if bid != "" and float(bid) > listing.current_bid:
            listing.current_bid = bid
            listing.bids += 1
            listing.current_bid = bid
            listing.current_bidder = request.user
            listing.save()
            newBid.save()
            return render(request, "auctions/listing.html", {
                "listing": Listing.objects.get(pk=listing_id)
            })
        else:
            return render(request, "auctions/listing.html", {
                "listing": Listing.objects.get(pk=listing_id),
                "message": "Bid must be higher than starting bid."
            })
    else:
        return render(request, "auctions/listing.html", {
        "listing": Listing.objects.get(pk=listing_id),
        "comments": Comment.objects.filter(listing=listing_id)

    })
@login_required
def add(request, listing_id):
    user = request.user
    listing = Listing.objects.get(pk=listing_id)
    listing.watchlist.add(user)
    return render(request, "auctions/listing.html", {
        "listing": Listing.objects.get(pk=listing_id)
    })
@login_required
def remove(request, listing_id):
    user = request.user
    listing = Listing.objects.get(pk=listing_id)
    listing.watchlist.remove(user)
    return render(request, "auctions/listing.html", {
        "listing": Listing.objects.get(pk=listing_id)
    })
@login_required
def close(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    listing.active = False
    listing.winner = listing.current_bidder
    listing.save()
    return render(request, "auctions/listing.html", {
        "listing": Listing.objects.get(pk=listing_id)
    })
@login_required
def comments(request, listing_id):
    comment = request.POST["comment"]
    user = request.user
    listing = Listing.objects.get(pk=listing_id)
    newComment = Comment.objects.create(
        comment=comment,
        user=user,
        listing=listing
    )
    newComment.save()
    return render(request, "auctions/listing.html", {
        "listing": Listing.objects.get(pk=listing_id),
        "comments": Comment.objects.filter(listing=listing_id)
    })


    
    
    
    
