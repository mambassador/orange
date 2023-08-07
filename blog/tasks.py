from celery import shared_task

from core import settings

from django.core.mail import send_mail


@shared_task
def new_post_mail_to_admin(to_email, message, subject="New post to approve") -> None:
    """Sends a notification email.

    Args:
        subject(str): the message subject
        to_email(List[str]): list of recipient email addresses
        message(str): the message content
    """
    send_mail(
        subject,
        message,
        settings.NOREPLY_EMAIL,
        to_email,
        fail_silently=False,
    )


@shared_task
def new_comment_mail_to_admin(to_email, message, subject="New comment to approve") -> None:
    """Sends a notification email.

    Args:
        subject(str): the message subject
        to_email(List[str]): list of recipient email addresses
        message(str): the message content
    """
    send_mail(
        subject,
        message,
        settings.NOREPLY_EMAIL,
        to_email,
        fail_silently=False,
    )


@shared_task
def new_comment_mail_to_user(to_email, message, subject="You have new comment") -> None:
    """Sends a notification email.

    Args:
        subject(str): the message subject
        to_email(List[str]): list of recipient email addresses
        message(str): the message content
    """
    send_mail(
        subject,
        message,
        settings.NOREPLY_EMAIL,
        to_email,
        fail_silently=False,
    )


@shared_task
def new_contact_request_to_admin(from_email, to_email, message, subject="New comment to approve") -> None:
    """Sends a notification email.

    Args:
        from_email(str): the email author
        subject(str): the message subject
        to_email(List[str]): list of recipient email addresses
        message(str): the message content
    """
    send_mail(
        subject,
        message,
        from_email,
        to_email,
        fail_silently=False,
    )
