from django.contrib import admin

from .models import Project, TypeProject, CategoryProject, TaskProject, StatusProject, StatusTask, CheckList

admin.site.site_header = 'SPS проекты'

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    date_hierarchy = 'cteated_date'
    list_filter = (
        'status_project',
    )
    list_display_links = ('title',)
    list_display = (
        'status_project', 
        'title', 
        'type_project', 
        'total_budget', 
        'spent_budget', 
        'balance_budget', 
        'cteated_date', 
        'start_date',
        'completed_date',
        'is_active',
    )
    list_editable = (
        'status_project', 
        'type_project', 
        'is_active'
    )


admin.site.register(TypeProject)
admin.site.register(CategoryProject)
admin.site.register(TaskProject)
admin.site.register(StatusProject)
admin.site.register(StatusTask)
admin.site.register(CheckList)
