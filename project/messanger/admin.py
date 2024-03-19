from django.contrib import admin

from messanger.models import Chat


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ("id",)
    list_filter = ("participants",)
    readonly_fields = ("participants",)


from django.apps import apps

models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
