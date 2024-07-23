from django.contrib import admin
from apps.contents.models import SiteContent, Skill, Resume


@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ('key',)
    list_display_links = ('key',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'updated_at')
    list_display_links = ('id', 'updated_at',)
