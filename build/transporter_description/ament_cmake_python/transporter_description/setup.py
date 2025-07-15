from setuptools import find_packages
from setuptools import setup

setup(
    name='transporter_description',
    version='0.0.0',
    packages=find_packages(
        include=('transporter_description', 'transporter_description.*')),
)
