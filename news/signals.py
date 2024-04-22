from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from dotenv import load_dotenv

from .models import PostCategory
from .tasks import mailing_new_post

load_dotenv()


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        mailing_new_post(instance.pk)


