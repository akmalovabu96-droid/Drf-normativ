from celery import shared_task
from django.utils import timezone
from datetime import timedelta

from .models import Post

@shared_task
def check_old_posts():
    old_posts = Post.objects.filter(
        created_at__lt=timezone.now() - timedelta(minutes=1)
    )

    count = old_posts.count()

    print(f"Old posts found: {count}")

    return f"{count} old posts found"

@shared_task
def test_log():
    print("CELERY IS WORKING!")
    return "OK"