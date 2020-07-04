from datetime import datetime as dt, datetime

from dateutil import tz

from config.base import DATE_FORMAT, TIME_FORMAT, DATE_TIME_FORMAT


def get_date():
    return dt.utcnow().strftime(DATE_FORMAT)


def get_local_or_utc_current_time(local=False):
    if local:
        return dt.now().strftime(TIME_FORMAT)
    else:
        return dt.utcnow().strftime(TIME_FORMAT)


def get_local_time(day, time):
    local_time = utc_to_local(day, time)
    return get_time(local_time)


def utc_to_local(day, time):
    date_time = f'{day} {time}'
    utc = datetime.strptime(date_time, DATE_TIME_FORMAT)
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    utc_timezone = utc.replace(tzinfo=from_zone)
    return utc_timezone.astimezone(to_zone)


def get_time(timestamp):
    return f'{timestamp.hour}:{timestamp.minute}:{timestamp.second}'
