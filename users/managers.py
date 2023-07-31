from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, phone_number, full_name, password, **extra_fields):
        """
        Create and save a user with the given phone_number and password.
        """
        if not phone_number:
            raise ValueError(_("phone_number must be set"))

        if not full_name:
            raise ValueError(_("full_name must be set"))

        user = self.model(
            phone_number=phone_number, full_name=full_name, **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, full_name, password, **extra_fields):
        """
        Create and save a SuperUser with the given phone_number and password.
        """
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        # if extra_fields.get("is_staff") is not True:
        #    raise ValueError(_("Superuser must have is_staff=True."))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(phone_number, full_name, password, **extra_fields)
