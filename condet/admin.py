from django.contrib import admin
from easy_select2 import select2_modelform

# Register your models here
from .models import Researcher, PosDegree, Degree, CourseTeacher, Course, Institution, University, Project, \
    ProjectMember

ResearcherForm = select2_modelform(Researcher, attrs={'width': '250px'})

class ResearcherAdmin(admin.ModelAdmin):
    form = ResearcherForm

UniversityForm = select2_modelform(University, attrs={'width': '250px'})

class UniversityAdmin(admin.ModelAdmin):
    form = UniversityForm

admin.site.register(Researcher, ResearcherAdmin)
admin.site.register(Degree)
admin.site.register(PosDegree)

admin.site.register(CourseTeacher)
admin.site.register(Course)

admin.site.register(Institution)
admin.site.register(University, UniversityAdmin)

admin.site.register(Project)
admin.site.register(ProjectMember)
#
#