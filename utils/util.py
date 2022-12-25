import random
from random import randint

from django.utils import timezone


def get_client_ip(request):
    if request is None:
        return None
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_user_device(request):
    return request.META['HTTP_USER_AGENT']


def get_next_id(model_class):
    items = model_class.objects.all().order_by('-id')
    if items.count() == 0:
        return 1
    return items[0].id + 1


default_chars = 'abcdefghijklmnopqrstuvwxyz0123456789'


def get_random_string(length, allowed_chars=default_chars):
    random_string = ""
    for i in range(length):
        random_string += random.choice(allowed_chars)
    return random_string


def get_secret_key():
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return get_random_string(50, chars)


def two_weeks_hence():
    return timezone.now() + timezone.timedelta(days=14)


def one_month_hence():
    return timezone.now() + timezone.timedelta(days=30)


def one_year_hence():
    return timezone.now() + timezone.timedelta(days=365)


def ten_years_hence():
    return timezone.now() + timezone.timedelta(days=3650)


def random_with_n_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


def diff(first, second):
    second = set(second)
    return [item for item in first if item not in second]


def xml_escape(string):
    string = string.replace('&lt;![CDATA[', '')
    string = string.replace(']]&gt;', '')
    string = string.replace('&', '&amp;')
    return string

def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return None
    for x in a:
        if not x.isdigit():
            return None
        i = int(x)
        if i < 0 or i > 255:
            return None
    return s