# user/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import format_html

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'delete_user_link')

    def delete_user_link(self, obj):
        return format_html('<a class="button" href="{}">Xóa</a>', reverse('admin:auth_user_delete', args=[obj.pk]))
    delete_user_link.short_description = 'Xóa người dùng'
    delete_user_link.allow_tags = True

# Unregister the original User admin
admin.site.unregister(User)
# Register the customized User admin
admin.site.register(User, UserAdmin)
