from setuptools import setup, find_packages
from setuptools.command.test import test

class TestRunner(test):
    def run(self, *args, **kwargs):
        from runtests import runtests
        runtests()
setup(
    name='django-object-tools',
    version='0.0.1',
    description='Django app allowing to easily add admin object tools.',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Praekelt Foundation',
    author_email='dev@praekelt.com',
    url='http://github.com/praekelt/django-object-tools',
    packages = find_packages(),
    include_package_data=True,
    test_suite = "object_tools.tests",
    cmdclass={"test": TestRunner},
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)