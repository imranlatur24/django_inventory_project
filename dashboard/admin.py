from django.contrib import admin
from .models import ProductModel,Order
#hide the group from admin page
from django.contrib.auth.models import Group

#add title to admin page
admin.site.site_header="Imran Dashboard"

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    ilst_display=('name','quantity','category',)
    list_filter=('category',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ilst_display=('product','staff','order_quantity')

# admin.site.register(ProductModel,ProductAdmin)
admin.site.unregister(Group)
