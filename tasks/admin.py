from django.contrib import admin
from tasks.models import Accessory , Brand, Category
# Register your models here.

@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass