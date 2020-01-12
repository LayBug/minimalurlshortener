from django.contrib import admin
from .models import ShortUrl

class ShortUrlAdmin(admin.ModelAdmin):
    fields = ('original_url','suggested_url_suffix', 'generated_url')
    readonly_fields = ['generated_url',]

admin.site.register(ShortUrl, ShortUrlAdmin)
