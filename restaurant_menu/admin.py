from django.contrib import admin
from .models import Item
#credential for admin login adda, Python2025!

# Register your models here.
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('meal', 'status')
    list_filter = ('status',)
    search_fields = ('meal', 'description')

admin.site.register(Item, MenuItemAdmin)





