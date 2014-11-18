from django.db import models
from django.contrib import admin

class Links(models.Model):
    url = models.URLField()
    title = models.CharField(max_length = 100)
    img = models.CharField(max_length = 256)
    time = models.DateTimeField(auto_now_add = True)
    flag = models.SmallIntegerField(max_length = 2, default = '0')

    def __str__(self):
        return "%s, %s, %s" % (self.url, self.title, self.img, self.time, self.flag)

class LinksAdmin(admin.ModelAdmin):
    list_display = ['url', 'title', 'img', 'time', 'flag']
    search_field = ['url', 'title', 'flag']

admin.site.register(Links, LinksAdmin)
