from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path("", views.index,  name = "shopHome"),
    path("about/", views.about,  name = "AboutUs"),
    path("contact/", views.contact,  name = "ContactUs"),
    path("tracker/", views.tracker,  name = "TrackingStatus"),
    path("search/", views.search,  name = "Search"),
    path("products/<int:myid>", views.product,  name = "product"),
    path("checkout/", views.checkout,  name = "Checkout"),
    # path("signup/", views.handleSignUp, name="handleSignUp"),
    # path("login/", views.handeLogin,  name = "login"),
    # path("logout/", views.handelLogout,  name = "logout"),
    
    
]
