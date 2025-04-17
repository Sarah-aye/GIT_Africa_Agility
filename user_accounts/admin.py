from django.contrib import admin
from .models import User, FarmerProfileEdit, ConsumerSignup, FoodbankSignup, LogisticsSignup, FarmerProfileModel, ProductList


admin.site.register(User)
admin.site.register(FarmerProfileEdit)
admin.site.register(ConsumerSignup)
admin.site.register(FoodbankSignup)
admin.site.register(LogisticsSignup)
admin.site.register(FarmerProfileModel)
admin.site.register(ProductList)

# Register your models here.
