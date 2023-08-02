from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

from .forms import AdminAuthenticationForm


class UserAdmin(BaseUserAdmin):
    list_display = ("full_name", "phone_number", "email", "is_active", "is_admin")
    list_filter = ("is_active", "is_admin")
    fieldsets = (
        (None, {"fields": ("full_name", "email", "phone_number", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_admin",
                    "is_superuser",
                    "last_login",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "full_name",
                    "phone_number",
                    "email",
                    "password1",
                    "password2",
                )
            },
        ),
    )
    search_fields = ("email", "full_name")
    ordering = (
        "created_at",
        "email",
    )
    filter_horizontal = ("groups", "user_permissions")

#    def get_form(self, request, obj=None, **kwargs):
#        form = super().get_form(request, obj, **kwargs)
#        is_superuser = request.user.is_superuser
#        if is_superuser:
#            form.base_fields["is_superuser"].disabled = True
#        return form


admin.site.register(User, UserAdmin)
admin.site.login_form = AdminAuthenticationForm
