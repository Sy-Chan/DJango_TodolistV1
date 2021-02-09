from django.contrib import admin
from .models import ToDo_List

# Register your models here.
class ListAdmin(admin.ModelAdmin):
    list_display = ('id','date ','action', 'due','status','dDate')
    admin.site.register(ToDo_List)
