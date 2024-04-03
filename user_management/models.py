from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, phone, password=None, **extra_fields):
        print("------------create user---------------")
        if not email:
            raise ValueError('email is required')
        if not name:
            raise ValueError('name is required')

        print(f"password---------------{password}")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone=phone,
            **extra_fields

        )

        user.set_password(password)
        print(f"user---------{user}")
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone, password, **extra_fields):
        user = self.create_user(
            email=email,
            name=name,
            phone=phone,
            password=password,
            **extra_fields

        )

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    def __str__(self):
        return self.email
