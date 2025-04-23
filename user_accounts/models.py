from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django_countries.fields import CountryField
from django.utils import timezone

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        FARMER = "FARMER", 'Farmer'
        CONSUMER = "CONSUMER", 'Consumer'
        FOODBANK = "FOODBANK", 'Foodbank'
        LOGISTICS = "LOGISTICS", 'Logistics'
    
    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk and not self.role:
            self.role = self.base_role
        return super().save(*args, **kwargs)
    
    
    def __str__(self):
        return f"{self.role} - {self.username} - {self.last_name} -  {self.first_name} - {self.email}"
        


#handling the farmer user
        
class FarmerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.FARMER)
    
class FarmerProfileEdit(User):
    base_role = User.Role.FARMER

    farmer = FarmerManager

    full_name = models.CharField(max_length=50)
    phone_number = models.TextField(help_text='start with country code')
    age = models.PositiveIntegerField(default=1)
    gender = models.CharField(max_length=1, choices = [
        ('M', 'Male'),
        ('F', 'Female'),

    ], default='M')
    years_farming = models.CharField(max_length=50, help_text='e.g 4 years, 4 weeks, or 4 months')
    location = models.CharField(max_length=255, help_text='Country, City')
    farm_size = models.CharField(max_length=50, help_text='e.g 3 Acres')
    type_of_farming = models.CharField(max_length=255, help_text='e.g. list all farming types practiced')
    crops_grown = models.CharField(max_length=255, help_text='list all crops grown')
    livestock = models.CharField(max_length=255, help_text='e.g. sheep, poultry, cattle')

    # farm_name = models.CharField(max_length=255)
    # country = CountryField(blank_label = '(select country)')
    # city = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} - {self.location} - {self.farm_size}"

    class Meta:
        proxy = False
        verbose_name = 'Farmer'
        verbose_name_plural = 'Farmers'
        ordering = ['location']




class FarmerProfileModel(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='farmer_profile')


    full_name = models.CharField(max_length=255, blank=True, null=True)
    farm_name = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} - {self.username} - {self.farm_name}"

    class Meta:
        proxy = False
        verbose_name = 'Farmer Profile'
        verbose_name_plural = 'Farmer Profiles'
        ordering = ['full_name']



class ProductList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='product_list')

    produce_name = models.CharField(max_length=255, blank=True, null=True)
    produce_type = models.CharField(max_length=255, help_text='e.g. cereal, legumes, tubers, fruits, vegetables, etc')
    picture = models.ImageField(upload_to='prduce_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text='Enter price in your local currency, e.g $9.99')
    quantity = models.DecimalField(max_digits=10, decimal_places=2, help_text='Enter quantity in grams or kilograms (e.g. 2.5 kg, 3 g)')
    harvest_date = models.DateField(help_text='Enter harvest date (DD/MM/YYYY)', blank=True, null=True)
    stock_availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.produce_name} - {self.price} - {self.stock_availability}" 
    
    class Meta:
        proxy = False
        verbose_name = 'Product List'
        verbose_name_plural = 'Product Lists'
        ordering = ['produce_name']




#handling the Consumer user

class ConsumerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.CONSUMER)



class ConsumerSignup(User):
    base_role = User.Role.CONSUMER

    consumer = ConsumerManager
    
    country = CountryField(blank_label = '(select country)')
    city = models.TextField(blank=True, null=True)

    class Meta:
        proxy = False
        verbose_name = 'Consumer'
        verbose_name_plural = 'Consumers'
        ordering = ['country']


#handling the foodbank user

class FoodbankManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.FOODBANK)


class FoodbankSignup(User):
    base_role = User.Role.FOODBANK

    foodbank = FoodbankManager
    
    country = CountryField(blank_label = '(select country)')
    city = models.TextField(blank=True, null=True)

    class Meta:
        proxy = False
        verbose_name = 'Foodbank'
        verbose_name_plural = 'Foodbanks'
        ordering = ['country']



#handling the logistics user

class LogisticsManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.LOGISTICS)


class LogisticsSignup(User):
    base_role = User.Role.LOGISTICS

    logistics = LogisticsManager
    
    country = CountryField(blank_label = '(select country)')
    city = models.TextField(blank=True, null=True)

    class Meta:
        proxy = False
        verbose_name = 'Logistics'
        verbose_name_plural = 'Logistics'
        ordering = ['country']
             






# Create your models here.
