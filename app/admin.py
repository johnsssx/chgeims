from .models import Genders, Entries, Review, Post, Game, Aside
from django.contrib import admin


# PrincipalMainLISTADMIN
class EntriesAdmin(admin.ModelAdmin):
    list_display = ["title","gender"]
    list_editable = ["gender"]
    search_fields = ["title", "gender"]
    list_filter = ["gender"]
    list_per_page = 12


# GameLISTADMIN
class GameAdmin(admin.ModelAdmin):
    list_display = ["title", "gender", "gb"]
    list_editable = ["gender", "gb"]
    search_fields = ["title", "gender"]
    list_filter = ["gender"]
    list_per_page = 12


# NewsLISTADMIN
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "number", "created_on")
    list_filter = ("author",)
    search_fields = ["title", "number"]


admin.site.register(Aside)
admin.site.register(Review)
admin.site.register(Genders)
admin.site.register(Game, GameAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Entries, EntriesAdmin)
