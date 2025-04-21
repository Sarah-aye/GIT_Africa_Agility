from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include



router = DefaultRouter()

router.register('product_list', views.ProductListViewSet, basename='product_list')

router.register('farmerprofile_edit', views.FarmerProfileEditViewSet, basename='farmer_profile_edit')

router.register('farmer_profile', views.FarmerProfileModelViewSet, basename='farmer_profile')

urlpatterns = [
    path('api/register/', views.RegisterView.as_view(), name='register'),
    path('api/login/', views.LoginView.as_view(), name='login'),
    path('api/reset-password/', views.PasswordResetRequestView.as_view(), name='reset-password'),

    # Include all viewset routes
    path('', include(router.urls)),
]
