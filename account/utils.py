from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_activation_code(email, code, status):
    if status == 'register':
        context = {
            'text_detail': 'Спасибо за регистрацию',
            'email': email,
            'domain': 'http://localhost:8000',
            'code': code
        }
        message = f'Код активаций: {code}'

        send_mail(
            'Активация аккаунта',
            message,
            "alamanov.dev@gmail.com",
            [email],
            # html_message=msg_html,
            fail_silently=False
        )
    elif status == 'forgot_password':
        send_mail(
            'Востановления пароля',
            f"Код активаций: {code}",
            'animal@admin.com',
            [email],
            fail_silently=True,
        )