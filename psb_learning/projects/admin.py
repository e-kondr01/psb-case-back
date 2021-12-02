from django.contrib import admin

from psb_learning.projects.models import (
    Project,
    ProjectFile,
    ProjectLink,
    ProjectMember,
)

admin.site.register(Project)
admin.site.register(ProjectFile)
admin.site.register(ProjectMember)
admin.site.register(ProjectLink)
