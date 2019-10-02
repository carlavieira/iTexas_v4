from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyUserManager(BaseUserManager):
    def create_user(self, podio_code, email, first_name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not podio_code:
            raise ValueError('Users must have an podio code ID')

        user = self.model(
            email=self.normalize_email(email),
            podio_code=podio_code,
            first_name=first_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, podio_code, email, first_name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            podio_code,
            email=email,
            first_name=first_name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    POST = (('1,', 'LCP'), ('2', 'LCVP'), ('3', 'TLB'), ('4', 'Membro'))
    DEPARTMENT = (('1', 'LCP'), ('2', 'PM'), ('3', 'F&L'), ('4', 'B2C'), ('5', 'B2B'), ('6', 'OGE'), ('7', 'OGT'), ('8', 'OGV'), ('9', 'IGE'), ('10', 'IGT'), )
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    podio_code = models.CharField(max_length=10, verbose_name='ID do Podio', unique=True)
    first_name = models.CharField(max_length=20, verbose_name='Nome')
    last_name = models.CharField(max_length=20, verbose_name='Sobrenome')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    post = models.CharField(max_length=2, choices=POST, blank=True, null=True,)
    department = models.CharField(max_length=2, choices=DEPARTMENT, blank=True, null=True)
    leader = models.ForeignKey("MyUser", blank=True, null=True, on_delete=models.SET_NULL)

    objects = MyUserManager()

    USERNAME_FIELD = 'podio_code'
    REQUIRED_FIELDS = ['email', 'first_name']

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
from django.db import models

