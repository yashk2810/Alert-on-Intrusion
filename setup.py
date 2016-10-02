from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Hack-Message',
    version='0.0.1',
    description='Sends you a sms and takes an image after every failed login attempt',
    long_description=long_description,
    url='https://github.com/yashk2810/Hack-Message',
    author='Yash Katariya',
    author_email='ykat95@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='message twilio',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['twilio','pygame','pygeoip'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    #package_data={
        # 'sample': ['package_data.dat'],
    # },
    # data_files=[('my_data', ['data/data_file'])],
    entry_points={
        'console_scripts': [
            'hack_message=hack_message:main',
        ],
    },
)
