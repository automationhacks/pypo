import os
import subprocess

from pydub.playback import PLAYER

from config.base import TIMER_SOUND


def play_stop_timer():
    _suppress_verbose_playback_output()


def _suppress_verbose_playback_output():
    devnull = open(os.devnull, 'w')
    subprocess.call(
        [PLAYER, "-nodisp", "-autoexit", "-hide_banner", TIMER_SOUND],
        stdout=devnull, stderr=devnull)
