from django.contrib import admin
from .models import (
    CustomUser, Farmer, Product,
    NGO, FoodBank, CommunityKitchen
)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'role')
    list_filter = ('role', 'is_staff', 'is_active')

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('user', 'farm_name', 'contact', 'email', 'location', 'has_storage', 'available_for_donation')
    search_fields = ('farm_name', 'contact', 'email', 'location', 'crops_grown')
    list_filter = ('has_storage', 'available_for_donation')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_type', 'quantity', 'price', 'is_available', 'farmer')
    search_fields = ('name', 'product_type')
    list_filter = ('is_available', 'product_type')

@admin.register(NGO)
class NGOAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'contact', 'operating_hours', 'logistics_availability')
    search_fields = ('full_name', 'email', 'contact', 'service_area')
    list_filter = ('operating_hours', 'order_frequency', 'logistics_availability')

@admin.register(FoodBank)
class FoodBankAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'contact', 'operating_hours', 'logistics_availability')
    search_fields = ('full_name', 'email', 'contact', 'service_area')
    list_filter = ('operating_hours', 'order_frequency', 'logistics_availability')

@admin.register(CommunityKitchen)
class CommunityKitchenAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'contact', 'operating_hours', 'logistics_availability')
    search_fields = ('full_name', 'email', 'contact', 'service_area')
    list_filter = ('operating_hours', 'order_frequency', 'logistics_availability')