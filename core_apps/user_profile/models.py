from typing import Any

from cloudinary.models import CloudinaryField
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from core_apps.common.models import TimeStampedModel

User = get_user_model()


class Profile(TimeStampedModel):
    class Salutation(models.TextChoices):
        MR = "MR", _("Mr.")
        MRS = "MRS", _("Mrs.")
        MISS = "MISS", _("Miss")

    class Gender(models.TextChoices):
        MALE = "MALE", _("Male")
        FEMALE = "FEMALE", _("Female")

    class MaritalStatus(models.TextChoices):
        SINGLE = "SINGLE", _("Single")
        MARRIED = "MARRIED", _("Married")
        WIDDOW = "WIDDOW", _("Widdow")
        DEVORCED = "DEVORCED", _("Devorced")
        UNKOWN = "UNKOWN", _("Unkown")

    class Identificationmeans(models.TextChoices):
        NATIONAL_ID = "NATIONAL_ID", _("National ID")
        PASSPORT = "PASSPORT", _("Passport")
        DRIVER_LICENSE = "DRIVER_LICENSE", _("Driver License")

    class EmploymentStatus(models.Textchoices):
        SELF_EMPLOYED = "SELF_EMPLOYED", _("Self Employed")
        EMPLOYED = "EMPLOYED", _("Employed")
        UNEMPLOYED = "UNEMPLOYED", _("Unemployed")
        RETIRED = "RETIRED", _("Retired")
        STIDENT = "STUDENT", _("Student")

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    title = models.CharField(
        _("Salutation"), max_length=5, choices=Salutation.choices, default=Salutation.MR
    )
    gender = models.CharField(_("Gender"), max_length=8, choices=Gender.choices)
    birth_date = models.DateField(
        _("Date of Birth"), default=settings.DEFUALT_BIRTH_DATE
    )
    birth_country = CountryField(
        _("Country of Birth"), default=settings.DEFUALT_COUNTRY
    )
    birth_place = models.CharField(
        _("Place of Birth"), max_length=50, default="Unknown"
    )
    marital_status = models.CharField(
        _("Marital Status"),
        max_length=20,
        choices=MaritalStatus.choices,
        default=MaritalStatus.UNKOWN,
    )
    identification_means = models.CharField(
        _("Identification Means"),
        max_length=20,
        choices=Identificationmeans.choices,
        default=Identificationmeans.NATIONAL_ID,
    )
    id_issue_date = models.DateField(
        _("ID or Passport Issue Date"), default=settings.DEFUALT_DATE
    )
    id_expiry_date = models.DateField(
        _("ID or Passport Expiry Date"), default=settings.DEFUALT_EXPIRY_DATE
    )
    passport_number = models.CharField(
        _("Passport Number"), max_length=30, null=True, blank=True
    )
    nationality = models.CharField(_("Nationality"), max_length=30, default="Unknown")
    phone_number = PhoneNumberField(
        _("Phone Number"), default=settings.DEFUALT_PHONE_NUMBER
    )
    address = models.CharField(_("Address"), max_length=100, default="Unknown")
    city = models.CharField(_("City"), max_length=30, default="Unknown")
    country = CountryField(_("Country"), default=settings.DEFUALT_COUNTRY)
    employment_status = models.CharField(
        _("Employment Status"),
        max_length=30,
        choices=EmploymentStatus.choices,
        default=EmploymentStatus.UNEMPLOYED,
    )
    employer_name = models.CharField(
        _("Employer Name"), max_length=30, null=True, blank=True
    )
    annual_income = models.DecimalField(
        _("Annual Income"), max_digits=15, decimal_places=2, default=0.00
    )
    date_of_employment = models.DateField(
        _("Date of Employment"), default=settings.DEFUALT_DATE
    )
    employer_address = models.CharField(
        _("Employer Address"), max_length=100, null=True, blank=True
    )
    employer_city = models.CharField(
        _("Employer City"), max_length=30, null=True, blank=True
    )
    employer_country = CountryField(_("Employer Country"), null=True, blank=True)
    photo = CloudinaryField(_("Photo"), null=True, blank=True)
    photo_url = models.URLField(_("Photo URL"), blank=True, null=True)
    id_photo = CloudinaryField(
        _("ID Photo"), default="default.jpg", null=True, blank=True
    )
    id_photo_url = models.URLField(_("ID Photo URL"), blank=True, null=True)
    signature_photo = CloudinaryField(_("Signiture Photo"), null=True, blank=True)
    signature_photo_url = models.URLField(
        _("Signiture Photo URL"), blank=True, null=True
    )

    def clean(self) -> None:
        cleaned_data = super().clean()
        if self.id_issue_date and self.id_expiry_date:
            if self.id_issue_date > self.id_expiry_date:
                raise ValidationError(
                    _(
                        "ID or Passport Issue Date cannot be greater than ID or Passport Expiry Date"
                    )
                )

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.full_clean()
        super().save(*args, **kwargs)

    def is_complete_with_next_of_kin(self):
        required_fields = [
            self.title,
            self.gender,
            self.birth_date,
            self.birth_country,
            self.birth_place,
            self.marital_status,
            self.identification_means,
            self.id_issue_date,
            self.id_expiry_date,
            self.nationality,
            self.phone_number,
            self.address,
            self.city,
            self.country,
            self.employment_status,
            self.photo,
            self.id_photo,
            self.signature_photo,
        ]
        return all(required_fields) and self.next_of_kin.exists()

    def __str__(self):
        return f"{self.title} {self.user.first_name} {self.user.last_name}'s Profile"


class NextOfKin(TimeStampedModel):
    class Salutation(models.TextChoices):
        MR = "MR", _("Mr.")
        MRS = "MRS", _("Mrs.")
        MISS = "MISS", _("Miss")

    class Gender(models.TextChoices):
        MALE = "MALE", _("Male")
        FEMALE = "FEMALE", _("Female")

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="next_of_kin",
        verbose_name=_("Profile"),
    )
    title = models.CharField(_("Title"), max_length=10, choices=Salutation.choices)
    first_name = models.CharField(_("First Name"), max_length=30)
    last_name = models.CharField(_("Last Name"), max_length=30)
    other_names = models.CharField(
        _("Other Names"), max_length=30, blank=True, null=True
    )
    birth_date = models.DateField(_("Birth Date"))
    gender = models.CharField(_("Gender"), max_length=10, choices=Gender.choices)
    relationship = models.CharField(_("Relationship"), max_length=30)
    email_address = models.EmailField(_("Email Address"), db_index=True)
    phone_number = PhoneNumberField(_("Phone Number"))
    address = models.CharField(_("Address"), max_length=100)
    city = models.CharField(_("City"), max_length=30)
    country = CountryField(_("Country"))
    is_primary = models.BooleanField(_("Is Primary"), default=False)

    def clean(self) -> None:
        super().clean()
        if self.is_primary:
            primary_kin = NextOfKin.objects.filter(
                profile=self.profile, is_primary=True
            ).exclude(pk=self.pk)
            if primary_kin.exists():
                raise ValidationError(_("There can only be one primary next of kin."))

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} - Next of Kin for {self.profile.user.full_name}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["profile", "is_primary"],
                condition=models.Q(is_primary=True),
                name="unique_primary_next_of_kin",
            )
        ]
