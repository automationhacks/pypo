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
image = emoji.emojize(':alarm_clock:', use_aliases=True)


@click.group()
def cli():
    """
    Your personal assistant.
    Try pomodoro timer --until 1 (default 25 mins)"""
    pass


@cli.command()
@click.option('--until', default=DEFAULT_TIMER_DURATION,
              help='Set a timer until x mins')
@click.option('--work_on', default='',
              help='What are you working on in this block?')
def timer(until, work_on):
    day = dt.utcnow().strftime('%Y-%m-%d')
    started_at = get_current_utc_time()
    work_record = {
        'day': day,
        'started_at': started_at,
        'task': work_on
    }

    start = dt.now()
    should_end_at = start + datetime.timedelta(minutes=until)
    current = dt.now()

    try:
        print(f'Starting work on: "{work_on}"')
        print_timer_until(current, should_end_at)
    except KeyboardInterrupt:
        print_session_end(work_on)
    finally:
        play_stop_timer()
        print('Logging your work.. Remember to take a break!')
        log_work(work_record)


@cli.command()
@click.option('--for_day', default='today',
              help='print work log done so far (Choices: today, yesterday)')
def past_work(for_day):
    with open('store/timer.json') as f:
        data = json.load(f)
        for index, record in enumerate(data['work_logs']):
            day = record['day']


            print(
                f'{index + 1} Day: {record["day"]} Task: {record["task"]} started at: {record["started_at"]} ended at: {record["ended_at"]}')


@cli.command()
@click.option("--data_for", default='all',
              help='how much data to flush from the work record')
def flush(data_for):
    print('Warning: This will remove all your work record data.')
    print('Do you still want to continue: [y/n]')
    user_input = str(input())
    if user_input == 'y':
        if data_for == 'all':
            template = """{"work_logs": []}"""
            with open('store/timer.json', 'w') as f:
                f.write(template)
            print('Your data has been reset. You have a clean slate again...')
    else:
        print('Good choice. Past is important to remember...')


def log_work(work_record):
    work_record['ended_at'] = get_current_utc_time()
    with open('store/timer.json', 'r+') as f:
        data = json.load(f)
        data['work_logs'].append(work_record)
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()


def get_current_utc_time():
    return dt.utcnow().strftime('%H:%M:%S')


def print_timer_until(current, end):
    while current < end:
        formatted_time, current = get_current_time()
        print(formatted_time, end="")
        time.sleep(1)


def print_session_end(work_on):
    print()
    print('=' * 10)
    end_time = get_current_time()[0].lstrip("\r")
    print(f'Stopped working on "{work_on}" at: {end_time}')


def get_current_time():
    current = dt.now()
    return (
        f'\r{image} {current.hour}:{current.minute}:{current.second}', current)


def play_stop_timer():
    _suppress_verbose_playback_output()


def _suppress_verbose_playback_output():
    devnull = open(os.devnull, 'w')
    subprocess.call(
        [PLAYER, "-nodisp", "-autoexit", "-hide_banner", 'sounds/stop.mp3'],
        stdout=devnull, stderr=devnull)


if __name__ == '__main__':
    timer()
