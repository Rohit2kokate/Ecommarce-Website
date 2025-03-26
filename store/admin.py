from django.contrib import admin
from . import models
# Register your models here.
admin.site.site_header="Ecommarce Website"
admin.site.site_title="Shop"

class filter(admin.SimpleListFilter):
    title='filter'
    parameter_name='filter parameter'
    def lookups(self, request, model_admin):
        return (
            ('filter','filter'),
            )
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter()
        else:
            return queryset
        
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    #list_filter = ('date_joined')
    list_display=['first_name','last_name','email','phone_number']
    search_fields = ('first_name','last_name')
    list_editable=['phone_number']
    list_per_page=2

@admin.register(models.Product)
class admin_Product(admin.ModelAdmin):
    list_filter=['product_price']
    list_display=('product_name','product_price','product_category')
    list_per_page=4

@admin.register(models.Category)
class admin_category(admin.ModelAdmin):
    list_display = ['name']
    list_filter=['name']
    search_fields=['name']
    list_per_page=2


@admin.register(models.Order)
class admin_Order(admin.ModelAdmin):
    list_display = ('customer', 'product_name', 'total_cost')
    list_filter = ('customer', 'product_name')
    search_fields = ('customer', 'product_name')
    list_per_page=3
