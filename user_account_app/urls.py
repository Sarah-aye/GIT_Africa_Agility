from django.urls import path
from . import views

urlpatterns = [
    # Registration
    path('register/', views.register_user, name='register'),

    # Farmer URLs
    path('farmer/profile/', views.create_or_update_farmer_profile, name='create_farmer_profile'),
    path('farmer/dashboard/', views.farmer_dashboard, name='farmer_dashboard'),

    # Community Kitchen URLs
    path('community-kitchen/profile/', views.create_or_update_community_kitchen_profile, name='create_community_kitchen_profile'),
    path('community-kitchen/dashboard/', views.community_kitchen_dashboard, name='community_kitchen_dashboard'),

    # NGO URLs
    path('ngo/profile/', views.create_or_update_NGO_profile, name='create_NGO_profile'),
    path('ngo/dashboard/', views.ngo_dashboard, name='ngo_dashboard'),

    # FoodBank URLs
    path('foodbank/profile/', views.create_or_update_FoodBank_profile, name='create_foodbank_profile'),
    path('foodbank/dashboard/', views.foodbank_dashboard, name='foodbank_dashboard'),
]