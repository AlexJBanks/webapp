from django.contrib import admin

from cv.models import Basic, Education, Grade, Work

admin.site.register(Basic)
admin.site.register(Education)
admin.site.register(Grade)
admin.site.register(Work)
