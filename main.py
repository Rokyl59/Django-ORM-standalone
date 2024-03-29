import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard, Visit  # noqa: E402


if __name__ == '__main__':
    print('Всего пропусков:', Passcard.objects.count())  # noqa: T001

    active_user = Passcard.objects.filter(is_active=True)
    print(f'Активных пропусков: {len(active_user)}')

    user_not_leaved = Visit.objects.filter(leaved_at__isnull=True)
    print(user_not_leaved)
