from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone_number, address, role, password=None):
        if not email:
            raise ValueError("The email field must be set")
        
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name,
                           phone_number=phone_number, address=address, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_seller(self, email, first_name, last_name, phone_number, address, role, password=None):
        if role != "SELLER":
            raise ValueError("The role must be seller")
        
        user = self.create_user(email, first_name, last_name, phone_number, address, role, password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user


class UserRegister(AbstractUser, PermissionsMixin):
    User = "USER"
    Seller = "SELLER"

    Role_Choice = [
        (User, "User"),
        (Seller, "Seller")
    ]

    # Remove this line as Django already provides an `id` field
    # user_id = models.AutoField(primary_key=True, null=False)

    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=12,
        validators=[RegexValidator(r'^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$')],
        null=False
    )
    address = models.TextField()
    role = models.CharField(max_length=10, choices=Role_Choice, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_group',
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True
    )

    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone_number", "role"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
