from setuptools import setup

setup(
    name='pydoro',
    version='0.1',
    py_modules=['jarvis'],
    install_requires=[
        'click',
        'ffmpeg-python',
        'pydub',
        'emoji',
    ],
    entry_points='''
        [console_scripts]
        pydoro=pydoro:cli
    '''
)
