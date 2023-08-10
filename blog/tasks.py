from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_contact_email(first_name, last_name, email, message):
    subject = "New Contact Form Submission"
    body = f"Name: {first_name} {last_name}\nEmail: {email}\nMessage: {message}"
    from_email = {email}
    recipient_list = ["admin@orange.com"]
    send_mail(subject, body, from_email, recipient_list)
