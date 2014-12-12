from django.contrib import admin
from .models import Course, Suscriptor

class SuscriptorInline(admin.TabularInline):
	model = Suscriptor
	extra = 1

class CourseAdmin(admin.ModelAdmin):
	inlines = [SuscriptorInline]

admin.site.register(Course, CourseAdmin)

