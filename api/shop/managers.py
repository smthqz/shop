from django.contrib.auth.base_user import  BaseUserManager

class UserManager(BaseUserManager):

        def create_user(self, username, email=None, password=None, **extra_fields):
                extra_fields.setdefault('is_staff', False)
                extra_fields.setdefault('is_superuser', False)
                extra_fields.setdefault('is_active', False)
                return self._create_user(username, email, password, **extra_fields)