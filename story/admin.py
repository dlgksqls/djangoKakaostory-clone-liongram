from django.contrib import admin
from story.models import Contents,Comment

# Register your models here.

@admin.register(Contents)
class ContentsModelAdmin(admin.ModelAdmin):
    list_display = ('id','image','content','created_at','writer')