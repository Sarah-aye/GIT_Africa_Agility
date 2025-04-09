from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import (
    CustomUserRegistrationForm,
    FarmerProfileForm,
    ProductFormSet,
    NGOForm,
    CommunityKitchenForm,
    FoodBankForm
)
from .models import Farmer, NGO, CommunityKitchen, FoodBank

def register_user(request):
    """
    Handle user registration using CustomUserRegistrationForm
    """
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            role = form.cleaned_data.get('role')

            # Redirect based on role
            if role == 'farmer':
                return redirect('create_farmer_profile')
            elif role == 'community_kitchen':
                return redirect('create_community_kitchen_profile')
            elif role == 'ngo':
                return redirect('create_NGO_profile')
            elif role == 'foodbank':
                return redirect('create_foodbank_profile')
            else:
                return redirect('home')  # Default redirect if the role is unknown
    else:
        form = CustomUserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})

# Farmer Views

@login_required
def create_or_update_farmer_profile(request):
    """
    View for creating or updating Farmer profile + adding products.
    """
    try:
        farmer = request.user.farmer
        is_editing = True
    except Farmer.DoesNotExist:
        farmer = None
        is_editing = False

    if request.method == 'POST':
        form = FarmerProfileForm(request.POST, request.FILES, instance=farmer)
        formset = ProductFormSet(request.POST, instance=farmer)

        if form.is_valid() and formset.is_valid():
            farmer = form.save(commit=False)
            farmer.user = request.user
            farmer.save()

            formset.instance = farmer
            formset.save()

            return redirect('farmer_dashboard')
    else:
        form = FarmerProfileForm(instance=farmer)
        formset = ProductFormSet(instance=farmer)

    return render(request, 'farmers/farmer_profile_form.html', {
        'form': form,
        'formset': formset,
        'is_editing': is_editing,
    })

@login_required
def farmer_dashboard(request):
    """
    Dashboard view for the logged-in farmer.
    """
    farmer = get_object_or_404(Farmer, user=request.user)
    products = farmer.products.all()

    return render(request, 'farmers/farmer_dashboard.html', {
        'farmer': farmer,
        'products': products
    })

# Community Kitchen Views

@login_required
def create_or_update_community_kitchen_profile(request):
    """
    View for creating or updating a Community Kitchen profile.
    """
    try:
        kitchen = request.user.communitykitchen
        is_editing = True
    except CommunityKitchen.DoesNotExist:
        kitchen = None
        is_editing = False

    if request.method == 'POST':
        form = CommunityKitchenForm(request.POST, request.FILES, instance=kitchen)
        if form.is_valid():
            kitchen = form.save(commit=False)
            kitchen.user = request.user
            kitchen.save()
            return redirect('community_kitchen_dashboard')
    else:
        form = CommunityKitchenForm(instance=kitchen)

    return render(request, 'community_kitchen/profile_form.html', {
        'form': form,
        'is_editing': is_editing
    })

@login_required
def community_kitchen_dashboard(request):
    """
    Dashboard view for the logged-in community kitchen user.
    """
    kitchen = get_object_or_404(CommunityKitchen, user=request.user)

    return render(request, 'community_kitchen/dashboard.html', {
        'kitchen': kitchen
    })

# NGO Views

@login_required
def create_or_update_NGO_profile(request):
    """
    View for creating or updating an NGO profile.
    """
    try:
        ngo = request.user.ngo
        is_editing = True
    except NGO.DoesNotExist:
        ngo = None
        is_editing = False

    if request.method == 'POST':
        form = NGOForm(request.POST, request.FILES, instance=ngo)
        if form.is_valid():
            ngo = form.save(commit=False)
            ngo.user = request.user
            ngo.save()
            return redirect('ngo_dashboard')
    else:
        form = NGOForm(instance=ngo)

    return render(request, 'ngo/profile_form.html', {
        'form': form,
        'is_editing': is_editing
    })

@login_required
def ngo_dashboard(request):
    """
    Dashboard view for the logged-in NGO user.
    """
    ngo = get_object_or_404(NGO, user=request.user)

    return render(request, 'ngo/dashboard.html', {
        'ngo': ngo
    })

# FoodBank Views

@login_required
def create_or_update_FoodBank_profile(request):
    """
    View for creating or updating a FoodBank profile.
    """
    try:
        foodbank = request.user.foodbank
        is_editing = True
    except FoodBank.DoesNotExist:
        foodbank = None
        is_editing = False

    if request.method == 'POST':
        form = FoodBankForm(request.POST, request.FILES, instance=foodbank)
        if form.is_valid():
            foodbank = form.save(commit=False)
            foodbank.user = request.user
            foodbank.save()
            return redirect('foodbank_dashboard')
    else:
        form = FoodBankForm(instance=foodbank)

    return render(request, 'foodbank/profile_form.html', {
        'form': form,
        'is_editing': is_editing
    })

@login_required
def foodbank_dashboard(request):
    """
    Dashboard view for the logged-in FoodBank user.
    """
    foodbank = get_object_or_404(FoodBank, user=request.user)

    return render(request, 'foodbank/dashboard.html', {
        'foodbank': foodbank
    })