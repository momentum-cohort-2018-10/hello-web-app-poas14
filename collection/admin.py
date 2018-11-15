from django.contrib import admin

from collection.models import Rocket

class RocketAdmin(admin.ModelAdmin):
    model = Rocket
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Rocket, RocketAdmin)