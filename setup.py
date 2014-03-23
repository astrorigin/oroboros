#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""*Oroboros* is an astrology software written in Python.
It is based on the following modules:

  - AstroDienst's Swiss Ephemeris (pyswisseph_) version >= 1.74.00-0
  - Olson timezones (pytz_)
  - Qt toolkit (PyQt4_) version >= 4.3

Optionally:

  - Docutils_ version = 0.5
  - Mercurial_ (for distant charts repositories)
  - Supybot_ (for IRC plugin)

===========
What's new?
===========

  - Usual bug fixes
  - Additional asteroids: Eris, Sedna, Quaoar, Nessus, Varuna

========
Features
========

  - Charts: natal/radix, transits, progression, harmonics, profection
  - Open Astrolog or Skylendar charts too
  - Save charts as images in various formats (png, jpg, bmp, svg,...)
  - Query the online GeoNames.org_ atlas database
  - Calculates all planets, nodes
  - More than 300 fixed stars
  - Asteroids (Eris, Quaoar, Sedna, etc)
  - Uses Swiss, JPL, or Moshier Ephemeris 
  - A flexible and powerfull configuration system
  - Geocentric, topocentric, heliocentric or barycentric charts
  - Various house systems, including Gauquelin sectors
  - Tropical or sidereal zodiacs
  - Midpoints calculations and drawings
  - Format comments with Docutils_ reStructured Text
  - Synchronize your charts with a distant repository (using Mercurial_)
  - A few toys for IRC chat addicts (Supybot_ plugin)
  - And easy extension capabilities with the Python language...

.. _pyswisseph: http://pypi.python.org/pypi/pyswisseph
.. _pytz: http://pytz.sourceforge.net
.. _PyQt4: http://www.riverbankcomputing.co.uk/pyqt
.. _Docutils: http://docutils.sourceforge.net
.. _Mercurial: http://www.selenic.com/mercurial
.. _Supybot: http://supybot.com
.. _GeoNames.org: http://www.geonames.org

===============
Oroboros manual
===============

Installation
------------
Download and install the package and the required modules (most of them
are available in your distro repositories). For example, uncompress the latest
source package of *Oroboros* with ``tar jxf oroboros-xxxxxxxx.tar.bz2``, then
``cd oroboros-xxxxxxxx``, finally (with super-user permission) type ``python
setup.py install``.

Ephemeris files
~~~~~~~~~~~~~~~
You should also install the compressed ephemeris data files on your system
(``/usr/local/share/swisseph`` looks like a good idea). These files are freely
distributed on `AstroDienst public FTP server`_.

.. _`AstroDienst public FTP server`: ftp://ftp.astro.com/pub/swisseph/ephe

A simple installation would require that you download the following files,
allowing calculations over the period from 1800 to 2399:

  - ``sepl_18.se1``
  - ``semo_18.se1``
  - ``seas_18.se1``
  - ``fixstars.cat``
  - ``seorbel.txt``

You can also grab the following asteroids files (other asteroids can be
implemented on demand):

  - ``136199 Eris``
  - ``7066 Nessus``
  - ``50000 Quaoar``
  - ``90377 Sedna``
  - ``20000 Varuna``
  - ``128 Nemesis``

Usage
-----
If everything goes well you will be able to start the application by typing
``oroboros`` in your shell.

First steps
~~~~~~~~~~~
Update the configuration settings, especially the path to ephemeris files.
You may also create an aspects filter and an orbs filter for the midpoints
settings, otherwise you'll have some surprises.

========
Download
========
"""

import sys, os
from distutils.core import setup

VERSION = '20080712'


setup(
	# meta info
	name = 'oroboros',
	version = VERSION,
	description = 'Astrology software',
	long_description = __doc__,
	author = 'S.Marquis',
	author_email = 'stnsls@gmail.com',
	#url = 'http://oroboros.atarax.org',
	download_url = 'http://pypi.python.org/pypi/oroboros',
	classifiers = [
		'Development Status :: 3 - Alpha',
		'Environment :: X11 Applications :: Qt',
		'Intended Audience :: Religion',
		'Intended Audience :: Science/Research',
		'License :: OSI Approved :: GNU General Public License (GPL)',
		'Topic :: Religion',
		'Topic :: Scientific/Engineering :: Astronomy'
		],
	keywords = 'Astrology Ephemeris Swisseph',
	# files
	packages = [
		'oroboros',
		'oroboros.core',
		'oroboros.cli',
		'oroboros.gui',
		'oroboros.irc'
		],
	package_data = {
		'oroboros': ['*.txt'],
		'oroboros.core': [
			'*.sql',
			'*.txt'
			],
		'oroboros.gui': [
			'icons/*.png',
			'icons/zodiac/*.png',
			'icons/cusps/*.png',
			'icons/planets/*.png',
			'tr/*.qm',
			'tr/*.ts'
			],
		'oroboros.irc': ['*.txt']
		},
	scripts = [
		'bin/oroboros',
		'bin/oroboros-hg'
		],
	data_files = [
		('/usr/share/applications', ['share/oroboros.desktop']),
		('/usr/share/pixmaps', ['share/oroboros.png'])
		]
	)

# post install
if 'install' in sys.argv:
	try:
		os.system('update-desktop-database')
	except:
		pass


# End.
