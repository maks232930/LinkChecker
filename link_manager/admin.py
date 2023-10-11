from django.contrib import admin

from link_manager.models import Link


class LinkAdmin(admin.ModelAdmin):
    """Конфигурация админ-панели для модели Link."""
    list_display = (
        'id', 'name', 'url', 'condition_type', 'text', 'is_active',
        'timestamp', 'is_result',)
    list_display_links = (
        'id', 'name', 'url', 'condition_type', 'text', 'timestamp',
        'is_result',)
    list_editable = ('is_active',)
    readonly_fields = ('timestamp', 'is_result',)


admin.site.register(Link, LinkAdmin)
