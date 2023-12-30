from django.contrib import admin
from .models import Account, Role, Company, Profile, Division, Position
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email', 'username','first_name', 'username', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'username')
    ordering = ('-date_joined',)
    readonly_fields = ('date_joined', 'last_login')
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'division', 'position', 'date_added', 'date_modified')
    readonly_fields = ('date_added', 'date_modified')
    
    
    
admin.site.register(Account, AccountAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Role)
admin.site.register(Company)
admin.site.register(Division)
admin.site.register(Position)