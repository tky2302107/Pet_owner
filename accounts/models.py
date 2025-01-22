from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext_lazy

class CustomUserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password,  **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password,  **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    screen_name = models.CharField(
        gettext_lazy('アカウント名'),
        max_length=128,
        default='',
        blank=True,
        help_text=gettext_lazy('128文字以内で入力してください'),
    )
    email = models.EmailField(gettext_lazy('メールアドレス'), unique=True)
    is_staff = models.BooleanField(
        gettext_lazy('staff status'),
        default=False,
        help_text=gettext_lazy('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        gettext_lazy('active'),
        default=True,
        help_text=gettext_lazy(
            'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(gettext_lazy('date joined'), default=timezone.now)

    objects = CustomUserManager()

    points = models.IntegerField(
        default=0,
        blank=True,
        null=True,
    )

    pt_give = models.IntegerField(
        default=0,
        blank=True,
        null=True,        
    )

    icon = models.ImageField(
        upload_to='icon/post',
        verbose_name='画像',
        null=True,
        blank=True
    )

    profile = models.TextField(
        gettext_lazy('プロフィール'),
        max_length=200,
        null=True,
        default='',
        blank=True,
        help_text=gettext_lazy('200文字以内で入力してください'),
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = gettext_lazy('user')
        verbose_name_plural = gettext_lazy('users')

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return self.screen_name or self.email
    
class fund(models.Model):
    points_sum = models.IntegerField(
        default=0,
    )

    def __str__(self):
        return self.__unicode__()



class AdoptList(models.Model):
    id = models.AutoField(primary_key=True)
    species = models.CharField(
        gettext_lazy("種族"),
        null=False,
        max_length=30,
        default='',
        blank=False,
    )
    detail = models.CharField(
        gettext_lazy("どんな子？"),
        null=False,
        max_length=128,
        default='',
        blank=False,
    )
    place = models.CharField(
        gettext_lazy("会える場所"),
        null=False,
        max_length=30,
        default='',
        blank=False,
    )
    address = models.CharField(
        gettext_lazy("住所"),
        null=False,
        max_length=50,
        default='',
        blank=False,
    )
    
    tel = models.CharField(
        gettext_lazy("電話(ハイフン無し)"),
        default=0,
        max_length=13
    )
    # tel = models.IntegerField(
    #     gettext_lazy("電話(ハイフン無し)"),
    #     default=0,
    # )

    email = models.CharField(
        gettext_lazy("メール"),
        null=True,
        max_length=50,
        default='',
        blank=True,
    )

    title = models.CharField(
        gettext_lazy("一言紹介(20文字)"),
        null=True,
        max_length=20,
        default='',
        blank=True,
    )
    def __str__(self):
        return self.title
