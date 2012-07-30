import os
from setuptools import setup, find_packages
import cmsplugin_markdown


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="cmsplugin-markdown",
    version=cmsplugin_markdown.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, django-cms, plugin, markdown, editor',
    author='Tobias Lorenz',
    author_email='tobias.lorenz@bitmazk.com',
    url="https://github.com/bitmazk/cmsplugin-markdown",
    packages=find_packages(),
    include_package_data=True,
)
