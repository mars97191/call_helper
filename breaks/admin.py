from django.contrib import admin
from django.contrib.admin import TabularInline

from breaks.models import organisations, replacements, dicts, breaks


#################
# INLINES
#################
class ReplacementEmployeeInline(TabularInline):
    model = replacements.ReplacementEmployee
    fields = ('employee', 'status')




@admin.register(organisations.Organisations)
class OrganisationsAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'director')



@admin.register(organisations.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'organisation', 'name', 'manager','min_active','break_start', 'break_end' )

@admin.register(replacements.Replacement)
class ReplacementAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'date', 'break_start', 'break_end')

    inlines = (
        ReplacementEmployeeInline,
    )

@admin.register(breaks.Break)
class BreakAdmin(admin.ModelAdmin):
    list_display = ('id', 'replacement', 'break_start', 'break_end', 'duration')



#############################
# Статусы
#############################

@admin.register(dicts.ReplacementStatus)
class ReplacementStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active')

@admin.register(dicts.BreakStatus)
class BreakStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active')