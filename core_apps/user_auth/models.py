import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .emails import send_account_locked_email
from .managers import UserManager

class User(AbstractUser):
    class SecurityQuestion(models.TextChoices):
        FAVOURITE_COLOR = "FAVOURITE_COLOR", _("What is your favourite color?")
        FAVOURITE_FOOD = "FAVOURITE_FOOD", _("What is your favourite food?")
        CHILDHOOD_FRIEND = "CHILDHOOD_FRIEND", _("Who was your childhood friend?")
        BIRTHCITY = "BIRTHCITY", _("What city were you born in?")

    class ACCOUNT_STATUS(models.TextChoices):
        ACTIVE = "ACTIVE", _("Active")
        LOCKED = "LOCKED", _("Locked")

    class RoleChoices(models.TextChoices):
        CUSTOMER = "CUSTOMER", _("Customer")
        ACCPUNT_EXECUTIVE = "ACCPUNT_EXECUTIVE", _("Account Executive")
        TELLER = "TELLER", _("Teller")
        BRANCH_MANAGER = "BRANCH_MANAGER", _("Branch Manager")

    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username                = models.CharField(_("username"), max_length=12, unique=True)
    security_question       = models.CharField(_("Security Question"), max_length=30, choices=SecurityQuestion.choices)
    security_answer         = models.CharField(_("Security Answer"), max_length=30)
    email                   = models.EmailField(_("email"), unique=True, db_index=True)  # Indexing email for faster searching
    first_name              = models.CharField(_("first name"), max_length=30)
    middle_name             = models.CharField(_("middle name"), max_length=30, blank=True, null=True)
    last_name               = models.CharField(_("last name"), max_length=30)
    id_no                   = models.PositiveIntegerField(_("ID Number"), unique=True)
    account_status          = models.CharField(_("account status"), max_length=10, choices=ACCOUNT_STATUS.choices, default=ACCOUNT_STATUS.ACTIVE)
    role                    = models.CharField(_("role"), max_length=20, choices=RoleChoices.choices, default=RoleChoices.CUSTOMER)
    login_failed_attempts   = models.PositiveSmallIntegerField(_("login failed attempts"), default=0)
    last_failed_login       = models.DateTimeField(null=True, blank=True)
    otp                     = models.CharField(_("OTP"), max_length=6, blank=True)
    otp_expiry_time         = models.DateTimeField(_("OTP Expiry Time"), null=True, blank=True)


    # Overriding the default user manager with our custom user manager
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "id_no", "security_question", "security_answer"]

    def set_otp(self, otp:str)->None:
        self.otp = otp
        self.otp_expiry_time = timezone.now() + settings.OTP_EXPIRATION
        self.save()

    def verify_otp(self, otp:str)->bool:
        if self.otp == otp and self.otp_expiry_time > timezone.now():
            self.otp = ''
            self.otp_expiry_time = None
            self.save()
            return True
        return False
    
    def handle_failed_login_attempts(self)->None:
        self.login_failed_attempts += 1
        self.last_failed_login = timezone.now()
        if self.login_failed_attempts >= settings.LOGIN_ATTEMPTS:
            self.account_status = self.ACCOUNT_STATUS.LOCKED
            send_account_locked_email(self)
        self.save()

    def reset_failed_login_attempts(self)->None:
        self.login_failed_attempts = 0
        self.last_failed_login = None
        self.account_status = self.ACCOUNT_STATUS.ACTIVE
        self.save()

    def unlock_account(self)->None:
        if self.account_status == self.ACCOUNT_STATUS.LOCKED:
            self.account_status = self.ACCOUNT_STATUS.ACTIVE
            self.login_failed_attempts = 0
            self.last_failed_login = None
            self.save()

    @property
    def is_locked(self)->bool:
        if self.account_status == self.ACCOUNT_STATUS.LOCKED:
            if self.last_failed_login and timezone.now() - self.last_failed_login > settings.LOCKOUT_DURATION:
                self.unlock_account()
                return False
            return True
        return False
    
    @property
    def full_name(self)->str:
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.title().strip()
    class meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        oredering = ["-date_joined"]

    def has_role(self, role_name:str)->bool:
        return hasattr(self, "role") and self.role == role_name
    
    def __str__(self):
        return f"{self.full_name}-{self.get_role_display()}"