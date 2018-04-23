import codecs
import os
import re
import sys
from setuptools import setup


if sys.version_info < (3, 5):
    raise RuntimeError("require Python 3.5+")


with codecs.open(os.path.join(os.path.abspath(os.path.dirname(
        __file__)), 'simple_search', '__init__.py'), 'r', 'utf-8') as fp:
    try:
        version = re.findall(r"^__version__ = '([^']+)'\r?$",
                             fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')


args = dict(
    name='simple_search',
    version=version,
    description='The simple full text search server',
    author='Volodymyr Kukushkin',
    author_email='volodymyr.kukushkin88@gmail.com',
    url='https://github.com/vkukushkin88/SimpleSearch.git',
    packages=['simple_search'],
    install_requires=[
        'flask-sqlalchemy==2.3.2',
        'flask-restful==0.3.6',
        'SQLAlchemy==1.2.4',
    ],
)

setup(**args)
