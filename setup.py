from setuptools import setup

setup(
    name='pypo',
    version='0.1',
    py_modules=['pypo'],
    install_requires=[
        'click',
        'ffmpeg-python',
        'pydub',
        'emoji',
    ],
    entry_points='''
        [console_scripts]
        pypo=pypo:cli
    '''
)
