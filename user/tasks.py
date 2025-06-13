from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_verification_email(email, username):
    subject= 'Verify Your Email'
    message= f'Hello {username},\n\nPlease verify your email address by clicking the link below:\n\nhttp://example.com/verify?email={email}\n\nThank you!'
    send_mail(subject, message, 'noreply@example.com', [email])
    return f'Verification email sent to {email}'