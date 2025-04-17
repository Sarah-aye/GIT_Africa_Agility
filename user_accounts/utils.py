from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


def send_password_reset_email(user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    reset_link = f"https://farmfoodhub.com/reset-password/{uid}/{token}/"

    subject = "Password Reset Request"
    message = f"Hi {user.first_name},\n\nClick the link below to reset your password:\n{reset_link}\n\nIf you didn't request this, you can ignore this email."

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )