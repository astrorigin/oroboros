#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Timezone system.

The timezones are used to compute local mean time (and to
provide some more info about charts).

See:
 - http://www.worldtimezone.net/standard.html
 - http://en.wikipedia.org/wiki/Timezone

Implemented are nowadays standard timezones.
Historical timezones (eg. méridien de Paris) may easily be
added to the end of the list.
Please send any update to the software maintainer...

"""

__all__ = ['TimeZone',
	'all_timezones', 'get']


class TimeZone(object):
	"""Timezone object."""
	
	__slots__ = ('code', 'utc', 'offset', 'longitude')
	
	def __init__(self, code, utc, offset, longitude):
		"""Init TimeZone object.
		
		:type code: str
		:type utc: str
		:type offset: numeric
		:type longitude: numeric
		"""
		self.code = code # code name
		self.utc = utc # utc name
		self.offset = offset # offset
		self.longitude = longitude # longitude
	
	def __str__(self):
		"""Get a printable version of timezone.
		
		:rtype: str
		"""
		return '%s (%s)' % (self.code, self.utc)
	
	def __repr__(self):
		return 'TimeZone(%s, %s, %s, %s)' % (
			self.code, self.utc, self.offset, self.longitude)



all_timezones = [
# code   utc.code  offset longitude
	TimeZone('Z', 'UTC+0', 0, 0),
	TimeZone('A', 'UTC+1', 1, 15),
	TimeZone('B', 'UTC+2', 2, 30),
	TimeZone('C', 'UTC+3', 3, 45),
	TimeZone('C+', 'UTC+3:30', 3.5, 52.5), ## Iran
	TimeZone('D', 'UTC+4', 4, 60),
	TimeZone('D+', 'UTC+4:30', 4.5, 67.5), ## Afghanistan
	TimeZone('E', 'UTC+5', 5, 75),
	TimeZone('E+', 'UTC+5:30', 5.5, 62.5), ## India, etc
	TimeZone('E++', 'UTC+5:45', 5.75, 66.25), ## Nepal
	TimeZone('F', 'UTC+6', 6, 90),
	TimeZone('F+', 'UTC+6:30', 6.5, 97.5), ## Burma
	TimeZone('G', 'UTC+7', 7, 105),
	TimeZone('H', 'UTC+8', 8, 120),
	TimeZone('H++', 'UTC+8:45', 8.75, 131.25), ## Adelaide
	TimeZone('I', 'UTC+9', 9, 135),
	TimeZone('I+', 'UTC+9:30', 9.5, 142.5), ## Alice Springs
	TimeZone('K', 'UTC+10', 10, 150),
	TimeZone('K+', 'UTC+10:30', 10.5, 157.5), ## Lord Howe Isl.
	TimeZone('L', 'UTC+11', 11, 165),
	TimeZone('L+', 'UTC+11:30', 11.5, 172.5), ## Norfolk Isl.
	TimeZone('M', 'UTC+12', 12, 180),
	TimeZone('M++', 'UTC+12:45', 12.75, -169.75), ## Chatham Isl.
	TimeZone('M+', 'UTC+13', 13, -165), ## Phoenix Isl.
	TimeZone('M+', 'UTC+14', 14, -150), ## Line Isl.
	TimeZone('N', 'UTC-1', -1, -15),
	TimeZone('O', 'UTC-2', -2, -30),
	TimeZone('P', 'UTC-3', -3, -45),
	TimeZone('P+', 'UTC-3:30', -3.5, -52.5), ## Labrador
	TimeZone('Q', 'UTC-4', -4, -60),
	TimeZone('Q+', 'UTC-4:30', -4.5, -67.5), ## Venezuela
	TimeZone('R', 'UTC-5', -5, -75),
	TimeZone('S', 'UTC-6', -6, -90),
	TimeZone('T', 'UTC-7', -7, -105),
	TimeZone('U', 'UTC-8', -8, -120),
	TimeZone('V', 'UTC-9', -9, -135),
	TimeZone('V+', 'UTC-9:30', -9.5, -142.5), ## Marquesas Isl.
	TimeZone('W', 'UTC-10', -10, -150),
	TimeZone('X', 'UTC-11', -11, -165),
	TimeZone('Y', 'UTC-12', -12, -180)
]


def get(zone):
	"""Find corresponding TimeZone object for given Utc code name.
	
	:type zone: str
	:rtype: TimeZone
	:raise ValueError: not found
	"""
	for tz in all_timezones:
		if tz.utc == zone:
			return tz
	raise ValueError('Invalid utc zone %s.' % zone)


# End.
