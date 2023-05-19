from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("categories", views.categories, name="categories"),
    path("category/<str:category>", views.category, name="category"),
    path("create", views.create, name="create"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("close/<int:listing_id>", views.close, name="close"),
    path("add/<int:listing_id>", views.add, name="add"),
    path("remove/<int:listing_id>", views.remove, name="remove"),
    path("add_comment/<int:listing_id>", views.comments, name="add_comment")
]
