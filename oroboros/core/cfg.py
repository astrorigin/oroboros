#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Configuration options.

Options are automaticly loaded at module import time.
Each is set at module's global scope.

Here is the list of user's options:

 - username -> user's name/nickname (str)
 - usermail -> user's email (str)
 - language -> user's language, for gui (str)
 - charts_dir -> directory where charts are stored (str)
 - use_docutils -> format strings with reStructured Text when possible (bool)
 - use_hg -> try to pull on startup and push on shutdown, using hg (bool)
 - hg_repo -> distant hg repo url (str)
 - hg_user -> hg username (str)
 - hg_pswd -> hg password (str)

For the default chart (here and now chart):

 - dft_name (str)
 - dft_location (str)
 - dft_country (str)
 - dft_zoneinfo (str)
 - dft_timezone (timezone.TimeZone)
 - dft_latitude (geocoords.Latitude)
 - dft_longitude (geocoords.Longitude)
 - dft_altitude (geocoords.Altitude)
 - dft_comment (str)
 - dft_filter (filters.Filter)

Still unused:

 - atlas_db -> path to sqlite atlas database (str)

Load config options:

	>>> load()

Get config options:

	>>> print(username)
	John Smith
	>>> print(atlas_db)
	~/.oroboros/atlas.db

Save config options:

	>>> save()

"""

from oroboros.core import db
from oroboros.core import geocoords
from oroboros.core import timezone
from oroboros.core.filters import Filter

import pytz


__all__ = ['load', 'save',
	'username', 'usermail', 'language', 'atlas_db', 'use_docutils',
	'use_hg', 'hg_repo', 'hg_user', 'hg_pswd',
	'dft_name', 'dft_location', 'dft_country', 'dft_zoneinfo', 'dft_timezone',
	'dft_latitude', 'dft_longitude', 'dft_altitude', 'dft_comment',
	'dft_filter']


# config options

username = 'John Smith'
usermail = 'johnsmith@nsa.gov'
language = ''
atlas_db = '~/.oroboros/atlas.db'
charts_dir = '~'

use_docutils = False
use_hg = False
hg_repo = 'http://hg.atarax.org/public'
hg_user = 'anonymous'
hg_pswd = 'password'

dft_name = 'Here-Now'
dft_location = 'Lausanne'
dft_country = 'Switzerland'
dft_zoneinfo = 'Europe/Zurich'
dft_timezone = timezone.get('UTC+1')
dft_latitude = geocoords.Latitude(46, 'N', 32)
dft_longitude = geocoords.Longitude(6, 'E', 40)
dft_altitude = geocoords.Altitude(400)
dft_comment = ''
dft_filter = Filter()



def load():
	"""Load configuration options from database (set globals)."""
	global username, usermail, language, atlas_db, charts_dir
	global use_docutils, use_hg, hg_repo, hg_user, hg_pswd
	global dft_name, dft_location, dft_country, dft_zoneinfo
	global dft_timezone, dft_latitude, dft_longitude, dft_altitude
	global dft_comment, dft_filter
	# load
	sql = "select * from Config;"
	res = db.execute(sql).fetchone()
	# set options
	username = res[0]
	usermail = res[1]
	language = res[2]
	atlas_db = res[3]
	charts_dir = res[4]
	use_docutils = bool(res[5])
	use_hg = bool(res[6])
	hg_repo = res[7]
	hg_user = res[8]
	hg_pswd = res[9]
	dft_name = res[10]
	dft_location = res[11]
	dft_country = res[12]
	if res[13] not in pytz.all_timezones:
		raise ValueError('Invalid timezone %s.' % res[13])
	else:
		dft_zoneinfo = res[13]
	dft_timezone = timezone.get(res[14]) if res[14] != '' else None
	dft_latitude = geocoords.Latitude(*res[15].split(':'))
	dft_longitude = geocoords.Longitude(*res[16].split(':'))
	dft_altitude = geocoords.Altitude(int(res[17]))
	dft_comment = res[18]
	dft_filter = Filter(int(res[19]))


def save():
	"""Save configuration options (globals) in database."""
	global username, usermail, language, atlas_db, charts_dir, dft_location
	global use_docutils, use_hg, hg_repo, hg_user, hg_pswd
	global dft_country, dft_zoneinfo, dft_timezone, dft_latitude
	global dft_longitude, dft_altitude, dft_filter
	# save
	sql = """update Config set username = ?, usermail = ?, language = ?,
		atlas_db = ?, charts_dir = ?, use_docutils = ?, use_hg = ?, hg_repo = ?,
		hg_user = ?, hg_pswd = ?, dft_location = ?, dft_country = ?,
		dft_zoneinfo = ?, dft_timezone = ?, dft_latitude = ?, dft_longitude = ?,
		dft_altitude = ?, dft_filter = ?;"""
	var = (username, usermail, language, atlas_db, charts_dir,
		int(use_docutils), int(use_hg), hg_repo, hg_user, hg_pswd,
		dft_location, dft_country, dft_zoneinfo,
		dft_timezone.utc if dft_timezone != None else '', str(dft_latitude),
		str(dft_longitude), dft_altitude, dft_filter._idx_)
	db.execute(sql, var)



def _test():
	import doctest
	doctest.testmod()


if __name__ == "__main__":
	_test()
else: # get config options
	load()

# End.
