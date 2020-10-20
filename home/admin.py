from django.contrib import admin

# Register your models here.
from home.models import Setting, Contact_MSJ



class ConMsj_Admin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'status', ]  # admin panal listesi
    list_filter = ['status']

admin.site.register(Setting)
admin.site.register(Contact_MSJ,ConMsj_Admin)