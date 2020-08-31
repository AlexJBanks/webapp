from django.contrib import admin

from cv.models import Basic, Education, Grade, Work

admin.site.register(Basic)
admin.site.register(Work)


class GradeInLine(admin.StackedInline):
    model = Grade
    extra = 1


class EducationAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['course','location','start_date','end_date']})]
    inlines = [GradeInLine]


admin.site.register(Education, EducationAdmin)