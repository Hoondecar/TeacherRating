from django.contrib import admin

# Register your models here.
from teacher_rating.models import Teacher, Chair, Comment, Vote

admin.site.register(Teacher)
admin.site.register(Chair)
admin.site.register(Comment)
admin.site.register(Vote)
