import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='Flask-Neo4j-Driver',
    version='0.1',
    url='https://github.com/deanwetherby/flask-neo4j-driver',
    license='GPLv3',
    author='Dean Wetherby',
    author_email='dean.wetherby@gmail.com',
    description='Flask extension for neo4j',
    long_description=read('README.md'),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['flask', 'neo4j-driver'],
    classifiers=[
        'Environment :: Web Environment', 'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English', 'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='flask neo4j',
    python_requires='>=3.6')
