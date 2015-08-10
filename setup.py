__author__ = 'khatcher'

import os

from setuptools import setup, find_packages


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='voc',
    version='0.0.3',
    install_requires=[
        "beautifulsoup4",
        "blinker",
        "boto",
        "Cerberus",
        "dominate",
        "elasticsearch",
        "Eve",
        "Eve-Mongoengine",
        "Events",
        "Flask",
        "Flask-Admin",
        "flask-admin-s3-upload",
        "Flask-Bootstrap",
        "Flask-Classy",
        "Flask-Elasticsearch",
        "Flask-Menu",
        "flask-mongoengine",
        "Flask-PyMongo",
        "Flask-QRcode",
        "Flask-Script",
        "Flask-WTF",
        "iso8601",
        "itsdangerous",
        "Jinja2",
        "MarkupSafe",
        "mongoengine",
        "noaaweather",
        "nose",
        "nose-mongoengine",
        "Pillow",
        "pymongo",
        "qrcode",
        "simplejson",
        "six",
        "url-for-s3",
        "urllib3",
        "Werkzeug",
        "WTForms",
        ],
    description='Web based virutal operations center for tactical or emergencies',
    long_description=(read('README.rst') + '\n\n' +
                      read('HISTORY.rst') + '\n\n' +
                      read('AUTHORS.rst')),
    url='https://github.com/kerryhatcher/voc',
    license='GNU AFFERO GPL v3',
    author='Kerry Hatcher',
    author_email='hs@ox.cx',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Other Audience',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
