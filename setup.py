from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='qgeneration',
    version='0.0a1',
    description='Data generation project',
    long_description=long_description,
    url='https://github.com/KirovVerst/qgeneration',
    author='KirovVerst',
    author_email='kirov.verst@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.6',
    ],
    keywords=['data', 'generator', 'fixtures', 'test'],
    packages=find_packages(exclude=["docs", "tests"]),
)
