from api.models import Contest, WinPerDay, UserWinningsPerDay
from django.db.models import F
from datetime import date
from api import exceptions
import random
import math


def get_code(request):
    try:
        return request.GET['contest']
    except Exception:
        raise exceptions.ContestCodeRequiredException()


def get_user_id(request):
    user_id = request.GET.get('user_id', None)
    if not user_id:
        return

    return user_id


def get_contest(contest_code):
    try:
        return Contest.objects.get(code=contest_code)
    except Contest.DoesNotExist:
        raise exceptions.ContestNotFoundException(contest_code)


def check_contest_validity(contest):
    now = date.today()
    if not contest.start <= now <= contest.end:
        raise exceptions.ContestNotActiveException(contest.code)


def get_prizes_remaining(contest):
    win_per_day = WinPerDay.objects.filter(contest__code=contest.code, day=date.today()).first()
    if not win_per_day:
        win_per_day = WinPerDay.objects.create(day=date.today(), contest=contest)
    return win_per_day


def is_prize_available(win_per_day, contest):
    return win_per_day.winnings < contest.prize.perday


def probability_to_win(contest):
    requests_h = n_requests_estimate(contest.prize.perday) / 24
    prizes_h = contest.prize.perday / 24
    probability = prizes_h / requests_h
    return probability


def has_won(contest, win_per_day, user_id):
    probability = probability_to_win(contest)
    occasion = random.random()
    boost = 0

    if win_per_day.attempts > n_requests_estimate(contest.prize.perday) * 0.9 and win_per_day.winnings < contest.prize.perday:
        boost = 0.2

    winning = occasion - boost < probability
    if winning and contest.wmax_per_user is not None:
        increase_user_winnings(contest, user_id)

    return winning


def increase_total_winnings(win_per_day):
    win_per_day.winnings = F("winnings") + 1
    win_per_day.attempts = F("attempts") + 1
    win_per_day.save()


def increase_attempts(win_per_day):
    win_per_day.attempts = F("attempts") + 1
    win_per_day.save()


def n_requests_estimate(winnings):
    return math.pow(winnings, 2)


def increase_user_winnings(contest, user_id):
    user_winnings, _ = UserWinningsPerDay.objects.get_or_create(contest=contest, day=date.today(), user_id=user_id)
    user_winnings.winnings = F('winnings') + 1
    user_winnings.save()


def can_win(contest, user_id):
    if user_id:
        user_winnings = UserWinningsPerDay.objects.filter(contest=contest, day=date.today(), user_id=user_id).first()

        if not user_winnings or user_winnings.winnings <= contest.wmax_per_user:
            return

        raise exceptions.WinningsExceededException()