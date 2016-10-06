from django.contrib import admin

from .models import Question, Choice

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'votes', )
    list_filter = ('question', )

admin.site.register(Question)
admin.site.register(Choice, ChoiceAdmin)
