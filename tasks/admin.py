from django.contrib import admin
from tasks.models import Accessory , Brand
# Register your models here.

@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass