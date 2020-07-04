import datetime
import json

from config.base import DATE_FORMAT, DB_PATH
from helpers.time import get_date, get_local_or_utc_current_time


def init_work_record(task):
    day = get_date()
    started_at = get_local_or_utc_current_time()

    work_record = {
        'day': day,
        'started_at': started_at,
        'task': task
    }
    return work_record


def log_work(work_record):
    work_record['ended_at'] = get_local_or_utc_current_time()

    with open(DB_PATH, 'r+') as f:
        data = json.load(f)
        data['logs'].append(work_record)
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()


def get_date_to_lookup_by(for_day):
    if for_day == 'today':
        lookup_date = get_date()
    elif for_day == 'yesterday':
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        lookup_date = yesterday.strftime(DATE_FORMAT)
    else:
        lookup_date = None
    return lookup_date


def get_filtered_records(data, lookup_date):
    if lookup_date:
        records = [record for record in data['logs'] if
                   record['day'] == lookup_date]
    else:
        records = data['logs']
    return records
