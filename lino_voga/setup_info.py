# -*- coding: UTF-8 -*-
# Copyright 2013-2016 Luc Saffre
# This file is part of Lino Voga.
#
# Lino Voga is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Lino Voga is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with Lino Voga.  If not, see
# <http://www.gnu.org/licenses/>.

SETUP_INFO = dict(
    name='lino_voga',
    version='0.0.4',
    install_requires=['lino', 'lino_cosi'],
    test_suite='tests',
    description="A Lino application for managing courses, "
    "participants and meeting rooms",

    long_description="""Lino Voga is a `Lino <http://www.lino-framework.org>`_
application for managing courses, participants and meeting rooms.

""",
    author='Luc Saffre',
    author_email='luc.saffre@gmail.com',
    url="http://voga.lino-framework.org",
    license='GNU Affero General Public License v3',
    classifiers="""\
Programming Language :: Python
Programming Language :: Python :: 2
Development Status :: 1 - Planning
Environment :: Web Environment
Framework :: Django
Intended Audience :: Developers
Intended Audience :: System Administrators
License :: OSI Approved :: BSD License
Operating System :: OS Independent
Topic :: Office/Business :: Scheduling
""".splitlines())

SETUP_INFO.update(packages=[
    'lino_voga',
    'lino_voga.lib',
    'lino_voga.lib.cal',
    'lino_voga.lib.cal.fixtures',
    'lino_voga.lib.contacts',
    'lino_voga.lib.contacts.fixtures',
    'lino_voga.lib.contacts.management',
    'lino_voga.lib.contacts.management.commands',
    'lino_voga.lib.courses',
    'lino_voga.lib.courses.fixtures',
    'lino_voga.lib.products',
    'lino_voga.lib.voga',
    'lino_voga.lib.voga.fixtures',
    'lino_voga.lib.rooms',
    'lino_voga.projects',
    'lino_voga.projects.docs',
    'lino_voga.projects.docs.settings',
    'lino_voga.projects.docs.tests',
    'lino_voga.projects.edmund',
    'lino_voga.projects.edmund.settings',
    'lino_voga.projects.edmund.settings.fixtures',
    'lino_voga.projects.roger',
    'lino_voga.projects.roger.settings',
    'lino_voga.projects.roger.settings.fixtures',
    'lino_voga.projects.roger.lib',
    'lino_voga.projects.roger.lib.courses',
    'lino_voga.projects.roger.lib.courses.fixtures',
    'lino_voga.projects.roger.lib.courses.management',
    'lino_voga.projects.roger.lib.courses.management.commands',
])

SETUP_INFO.update(message_extractors={
    'lino_voga': [
        ('**/cache/**',          'ignore', None),
        ('**.py',                'python', None),
        ('**.js',                'javascript', None),
        ('**/templates_jinja/**.html', 'jinja2', None),
    ],
})

SETUP_INFO.update(package_data=dict())


def add_package_data(package, *patterns):
    l = SETUP_INFO['package_data'].setdefault(package, [])
    l.extend(patterns)
    return l

#~ add_package_data('lino_voga',
  #~ 'config/patrols/Patrol/*.odt',
  #~ 'config/patrols/Overview/*.odt')

l = add_package_data('lino_voga')
for lng in 'de fr'.split():
    l.append('locale/%s/LC_MESSAGES/*.mo' % lng)