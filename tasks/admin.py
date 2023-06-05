from django.contrib import admin
from tasks.models import Accessory
# Register your models here.

@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    pass