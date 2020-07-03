import datetime
import os
import subprocess
import time
from datetime import datetime as dt

import click
import emoji
from pydub.playback import PLAYER

DEFAULT_TIMER_DURATION = 25
image = emoji.emojize(':alarm_clock:', use_aliases=True)


def play_stop_timer():
    _supress_verbose_playback_output()


def _supress_verbose_playback_output():
    devnull = open(os.devnull, 'w')
    subprocess.call(
        [PLAYER, "-nodisp", "-autoexit", "-hide_banner", 'sounds/stop.mp3'],
        stdout=devnull, stderr=devnull)


@click.command()
@click.option('--until', default=DEFAULT_TIMER_DURATION,
              help='Set a timer until x mins')
def start_timer(until):
    start = dt.now()
    end = start + datetime.timedelta(minutes=until)
    current = dt.now()

    try:
        print_timer_until(current, end)
    except KeyboardInterrupt:
        print_session_end()
    finally:
        play_stop_timer()


def print_session_end():
    print()
    print('=' * 10)
    end_time = get_current_time()[0].lstrip("\r")
    print(f'Session ended at: {end_time}')


def print_timer_until(current, end):
    while current < end:
        formatted_time, current = get_current_time()
        print(formatted_time, end="")
        time.sleep(1)


def get_current_time():
    current = dt.now()
    return (
        f'\r{image} {current.hour}:{current.minute}:{current.second}', current)


if __name__ == '__main__':
    start_timer()
