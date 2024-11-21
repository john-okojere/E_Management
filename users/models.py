from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, worker_id, password=None, **extra_fields):
        if not worker_id:
            raise ValueError("The Worker ID field is required.")
        extra_fields.setdefault('is_active', True)
        user = self.model(worker_id=worker_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, worker_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(worker_id, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    worker_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_first_login = models.BooleanField(default=True)  # To track if user has logged in for the first time
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'worker_id'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        # Automatically generate Worker ID if it does not exist
        if not self.worker_id:
            last_id = CustomUser.objects.order_by('id').last()
            next_id = last_id.id + 1 if last_id else 1
            self.worker_id = f"{1000 + next_id}"  # Example: 1001, 1002, etc.
        super().save(*args, **kwargs)

    def __str__(self):
        return self.worker_id
