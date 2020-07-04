from pathlib import Path

import emoji

DEFAULT_TIMER_DURATION = 25
DATE_FORMAT = '%Y-%m-%d'
TIME_FORMAT = '%H:%M:%S'
DATE_TIME_FORMAT = f'{DATE_FORMAT} {TIME_FORMAT}'
CLOCK_EMOJI = emoji.emojize(':alarm_clock:', use_aliases=True)
TAKE_A_BREAK_EMOJI = emoji.emojize(':running:', use_aliases=True)
WINK_EMOJI = emoji.emojize(':wink:', use_aliases=True)
USER_HOME = str(Path.home())
APP_FOLDER = '.pypo'
BASE_PATH = f'{USER_HOME}/{APP_FOLDER}'
DB_DIR = f'{BASE_PATH}/db'
DB_PATH = f'{DB_DIR}/timer.json'
TIMER_SOUND = f'{BASE_PATH}/sounds/stop.mp3'
