from django.contrib import admin
from . import models


@admin.register(models.Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'developer', 'release']
    list_display_links = ['name']


@admin.register(models.Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ['id', 'word_en', 'word_ru', 'game', 'user', 'create_at', 'update_at']
    list_display_links = ['word_en']


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(models.Correction)
class CorrectionAdmin(admin.ModelAdmin):
    list_display = ['definition', 'create_at']
    list_display_links = ['definition', 'create_at']
