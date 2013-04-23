from django.contrib import admin
from models import Podcast

class PodcastAdmin(admin.ModelAdmin):
    list_filter = ('program',)
    list_display = ('program', 'date', )
    #search_fields = ('name', 'uri_name')


admin.site.register(Podcast, PodcastAdmin)


