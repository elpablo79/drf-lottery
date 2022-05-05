from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Contest(models.Model):
    code = models.CharField(max_length=10, null=False, blank=False, unique=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    start = models.DateField(null=False)
    end = models.DateField(null=False)
    prize = models.ForeignKey('api.Prize', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.code + '-' + self.name


class Prize(models.Model):
    code = models.CharField(max_length=30, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    perday = models.IntegerField(null=False)

    def __str__(self):
        return self.code + '-' + self.name


class WinPerDay(models.Model):
    day = models.DateField(datetime.now())
    contest = models.ForeignKey('api.Contest', null=False, on_delete=models.CASCADE)
    winnings = models.IntegerField(default=0)
    attempts = models.IntegerField(default=0)


class UserToContest(models.Model):
    contest = models.ForeignKey('api.Contest', null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + '-' + self.contest.code


class UserWinningsPerDay(models.Model):
    day = models.DateField(auto_now_add=True)
    winnings = models.IntegerField(default=1)
    contest = models.ForeignKey('api.Contest', null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ("user", "contest", "day"),
                name = "unique_user_contest_date",
            ),
        ]

    def __str__(self):
        return f'{self.user.username} | {self.contest.code}, Winnings ({self.winnings})'

