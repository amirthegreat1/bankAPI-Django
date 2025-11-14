from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.translation import gettext_lazy as _
from loguru import logger


def send_otp_email(email, otp):
    subject = _("OTP Verification")
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    context = {
        "otp": otp,
        "expriry_time": settings.OTP_EXPIRY_TIME,
        "site_name": settings.SITE_NAME,
    }
