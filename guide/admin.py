from django.contrib import admin
from .models import GuideProfile


class GuideProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'avatar', 'is_guide')


admin.site.register(GuideProfile, GuideProfileAdmin)
