from django.contrib import admin
from teams.models import Team


@admin.register(Team)
class TeamModelAdmin(admin.ModelAdmin):
    list_display = ["name", "city", "login", "competition", "score", "last_submit"]
    exclude = ["score", "last_submit"]
