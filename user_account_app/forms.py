from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms.models import inlineformset_factory
from .models import CustomUser, Farmer, NGO, Product, FoodBank, CommunityKitchen


class CustomUserRegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=150, required=True, label='Full Name')
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    role = forms.ChoiceField(choices=CustomUser.Category_Choice, required=True)

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        help_text="Enter a strong password."
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput,
        help_text="Enter the same password for confirmation."
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'full_name', 'email', 'phone_number', 'password1', 'password2', 'role']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        # If using custom phone_number field later, you can handle that here
        if commit:
            user.save()
        return user
    
    #farmer-registration form

class FarmerProfileForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['farm_name', 'profile_picture', 'location', 'crops_grown', 'average_harvest', 'has_storage', 'available_for_donation',]
        widgets = {
            'location': forms.Textarea(attrs={'rows': 3}),
            'crops_grown': forms.Textarea(attrs={'rows': 3}),
        }


# product form as a sub-form of farmer registration

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_type', 'quantity', 'price', 'is_available']
        widgets = {
            'product_type': forms.TextInput(attrs={'placeholder': 'e.g. vegetable'}),
        }

ProductFormSet = inlineformset_factory(
    parent_model=Farmer,
    model=Product,
    form=ProductForm,
    extra=1,  # Number of extra blank forms to show
    can_delete=True  # Allow user to remove products
)


# Community Kitchen

class CommunityKitchenForm(forms.ModelForm):
    class Meta:
        model = CommunityKitchen
        fields = [
            'full_name', 'address', 'about_us', 'service_area', 'operating_hours', 'certification', 'product_type', 'typical_quantity', 'order_frequency', 'logistics_availability', 'Additional_Information',
        ]
        widgets = {
            'address': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Enter address...'}),
            'about_us': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe your mission or work...'}),
            'product_type': forms.Textarea(attrs={'rows': 2, 'placeholder': 'e.g. vegetables, cereals, legumes'}),
            'Additional_Information': forms.Textarea(attrs={'rows': 3, 'placeholder': 'e.g. core values, operation area'}),
        }

        help_texts = {
            'product_type': 'List the types of food you handle',
        }

    def clean_certification(self):
        certification = self.cleaned_data.get('certification')
        if certification and certification.size > 5 * 1024 * 1024:
            raise forms.ValidationError("Certification file size must be under 5MB.")
        return certification
    
    # NGO form

class NGOForm(forms.ModelForm):
    class Meta:
        model = NGO
        fields = [
            'full_name', 'address', 'about_us', 'service_area', 'operating_hours', 'certification', 'product_type', 'typical_quantity', 'order_frequency', 'logistics_availability', 'Additional_Information',
        ]
        widgets = {
            'address': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Enter address...'}),
            'about_us': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe your mission or work...'}),
            'product_type': forms.Textarea(attrs={'rows': 2, 'placeholder': 'e.g. vegetables, cereals, legumes'}),
            'Additional_Information': forms.Textarea(attrs={'rows': 3, 'placeholder': 'e.g. core values, operation area'}),
        }

        help_texts = {
            'product_type': 'List the types of food you handle',
        }

    def clean_NGO(self):
        certification = self.cleaned_data.get('certification')
        if certification and certification.size > 5 * 1024 * 1024:
            raise forms.ValidationError("Certification file size must be under 5MB.")
        return certification  
    

    #FoodBank form

class FoodBankForm(forms.ModelForm):
    class Meta:
        model = FoodBank
        fields = [
            'full_name', 'address', 'about_us', 'service_area', 'operating_hours', 'certification', 'product_type', 'typical_quantity', 'order_frequency', 'logistics_availability', 'Additional_Information',
        ]
        widgets = {
            'address': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Enter address...'}),
            'about_us': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe your mission or work...'}),
            'product_type': forms.Textarea(attrs={'rows': 2, 'placeholder': 'e.g. vegetables, cereals, legumes'}),
            'Additional_Information': forms.Textarea(attrs={'rows': 3, 'placeholder': 'e.g. core values, operation area'}),
        }

        help_texts = {
            'product_type': 'List the types of food you handle',
        }

    def clean_FoodBank(self):
        certification = self.cleaned_data.get('certification')
        if certification and certification.size > 5 * 1024 * 1024:
            raise forms.ValidationError("Certification file size must be under 5MB.")
        return certification

    