from django.contrib import admin
from .models import Advertisement


class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'auction', 'created_date', 'updated_date']
    list_filter = ['auction', 'created_at']
    actions =['maaf', 'maat']



    @admin.action(description='Убрать возможность торга')
    def maaf(self,request, queryset):
        queryset.update(auction = False)

    @admin.action(description='Добавить возможность торга')
    def maat(self, request, queryset):
        queryset.update(auction=True)

    fieldsets = (
        ("Общее", {"fields": ("title", "description")}),
        ("Финансы", {"fields": ("price", "auction"), "classes":["collapse"]})
    )

admin.site.register(Advertisement, AdvertisementsAdmin)






# Register your models here.
