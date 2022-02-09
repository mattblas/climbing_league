from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from members.models import Member 

# Register your models here.

class MemberAdmin(UserAdmin):
    list_display = ('username', 'email', 'gender', 'last_login', 'is_admin', 'is_staff',)
    search_fields = ('email', 'username', 'gender',)
    readonly_fields = ('last_login',)

    filter_horizontal =()
    list_filter = ()
    fieldsets = ()

admin.site.register(Member, MemberAdmin)