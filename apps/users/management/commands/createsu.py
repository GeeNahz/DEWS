from typing import Any, Optional
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


User = get_user_model()


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args: Any, **options: Any) -> str | None:
        if not User.objects.filter(username='admin').exists():
            print('Creating superuser...')
            User.objects.create_superuser(
                username='admin',
                password='admin',
                email='admin@email.com',
            )
            print('Superuser has been created.')
        else:
            print('Superuser already exists. Skipping creating superuser.')
