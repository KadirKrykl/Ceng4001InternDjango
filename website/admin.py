from django.contrib import admin
from django.contrib.auth.models import User

from .models import ResearchGroups, News, UserProfile, Project, Resource, Publication, Research
# Register your models here.
admin.site.register(ResearchGroups)
admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Resource)
admin.site.register(Publication)
admin.site.register(Research)


class NewsAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(News, NewsAdmin)