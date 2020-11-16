from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name = 'fdcomp',
    version = '0.0.1',
    url = 'https://github.com/AndreasAlbert/fdcomp',
    author = 'Andreas Albert',
    author_email = 'andreas.albert@cern.ch',
    description = 'Comparison utility for FitDiagnostics files.',
    packages = find_packages(),
    install_requires = requirements,
    scripts=[
        ],
)
