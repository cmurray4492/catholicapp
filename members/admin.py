from django.contrib import admin
from .models import Members


class MemberAdmin(admin.ModelAdmin):
    """This is Admin setup for the Members App"""
    list_display = ('id', 'member_first_name', 'member_last_name',
                    'member_email_address')
    list_display_links = ('id', 'member_email_address')
    # list_editable = ('member_is_active',)
    search_fields = ('member_email_address',
                     'member_first_name', 'member_last_name')
    # prepopulated_fields = {"blog_slug": ("blog_title",)}


admin.site.register(Members, MemberAdmin)
