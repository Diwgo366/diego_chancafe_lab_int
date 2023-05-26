from django.contrib import admin
from owner.models import Owner

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'vigente')
    list_filter = ("pais",)
    search_fields = ("nombre", "pais")
