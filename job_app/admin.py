from django.contrib import admin
from .models import Form

class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name","date","occupation")
    list_filter = ("date","occupation")
    search_fields = ("first_name","date","occupation")
    ordering=("date",)
    readonly_fields = ("occupation",)

admin.site.register(Form,FormAdmin)

