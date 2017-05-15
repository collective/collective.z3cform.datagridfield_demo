# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

import os


version = '0.7.dev0'

setup(
    name='collective.z3cform.datagridfield_demo',
    version=version,
    description="Demo DataGridField for Plone/Dexterity",
    long_description=(
        open("README.rst").read() +
        '\n' +
        open(os.path.join("docs", "HISTORY.txt")).read(),
    ),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='Plone, Dexterity, z3c.form, datagridfield widget',
    author='Kevin Gill',
    author_email='kevin@movieextras.ie',
    url='https://github.com/collective/collective.z3cform.datagridfield_demo',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.z3cform'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'five.grok',
        'collective.z3cform.datagridfield',
    ],
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
