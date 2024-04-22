from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from news.models import Post, Category
from news_portal import settings
from django.utils import timezone
import datetime


@shared_task
def mailing_new_post(pk):
    post = Post.objects.get(pk=pk)
    categories = post.category.all()
    subscribers_emails = []

    for cat in categories:
        subscribers = cat.subscribers.all()
        subscribers_emails += [s.email for s in subscribers]

    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': post.preview(),
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=post.title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=['mzima905@gmail.com'],#subscribers
    )

    msg.attach_alternative(html_content, "text/html")  # добавляем html
    msg.send()


@shared_task
def mailing_on_mondays():
    today = timezone.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(datetime__gte=last_week)
    categories = set(posts.values_list('category__name', flat=True))
    subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))

    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )

    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=['mzima905@gmail.com'],  # subscribers
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

