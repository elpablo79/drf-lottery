from django.core.management.base import BaseCommand
from api.models import Prize, Contest, UserToContest
from django.contrib.auth.models import User
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Create random users'

    def handle(self, *args, **kwargs):
        prize1 = Prize.objects.create(code='five-percent_discount', perday=45, name='Sconto del 5%')
        prize2 = Prize.objects.create(code='ten-percent_discount', perday=20, name='Sconto del 10%')

        start = date.today().replace(day=1)
        end = last_day_of_month(start)

        contest1 = Contest.objects.create(code=f'C0001',
                               name='Vinci uno sconto',
                               start=start,
                               end=end,
                               prize=prize1)

        contest2 = Contest.objects.create(code=f'C0002',
                               name='Vinci uno sconto',
                               start=start - timedelta(days=60),
                               end=end - timedelta(days=60),
                               prize=prize2)

        User.objects.create_superuser('admin', 'admin@mail.com', 'admin').save()

        User.objects.create_user('user1', 'user1@gmail.com', '123456').save()
        User.objects.create_user('user2', 'user2@gmail.com', '123456').save()


        user1 = User.objects.filter(username='user1').first()

        UserToContest.objects.create(contest=contest1, user=user1)
        UserToContest.objects.create(contest=contest2, user=user1)

def last_day_of_month(input_day):
    next_month = input_day.replace(day=28) + timedelta(days=4)
    return next_month - timedelta(days=next_month.day)