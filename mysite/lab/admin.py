from django.contrib import admin

from .models import Team, Shop, Osoba, Stanowisko

admin.site.register(Team)
admin.site.register(Shop)


class OsobaAdmin(admin.ModelAdmin):
    readonly_fields = ["data_dodania"]
    list_display = ["data_dodania", "nazwisko", "imie", "stanowisko", "plec"]
    list_filter = ["stanowisko", "data_dodania"]

    @admin.display(description="Dodana")
    def data_dodania(self, instance):
        return instance.data_dodania

    @admin.display(description="Stanowisko")
    def stanowisko(self, instance):
        return f"{instance.stanowisko.nazwa} ({instance.stanowisko.id})"

# Dodanie 2 nowych modeli do panelu administratora
admin.site.register(Osoba, OsobaAdmin)

class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ["nazwa", "opis"]
    list_filter = ["nazwa"]

admin.site.register(Stanowisko, StanowiskoAdmin)
# Register your models here.
