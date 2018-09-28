from django.contrib import admin

from .models import Question, Work, Lesson


admin.site.register(Question)
admin.site.register(Lesson)
admin.site.register(Work)
