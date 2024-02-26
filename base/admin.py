from django.contrib import admin

from base import models

admin.site.register(models.Pengguna)
admin.site.register(models.Messages)
admin.site.register(models.RoomChat)