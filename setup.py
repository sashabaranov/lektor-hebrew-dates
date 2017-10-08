from setuptools import setup

setup(
    name='lektor-hebrew-dates',
    version='0.1',
    author='AB',
    author_email='_',
    license='MIT',
    py_modules=['lektor_hebrew_dates'],
    entry_points={
        'lektor.plugins': [
            'hebrew-dates = lektor_hebrew_dates:HebrewDatesPlugin',
        ]
    },
    install_requires=['jewish']
)
