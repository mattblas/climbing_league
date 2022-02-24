from django.contrib import admin
from climbing_ligue.models import Route, User_routes, Active_edition, User_Group, Active_round


# Register your models here.

# @admin.register(Edition)
# class EditionAdmin(admin.ModelAdmin):
#     ordering = ('edition_number',)
#     list_display = ('edition_number',)
#     search_fields = ('edition_number',)

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('route_name', 'route_grade', 'points', 'edition', 'round', 'route_group', 'add_date',)
    search_fields = ('route_name', 'edition',)

@admin.register(User_routes)
class User_routesAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_routes', 'date_created')
    search_fields = ('user_name',)

@admin.register(Active_edition)
class Active_editionAdmin(admin.ModelAdmin):
    list_display = ('edition', 'current_edition',)

@admin.register(Active_round)
class Active_editionAdmin(admin.ModelAdmin):
    list_display = ('round', 'current_round',)

@admin.register(User_Group)
class User_GroupAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'edition', 'user_group',)
