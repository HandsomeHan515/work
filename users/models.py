from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class AccountManager(BaseUserManager):

    def create_user(self, username, nickname=None, password=None):
        if not username:
            raise ValueError("Users must have username")

        user = self.model(
            username=username,
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, nickname, password):
        user = self.create_user(
            username=username,
            password=password,
            nickname=nickname,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    username = models.CharField('telephone', max_length=128, unique=True)
    nickname = models.CharField(max_length=256, blank=True, null=True)
    avatar = models.ImageField(null=True, blank=True)
    address = models.CharField(max_length=1024, blank=True, null=True)
    email = models.EmailField(max_length=256, blank=True, null=True)
    sex = models.CharField(max_length=64, choices=(
        ('male', u'男'), ('female', u'女')), default='male')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    register_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nickname']

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return True
