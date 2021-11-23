from django.contrib import admin
from .models import Category,Product,OrderItem,Order,Client


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','available','created','updated']
    list_filter = ['available','created','updated']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product,ProductAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(OrderItem, OrderItemAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Order, OrderAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(Client, ClientAdmin)
