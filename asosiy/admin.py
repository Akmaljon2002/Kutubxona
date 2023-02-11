from django.contrib import admin
from.models import *

@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display = ("id", "ism", "kitob_soni", "kurs", "bitiruvchi")
    list_editable = ("kitob_soni", "kurs", "bitiruvchi")
    list_display_links = ("ism", )
    list_filter = ("bitiruvchi", "kurs", "id")
    search_fields = ("ism", "id", "kitob_soni")
    list_per_page = 10

# 2
@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    list_display = ("id", "ism", "kitob_soni", "tirik")
    list_editable = ("kitob_soni", "tirik")
    list_display_links = ("id", "ism")
    list_filter = ("tirik", )
    search_fields = ("ism", )


@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    list_display = ("id", "nom", "sahifa", "janr", "muallif")
    list_editable = ("sahifa", )
    list_display_links = ("nom", "janr")
    list_filter = ("janr", )
    search_fields = ("nom", "id")
    autocomplete_fields = ("muallif", )

# 1
@admin.register(Admin)
class AdminModel(admin.ModelAdmin):
    list_display = ("id", "ism", "ish_vaqti")
    list_filter = ("ish_vaqti", )
    search_fields = ("ism", )

# 3
@admin.register(Record)
class RecordModel(admin.ModelAdmin):
    list_display = ("id", "talaba", "kitob", "admin", "olingan_sana",
                    "qaytardi", "qaytargan_sana")
    autocomplete_fields = ("talaba", "kitob", "admin")