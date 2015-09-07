from setuptools import setup
from setuptools import find_packages


setup(
    name='multable',
    version='0.1',
    description='multiplication tables generator',
    author='Walid Saad',
    author_email='walid.sa3d@gmail.com',
    url='github.com/walidsa3d/multable',
    py_modules=['multable'],
    classifiers=['Development Status :: 5 - Production/Stable', 'Environment :: Console'],
    include_package_data=True,
    package_data={'multable': ['LICENSE']},
    packages=find_packages(exclude=['test', 'tests']),
    long_description='generator for multiplication tables of any size',
)
