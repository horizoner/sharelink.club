from django.db import models
from django.contrib import admin

class LinkHome(models.Model):
    url = models.URLField()
    title = models.CharField(max_length = 100)
    img = models.CharField(max_length = 256)
    time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return "%s, %s, %s" % (self.url, self.title, self.time)

class LinkHomeAdmin(admin.ModelAdmin):
    list_display = ['url', 'title', 'img', 'time']
    search_field = ['url']

admin.site.register(LinkHome, LinkHomeAdmin)
