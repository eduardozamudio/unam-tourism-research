from django.contrib import admin
from easy_select2 import select2_modelform
from leaflet.admin import LeafletGeoAdmin

# Register your models here
from .models import Researcher, PosDegree, Degree, CourseTeacher, Course, Institution, University, Project, \
    ProjectMember, Position, PositionType, Professor

ResearcherForm = select2_modelform(Researcher, attrs={'width': '250px'})

class ResearcherAdmin(admin.ModelAdmin):
    form = ResearcherForm


UniversityForm = select2_modelform(University, attrs={'width': '250px'})

class UniversityAdmin(LeafletGeoAdmin):
    form = UniversityForm


CourseForm = select2_modelform(Course, attrs={'width': '250px'})

class CourseAdmin(admin.ModelAdmin):
    form = CourseForm


admin.site.register(Researcher, ResearcherAdmin)
admin.site.register(Degree)
admin.site.register(PosDegree)

admin.site.register(CourseTeacher)
admin.site.register(Course, CourseAdmin)

admin.site.register(Institution)
admin.site.register(University, UniversityAdmin)

admin.site.register(Position)
admin.site.register(PositionType)

admin.site.register(Professor)

# admin.site.register(Project)
# admin.site.register(ProjectMember)
#
#
