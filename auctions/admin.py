from django.contrib import admin

# Register your models here.
from .models import User, Listing, Categorie, Comment, Bid

admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Categorie)
admin.site.register(Comment)
admin.site.register(Bid)
