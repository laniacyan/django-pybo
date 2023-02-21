from django.contrib import admin

# Register your models here.
from .models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
    list_display = ['id', 'subject', 'create_date']
    ordering = ['-id'] #+는 오름차순

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)


