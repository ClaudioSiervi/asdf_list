from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from families.models import Family, FamilyInvite


# admin.site.register(Family) 
# admin.site.register(FamilyInvite) 

@admin.register(Family)
class FamilyAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
        "created_at",
        "updated_at",
    )
    fields = (
        "name",
        "members",
    )
    readonly_fields = (
        # "created_at",
        "updated_at",
    )
    filter_horizontal = ()
    list_filter = ('name',)