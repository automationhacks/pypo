import datetime
import json
import os
import subprocess
import time
from datetime import datetime as dt

import click
import emoji
from pydub.playback import PLAYER

DEFAULT_TIMER_DURATION = 25
DATE_FORMAT = '%Y-%m-%d'
TIME_FORMAT = '%H:%M:%S'
CLOCK_EMOJI = emoji.emojize(':alarm_clock:', use_aliases=True)


@click.group()
def cli():
    """Pydoro is your personal pomodoro timer and work log recorder"""
    pass


@cli.command()
@click.option('--until', default=DEFAULT_TIMER_DURATION,
              help='Set a timer until x mins')
@click.option('--task', default='',
              help='What are you working on in this block?')
def timer(until, task):
    work_record = init_work_record(task)

    try:
        print(f'Starting task => "{task}"')
        print_timer_until(until)
    except KeyboardInterrupt:
        print_session_end(task)
    finally:
        play_stop_timer()
        print('Logging your work..')
        print('Remember to take a break! ... Go out for a walk... ☮️ ')
        log_work(work_record)


def init_work_record(task):
    day = get_date()
    started_at = get_time()

    work_record = {
        'day': day,
        'started_at': started_at,
        'task': task
    }
    return work_record


def print_timer_until(until):
    in_mins = until * 60
    while in_mins:
        mins, secs = divmod(in_mins, 60)
        time_format = f'\r {CLOCK_EMOJI}  ' + '{:02d}:{:02d}'.format(mins, secs)
        print(time_format, end="")
        time.sleep(1)
        in_mins -= 1


def print_session_end(task):
    print()
    end_time = get_time(local=True)
    print(f'Stopped working on "{task}" at: {end_time}')


def log_work(work_record):
    work_record['ended_at'] = get_time()

    with open('db/timer.json', 'r+') as f:
        data = json.load(f)
        data['logs'].append(work_record)
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()


@cli.command()
@click.option('--for_day', default='today',
              help='print work log done so far (Choices: today, yesterday)')
def time_machine(for_day):
    with open('db/timer.json') as f:
        data = json.load(f)
        lookup_date = get_date_to_lookup_by(for_day)
        records = get_filtered_records(data, lookup_date)

        for index, record in enumerate(records):
            print_work_log_to_console(index, record)


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


def print_work_log_to_console(index, record):
    task_no = index + 1
    day = record['day']
    task = record['task']
    started = record['started_at']
    ended = record['ended_at']
    print(
        f'{task_no} Day: {day} Task: {task} '
        f'started at: {started} ended at: {ended}')


@cli.command()
@click.option("--data_for", default='all',
              help='how much db to flush from the work record')
def flush(data_for):
    print('Warning: This will remove all your work record db.')
    print('Do you still want to continue: [y/n]')
    user_input = str(input())
    if user_input == 'y':
        if data_for == 'all':
            template = """{"logs": []}"""
            with open('db/timer.json', 'w') as f:
                f.write(template)
            print('Your db has been reset. You have a clean slate again...')
    else:
        print('Good choice. Past is important to remember...')


def get_date():
    return dt.utcnow().strftime(DATE_FORMAT)


def get_time(local=False):
    if local:
        return dt.now().strftime(TIME_FORMAT)
    else:
        return dt.utcnow().strftime(TIME_FORMAT)


def play_stop_timer():
    _suppress_verbose_playback_output()


def _suppress_verbose_playback_output():
    devnull = open(os.devnull, 'w')
    subprocess.call(
        [PLAYER, "-nodisp", "-autoexit", "-hide_banner", 'sounds/stop.mp3'],
        stdout=devnull, stderr=devnull)


if __name__ == '__main__':
    time_machine()
