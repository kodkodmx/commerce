from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Categorie(models.Model):
    categories = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.categories}"
    
class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="owner")
    active = models.BooleanField(default=True)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="winner", blank=True, null=True)
    watchlist = models.ManyToManyField(User, blank=True, related_name="watchlist", null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    current_bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="current_bidder", blank=True, null=True)
    current_bid = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    bids = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
    
class Bid(models.Model):
    bid = models.DecimalField(max_digits=6, decimal_places=2, default=0, blank=True, null=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bid_listing", blank=True, null=True)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bid_user", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    
    
    def __str__(self):
        return f"{self.bid}"

class Comment(models.Model):
    comment = models.TextField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE,  related_name="comment_listing", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_user", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} commented on {self.listing}"
    
