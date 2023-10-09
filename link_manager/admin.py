from django.contrib import admin
from django.forms import ModelForm

from link_manager.models import Link, Result


class LinkAdminForm(ModelForm):
    class Meta:
        model = Link
        exclude = ['user']


class LinkAdmin(admin.ModelAdmin):
    form = LinkAdminForm
    list_display = ('name', 'url', 'condition_type', 'text', 'is_active',)
    list_display_links = ('name', 'url', 'condition_type', 'text',)
    list_editable = ('is_active',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=request.user)


class ResultAdmin(admin.ModelAdmin):
    list_display = ('link', 'is_result', 'timestamp')
    list_display_links = ('link', 'is_result', 'timestamp')
    list_filter = ('link',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(link__user=request.user)


admin.site.register(Link, LinkAdmin)
admin.site.register(Result, ResultAdmin)
