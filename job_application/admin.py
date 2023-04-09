from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    """Modifying the default model admin"""
    list_display = ("first_name", "last_name",
                    "email", "date", "occupation")
    search_fields = ("first_name", "last_name",
                     "email", "date", "occupation")
    list_filter = ("date", "occupation")
    ordering = ("first_name",)
    readonly_fields = ("occupation",)


admin.site.register(Form, FormAdmin)
