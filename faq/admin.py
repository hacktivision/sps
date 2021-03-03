from django.contrib import admin

from .models import Faq, FaqCategory

admin.site.site_header = 'SPS MEDIA'

admin.site.register(FaqCategory)

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'author',
        'is_active'
    )
    list_editable = (
        'category',
        'author',
        'is_active',
    )


