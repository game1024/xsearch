import datetime

def is_within_days(the_time, days):
    current = datetime.datetime.now()
    the_days_ago = current - datetime.timedelta(days=days)
    if the_days_ago <= the_time <= current:
        return True
    else:
        return False

def is_within_seconds(the_time, seconds):
    current = datetime.datetime.now()
    the_seconds_ago = current - datetime.timedelta(seconds=seconds)
    if the_seconds_ago <= the_time <= current:
        return True
    else:
        return False

def is_within_hours(the_time, hours):
    current = datetime.datetime.now()
    the_hours_ago = current - datetime.timedelta(hours=hours)
    if the_hours_ago <= the_time <= current:
        return True
    else:
        return False

def is_within_7_days(the_time):
    return is_within_days(the_time, 7)


def is_within_30_days(the_time):
    return is_within_days(the_time, 30)