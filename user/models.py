from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.contrib.postgres.fields import ArrayField
from django.db import models

# SUPERADMIN = "SPADM"
# ADMIN = "ADM"
# MEMBER = "MBR"

# ROLE_CHOICES = (
#     (SUPERADMIN, "Super Admin"),
#     (ADMIN, "Admin"),
#     (MEMBER, "Member"),
# )


# class Roles(models.Model):
#     role = models.CharField(
#         max_length=5,
#         default=MEMBER,
#         choices=ROLE_CHOICES,
#     )

#     def __str__(self):
#         return str(self.role)


# def get_roles():
#     return Roles.objects.get_or_create(role=MEMBER)[1]


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        # extra_fields.setdefault("role", SUPERADMIN)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, null=True)
    phone = models.BigIntegerField(unique=True, null=True)

    std_id = models.CharField(max_length=255, unique=True, blank=True, null=True)
    clg_id = models.CharField(max_length=255, unique=True, blank=True, null=True)

    valid_till = models.DateTimeField(blank=True, null=True)
    is_premium = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)

    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    interests = ArrayField(models.CharField(max_length=255), blank=True, null=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    # role = models.ForeignKey(Roles, on_delete=models.CASCADE, default=get_roles)  # type: ignore

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "name"]

    objects = UserManager()

    def __str__(self):
        return f"{self.username}-{self.name}"
