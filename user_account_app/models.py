from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.


# model1. Farmer model.

class CustomUser(AbstractUser):
    Category_Choice = [
        ('farmer', 'Farmer'),
        ('ngo', 'NGO'),
        ('food_banks', 'Food Banks'),
        ('community_kitchen', 'Community Kitchen'),
        ('consumer', 'Consumer'),
        ('logistics', 'Logistics'),
        ('food_banks_ngo_community_kitchen', 'Food Banks | NGO | Community Kitchen'),
    ]

    role = models.CharField(max_length=60, choices=Category_Choice, default='consumer')

    def __str__(self):
        return self.username
    

    # farmer model starts here

class Farmer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='farmer_profile')
    farm_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    location = models.TextField()
    email = models.EmailField()
    crops_grown = models.TextField(help_text="e.g. maize, tomatoes, onions")
    average_harvest = models.CharField(max_length=255)
    has_storage = models.BooleanField(default=False)
    available_for_donation = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.farm_name} (Farmer)"
    
    class Meta:
        verbose_name = "Farmer data"
        verbose_name_plural = "Farmers data"
        ordering = ['farm_name']
    
# class of product attached to the farmer
class Product(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=100, help_text="e.g. vegetable, grain, fruit")
    quantity = models.DecimalField(max_digits=10, decimal_places=2, help_text="Quantity in kilograms or relevant unit")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price per unit")
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.product_type}) - {self.quantity} units"
    

    class Meta:
        verbose_name = "Farmer Product"
        verbose_name_plural = "Farmer Products"
        ordering = ['name']


# NGO Model

class NGO(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ngo_profile')

    full_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=100, help_text="Phone number or email")
    address = models.TextField()
    email = models.EmailField()

    about_us = models.TextField(blank=True, null=True)
    service_area = models.CharField(max_length=255, blank=True, null=True)

    operating_hours = models.CharField(
        max_length=50,
        choices=[
            ('weekdays', 'Monday to Friday: 8:00 AM - 5:00 PM'),
            ('saturday', 'Saturday: 9:00 AM - 1:00 PM'),
            ('sunday_closed', 'Sunday: Closed'),
        ],
        default='weekdays'
    )
    certification = models.FileField(upload_to='document/', validators= [FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpeg', 'docx'])], blank=True, null=True)
    product_type = models.TextField(help_text="e.g vegetables, cereals, legumes, fruits", blank=True, null=True)
    typical_quantity = models.CharField(max_length=255, choices=[
        ('0 - 50 kg', '0 to 50 kilograms'),
        ('60 - 100 kg', '60 to 100 kilograms'),
        ('110 - 150 kg', '110 to 150 kilograms'), 

        ], default= '0 - 50 kg')
    order_frequency = models.CharField(max_length=255, choices=[
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly') 

        ], default= 'monthly')
    logistics_availability = models.BooleanField(default=True)
    Additional_Information = models.TextField(help_text="e.g core values, primary mission, operation area", blank=True, null=True)


    def __str__(self):
        return f"{self.full_name} - {self.email}"

    class Meta:
        verbose_name = "NGO Profile"
        verbose_name_plural = "NGO Profiles"
        ordering = ['full_name']


# FoodBank Model

class FoodBank(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='FoodBank_profile')

    full_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=100, help_text="Phone number or email")
    address = models.TextField()
    email = models.EmailField()

    about_us = models.TextField(blank=True, null=True)
    service_area = models.CharField(max_length=255, blank=True, null=True)

    operating_hours = models.CharField(
        max_length=50,
        choices=[
            ('weekdays', 'Monday to Friday: 8:00 AM - 5:00 PM'),
            ('saturday', 'Saturday: 9:00 AM - 1:00 PM'),
            ('sunday_closed', 'Sunday: Closed'),
        ],
        default='weekdays'
    )
    certification = models.FileField(upload_to='document/', validators= [FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpeg', 'docx'])], blank=True, null=True)
    product_type = models.TextField(help_text="e.g vegetables, cereals, legumes, fruits", blank=True, null=True)
    typical_quantity = models.CharField(max_length=255, choices=[
        ('0 - 50 kg', '0 to 50 kilograms'),
        ('60 - 100 kg', '60 to 100 kilograms'),
        ('110 - 150 kg', '110 to 150 kilograms'), 

        ], default= '0 - 50 kg')
    order_frequency = models.CharField(max_length=255, choices=[
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly') 

        ], default= 'monthly')
    logistics_availability = models.BooleanField(default=True)
    Additional_Information = models.TextField(help_text="e.g core values, primary mission, operation area", blank=True, null=True)


    def __str__(self):
        return f"{self.full_name} - {self.email}"

    class Meta:
        verbose_name = "FoodBank Profile"
        verbose_name_plural = "FoodBank Profiles"
        ordering = ['full_name']

# Community Kitchen

class CommunityKitchen(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='CommunityKitchen_profile')

    full_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=100, help_text="Phone number or email")
    address = models.TextField()
    email = models.EmailField()

    about_us = models.TextField(blank=True, null=True)
    service_area = models.CharField(max_length=255, blank=True, null=True)

    operating_hours = models.CharField(
        max_length=50,
        choices=[
            ('weekdays', 'Monday to Friday: 8:00 AM - 5:00 PM'),
            ('saturday', 'Saturday: 9:00 AM - 1:00 PM'),
            ('sunday_closed', 'Sunday: Closed'),
        ],
        default='weekdays'
    )



    certification = models.FileField(upload_to='document/', validators= [FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpeg', 'docx'])], blank=True, null=True)
    product_type = models.TextField(help_text="e.g vegetables, cereals, legumes, fruits", blank=True, null=True)
    typical_quantity = models.CharField(max_length=255, choices=[
        ('0 - 50 kg', '0 to 50 kilograms'),
        ('60 - 100 kg', '60 to 100 kilograms'),
        ('110 - 150 kg', '110 to 150 kilograms'), 

        ], default= '0 - 50 kg')
    order_frequency = models.CharField(max_length=255, choices=[
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly') 

        ], default= 'monthly')
    logistics_availability = models.BooleanField(default=True)
    Additional_Information = models.TextField(help_text="e.g core values, primary mission, operation area", blank=True, null=True)


    def __str__(self):
        return f"{self.full_name} - {self.email}"

    class Meta:
        verbose_name = "Community-Kitchen Profile"
        verbose_name_plural = "Community-Kitchen Profiles"
        ordering = ['full_name']