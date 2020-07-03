from setuptools import setup

setup(
    name='jarvis',
    version='0.1',
    py_modules=['pomodoro'],
    install_requires=[
        'click',
        'ffmpeg-python',
        'pydub',
        'emoji',
    ],
    entry_points='''
        [console_scripts]
        pomodoro=pomodoro:cli
    '''
)
