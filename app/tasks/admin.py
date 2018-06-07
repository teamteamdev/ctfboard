from django.contrib import admin
from tasks.models import Submit, Hint


@admin.register(Submit)
class SubmitModelAdmin(admin.ModelAdmin):
    list_display = ['text', 'task', 'team', 'success', 'timestamp']


@admin.register(Hint)
class HintModelAdmin(admin.ModelAdmin):
    pass
