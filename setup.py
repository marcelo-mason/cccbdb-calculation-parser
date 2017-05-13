from setuptools import setup, find_packages

setup(
    name='cccbdb-geometry-parser',
    version='1.0',
    description=(
        'Pulls all geometry information from cccbdb.nist.gov for the specified chemical formula'),
    author='Ben',
    install_requires=[
        'beautifulsoup4==4.4.1',
        'requests==2.9.1',
        'grequests'
    ],
    author_email='phaedrus.one at the gmails',
    license='MIT',
    packages=find_packages(),
    zip_safe=False)
