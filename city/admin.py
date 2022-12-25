from django.contrib import admin

from city.models import City


class CityAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name')

admin.site.register(City, CityAdmin)

