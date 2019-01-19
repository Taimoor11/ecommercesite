from django.contrib import admin
from .models import Profile, Address

# Register your models here.




@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'customer_type', 'photo']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user_profile', 'address_line1', 'city', 'state', 'postal_code', 'country']






