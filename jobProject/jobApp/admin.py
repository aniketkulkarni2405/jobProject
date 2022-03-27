from django.contrib import admin
from jobApp.models import *

class HydjobsAdmin(admin.ModelAdmin):
    list_display=["date","company","title","eligibility","address","email","phonenumber"]

class ChennaijobsAdmin(admin.ModelAdmin):
    list_display=["date","company","title","eligibility","address","email","phonenumber"]

class PunejobsAdmin(admin.ModelAdmin):
    list_display=["date","company","title","eligibility","address","email","phonenumber"]

class MumbaijobsAdmin(admin.ModelAdmin):
    list_display=["date","company","title","eligibility","address","email","phonenumber"]

admin.site.register(Hydjobs,HydjobsAdmin)
admin.site.register(Punejobs,PunejobsAdmin)
admin.site.register(Mumbaijobs,MumbaijobsAdmin)
admin.site.register(Chennaijobs,ChennaijobsAdmin)
# Register your models here.
