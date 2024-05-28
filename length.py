from setuptools import setup, find_packages

setup(
    name='unit_converter',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'unit_converter=unit_converter.converter:main',
        ],
    },
)
