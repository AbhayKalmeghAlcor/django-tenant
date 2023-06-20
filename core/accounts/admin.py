from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html


class AccountAdmin(UserAdmin):

    # if Account.avtar is not 'Null':
    #     def thumbnail(self, object):
    #         return format_html('<img src="{}" width="30" style="border-redius:50%;">'.format(object.avtar.url))
    #
    #     thumbnail.short_description = 'Profile Picture'
    #
    # else:
    #     pass
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'created_date')
    ordering = ('-created_date',)
    filter_horizontal = ()
    fieldsets = ()
    list_filter = ()


admin.site.register(Account, AccountAdmin)

