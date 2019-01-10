from django.contrib import admin
from .models import Order, OrderItem
import csv
from django.http import  HttpResponse
import datetime


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']



def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model.__meta


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
