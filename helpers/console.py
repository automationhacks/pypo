import time

from config.base import CLOCK_EMOJI
from helpers.time import get_local_or_utc_current_time, get_local_time


def print_timer_until(until):
    total_mins = until * 60
    while total_mins:
        mins, secs = divmod(total_mins, 60)
        time_format = f'\r {CLOCK_EMOJI}  ' + '{:02d}:{:02d}'.format(mins, secs)
        print(time_format, end="")
        time.sleep(1)
        total_mins -= 1


def print_session_end(task):
    print()
    end_time = get_local_or_utc_current_time(local=True)
    print(f'Stopped working on "{task}" at: {end_time}')


def print_work_log_to_console(index, record):
    task_no = index + 1
    day = record['day']
    task = record['task']

    started_at = get_local_time(day, record['started_at'])
    ended_at = get_local_time(day, record['ended_at'])

    print(
        f'#{task_no} Task: {task} '
        f'started at: {started_at} ended at: {ended_at}')
