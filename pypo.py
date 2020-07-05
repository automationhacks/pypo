import json
import os

import click

from config.base import *
from config.strings import BASE_TIMER_CMD
from helpers.console import print_timer_until, print_session_end, \
    print_work_log_to_console
from helpers.file import create_base_db
from helpers.sound import play_stop_timer
from helpers.work_logger import get_date_to_lookup_by, get_filtered_records, \
    log_work, init_work_record


@click.group()
def cli():
    """Pypo is your personal pomodoro timer and work log recorder"""
    if not os.path.isdir(DB_DIR):
        os.makedirs(DB_DIR)

    is_db_file_present = os.path.isfile(DB_PATH)
    if not is_db_file_present:
        create_base_db()


@cli.command()
@click.option('--until', default=DEFAULT_TIMER_DURATION,
              help='Set a timer until x mins')
@click.option('--task', default='',
              help='What are you working on in this block?')
def timer(until, task):
    work_record = init_work_record(task)

    try:
        print(f'Starting task => "{task}" {WINK_EMOJI}')
        print('Press Ctrl + C to exit ... ')
        print()
        print_timer_until(until)
    except KeyboardInterrupt:
        print_session_end(task)
    finally:
        play_stop_timer()
        print('\nLogging your work..')
        print(
            f'Good job. Remember to take a break now! ... {TAKE_A_BREAK_EMOJI}️ ')
        print(f'Take a walk, have water and breathe ... ')
        log_work(work_record)


@cli.command()
@click.option('--for_day', default='today',
              help='print work log done so far (Choices: today, yesterday)')
def time_machine(for_day):
    with open(DB_PATH) as f:
        data = json.load(f)
        if not data['logs']:
            print('You have not done any work yet!')
            print('0 RECORDS FOUND')
            print(f'Hint: Try {BASE_TIMER_CMD}')
            return

        lookup_date = get_date_to_lookup_by(for_day)
        records = get_filtered_records(data, lookup_date)

        print(f"Work log for Day: {records[0]['day']}")
        print('---------------' * 2)
        print(f'{len(records)} RECORDS FOUND')
        for index, record in enumerate(records):
            print_work_log_to_console(index, record)


@cli.command()
@click.option("--data_for", default='all',
              help='how much db to flush from the work record')
def flush(data_for):
    print('Warning: This will remove all your work record db.')
    print('Do you still want to continue: [y/n]')
    user_input = str(input()).lower()
    if user_input == 'y':
        if data_for == 'all':
            create_base_db()
            print('Your db has been reset. You have a clean slate again...')
    else:
        print('Good choice. Past is important to remember...')


if __name__ == '__main__':
    cli()
