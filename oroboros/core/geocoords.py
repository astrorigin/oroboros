#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Geographic coordinates and altitude.

NB: Use explicit direction indicator (N, S, E, W) to avoid confusion
related to positive/negative degrees.

Latitudes and longitudes:

	>>> print(Longitude())
	0:E:0:0
	>>> print(Latitude(3, 'S', 56))
	3:S:56:0
	>>> print(Longitude(8, 'e', 1, 33))
	8:E:1:33
	>>> print(Latitude(46, '+', 32)) # deprecated
	46:N:32:0
	>>> print(Longitude(13, 1, 2)) # deprecated
	13:E:2:0

Get floating point value of coordinates:

	>>> print(float(Longitude(6, 'w', 55)))
	-6.91666666667
	>>> print(float(Latitude(23, 'N', 35)))
	23.5833333333

Get decimal value of coordinates:

	>>> Latitude(52, 's', 33).to_decimal()
	Decimal("-52.55")
	>>> Longitude(123, 'e', 10).to_decimal()
	Decimal("123.166666667")

Addition and substraction with coords return new coords:

	>>> print(Latitude() + 3.5)
	3:N:30:0
	>>> print(Longitude(10) - 20)
	10:W:0:0
	>>> Latitude(45, 'n') + Latitude(20, 's')
	Latitude(25, 'N', 0, 0)
	>>> Longitude(120, 'w') - Longitude(19)
	Longitude(139, 'W', 0, 0)

Altitudes must be above sea level (0):

	>>> print(Altitude(500))
	500
	>>> Altitude()
	Altitude(0)

:todo: check coords is not superior to maximum (90:n:59 is invalid..)
:todo: better coords __add__, __sub__

"""

from decimal import Decimal


__all__ = ['Latitude', 'Longitude', 'Altitude']



class _Coords(object):
	"""Geographical coordinates base type."""
	
	__slots__ = ('_degrees', '_direction', '_minutes', '_seconds')
	
	def _get_degrees(self):
		"""Return coords degrees value.
		
		:rtype: int
		"""
		return self._degrees
	
	def _set_degrees(self, degrees):
		"""Check and set coordinates degrees.
		
		:raise Exception: not implemented
		"""
		raise Exception(NotImplemented)
	
	def _get_direction(self):
		"""Return coords direction (N/S/E/W).
		
		:rtype: str
		"""
		return self._direction
	
	def _set_direction(self, direction):
		"""Check and set coord direction.
		
		:raise Exception: not implemented
		"""
		raise Exception(NotImplemented)
	
	def _get_minutes(self):
		"""Return coords minutes value.
		
		:rtype: int
		"""
		return self._minutes
	
	def _set_minutes(self, minutes):
		"""Check and set coordinates minutes.
		
		:type minutes: numeric
		:raise ValueError: minutes not in range(60)
		"""
		minutes = int(minutes)
		if minutes < 0 or minutes > 59:
			raise ValueError('Coordinates minutes not in range(60).',
				minutes)
		self._minutes = minutes
	
	def _get_seconds(self):
		"""Return coords seconds value.
		
		:rtype: int
		"""
		return self._seconds
	
	def _set_seconds(self, seconds):
		"""Check and set coordinates seconds.
		
		:type seconds: numeric
		:raise ValueError: seconds not in range(60)
		"""
		seconds = int(seconds)
		if seconds < 0 or seconds > 59:
			raise ValueError('Coordinates seconds not in range(60).',
				seconds)
		self._seconds = seconds
	
	degrees = property(_get_degrees, _set_degrees,
		doc="Coordinates degrees.")
	direction = property(_get_direction, _set_direction,
		doc="Coordinates direction.")
	minutes = property(_get_minutes, _set_minutes,
		doc="Coordinates minutes.")
	seconds = property(_get_seconds, _set_seconds,
		doc="Coordinates seconds.")
	
	def set(self, deg=None, dir=None, min=None, sec=None):
		"""Set coordinates properties."""
		if deg != None:
			self.degrees = deg
		if dir != None:
			self.direction = dir
		if min != None:
			self.minutes = min
		if sec != None:
			self.seconds = sec
	
	def __init__(self, deg=None, dir=None, min=None, sec=None):
		"""Coordinates initialization.
		
		Default: '0:+:0:0'
		
			- 'deg' -> degrees
			- 'dir' -> direction
				- for latitudes:
					- 'N', 'n', '+' -> North
					- 'S', 's', '-' -> South
				- for longitudes:
					- 'E', 'e', '+' -> East
					- 'W', 'w', '-' -> West
			- 'min' -> minutes
			- 'sec' -> seconds
		
		"""
		if deg != None:
			self.degrees = deg
		else:
			self._degrees = 0
		self.direction = dir
		if min != None:
			self.minutes = min
		else:
			self._minutes = 0
		if sec != None:
			self.seconds = sec
		else:
			self._seconds = 0
	
	def __iter__(self):
		"""Return iterator over properties.
		
		:rtype: generator
		"""
		return (x for x in (self._degrees, self._direction, self._minutes,
			self._seconds))
	
	def __float__(self):
		"""Return floating point value of coordinates.
		
		:rtype: float
		"""
		if self._direction in ('N', 'E'):
			dir = '+'
		else:
			dir = '-'
		return float('%s%s' % (dir,
			str(self._degrees + (self._minutes/60.0) + (self._seconds/3600.0))))
	
	def to_decimal(self):
		"""Return decimal value of coordinates.
		
		:rtype: Decimal
		"""
		if self._direction in ('N', 'E'):
			dir = '+'
		else:
			dir = '-'
		return Decimal('%s%s' % (dir,
			str(self._degrees + (self._minutes/60.0) + (self._seconds/3600.0))))
	
	def from_decimal(self, value):
		"""Set coords from a decimal or float value."""
		value = Decimal(str(value))
		deg = int(value)
		self._set_degrees(deg)
		if deg < 0:
			self._set_direction('-')
		else:
			self._set_direction('+')
		dec = abs(value - Decimal(str(deg)))
		mins = int(dec * Decimal('60.0'))
		self._set_minutes(mins)
		sec = int((dec-(Decimal(str(mins))/Decimal('60.0')))*Decimal('3600.0'))
		self._set_seconds(sec)
		return self
	
	def __str__(self):
		"""Return coordinates as string (for database input).
		
		Example: '46:N:32:0'
		
		:rtype: str
		"""
		return "%s:%s:%s:%s" % (self._degrees, self._direction,
			self._minutes, self._seconds)
	
	def __repr__(self):
		return "_Coords(%s, '%s', %s, %s)" % (self._degrees,
			self._direction, self._minutes, self._seconds)
	
	def __getstate__(self):
		return {'_degrees': self._degrees,
			'_direction': self._direction,
			'_minutes': self._minutes,
			'_seconds': self._seconds}
	
	def __lt__(self, other):
		"""Return True if float value of coord < float value of other.
		
		:rtype: bool
		"""
		if other == None:
			return False
		if float(self) < float(other):
			return True
		return False
	
	def __le__(self, other):
		"""Return True if float value of coord <= float value of other.
		
		:rtype: bool
		"""
		if other == None:
			return False
		if float(self) <= float(other):
			return True
		return False
	
	def __eq__(self, other):
		"""Return True if float value of coord == float value of other.
		
		:rtype: bool
		"""
		if other == None:
			return False
		if float(self) == float(other):
			return True
		return False
	
	def __ne__(self, other):
		"""Return True if float value of coord != float value of other.
		
		:rtype: bool
		"""
		if other == None:
			return True
		if float(self) != float(other):
			return True
		return False
	
	def __gt__(self, other):
		"""Return True if float value of coord > float value of other.
		
		:rtype: bool
		"""
		if other == None:
			return False
		if float(self) > float(other):
			return True
		return False
	
	def __ge__(self, other):
		"""Return True if float value of coord >= float value of other.
		
		:rtype: bool
		"""
		if other == None:
			return False
		if float(self) >= float(other):
			return True
		return False
	
	def __add__(self, other):
		"""Return a new instance of coordinates, after addition operation.
		
		:type other: numeric or Decimal or type(self)
		:rtype: type(self)
		:raise TypeError: other type is invalid
		"""
		if not isinstance(other, (int, float, Decimal, type(self))):
			raise TypeError('Invalid type for coordinates addition.',
				type(other))
		if isinstance(other, (int, Decimal)):
			val = self.to_decimal() + other
		elif isinstance(other, float):
			val = self.to_decimal() + Decimal(str(other))
		elif isinstance(other, type(self)):
			val = self.to_decimal() + other.to_decimal()
		if val < 0:
			dir = '-'
		else:
			dir = '+'
		val = abs(val)
		deg = int(val)
		val -= deg
		min = int(val * 60)
		val -= Decimal(str(min / 60.0))
		sec = int(val * 3600)
		return type(self)(deg, dir, min, sec)
	
	def __sub__(self, other):
		"""Return a new instance of coordinates, after substraction operation.
		
		:type other: numeric or Decimal or type(self)
		:rtype: type(self)
		:raise TypeError: other type is invalid
		"""
		if not isinstance(other, (int, float, Decimal, type(self))):
			raise TypeError('Invalid type for coordinates substraction.',
				type(other))
		if isinstance(other, (int, Decimal)):
			val = self.to_decimal() - other
		elif isinstance(other, float):
			val = self.to_decimal() - Decimal(str(other))
		elif isinstance(other, type(self)):
			val = self.to_decimal() - other.to_decimal()
		if val < 0:
			dir = '-'
		else:
			dir = '+'
		val = abs(val)
		deg = int(val)
		val -= deg
		min = int(val * 60)
		val -= Decimal(str(min / 60.0))
		sec = int(val * 3600)
		return type(self)(deg, dir, min, sec)


class Latitude(_Coords):
	"""Latitude type.
	
	Default to '0:N:0:0'.
	
	"""
	
	__slots__ = _Coords.__slots__
	
	def _set_degrees(self, degrees):
		"""Check and set latitude degrees.
		
		:type degrees: numeric
		:raise ValueError: degrees not in range(-90, 91)
		"""
		degrees = abs(int(degrees))
		if degrees < 0 or degrees > 90:
			raise TypeError('Latitude degrees not in range(-90, 91).',
				degrees)
		self._degrees = degrees
	
	def _set_direction(self, direction):
		"""Check and set latitude direction (N/S).
		
		:type direction: str
		:raise ValueError: invalid direction
		"""
		if direction in (None, 'N', 'n', '+', 1):
			self._direction = 'N'
		elif direction in ('S', 's', '-', 0):
			self._direction = 'S'
		else:
			raise ValueError('Latitude direction not in ("N", "+", "S", "-").',
				direction)
	
	degrees = property(_Coords._get_degrees, _set_degrees,
		doc="Latitude degrees [-90;90].")
	direction = property(_Coords._get_direction, _set_direction,
		doc="Latitude direction (N/S).")
	minutes = property(_Coords._get_minutes, _Coords._set_minutes,
		doc="Latitude minutes [0;59].")
	seconds = property(_Coords._get_seconds, _Coords._set_seconds,
		doc="Latitude seconds [0;59].")
	
	def __repr__(self):
		return "Latitude(%s, '%s', %s, %s)" % (
			self._degrees, self._direction, self._minutes, self._seconds)


class Longitude(_Coords):
	"""Longitude type.
	
	Default to '0:E:0:0'.
	
	"""
	
	__slots__ = _Coords.__slots__
	
	def _set_degrees(self, degrees):
		"""Check and set longitude degrees.
		
		:type degrees: numeric
		:raise ValueError: degrees not in range(-180, 181)
		"""
		degrees = abs(int(degrees))
		if degrees < 0 or degrees > 180:
			raise ValueError('Longitude degrees not in range(-180, 181).',
				degrees)
		self._degrees = degrees
	
	def _set_direction(self, direction):
		"""Check and set longitude direction (E/W).
		
		:type direction: str
		:raise ValueError: invalid direction
		"""
		if direction in (None, 'E', 'e', '+', 1):
			self._direction = 'E'
		elif direction in ('W', 'w', '-', 0):
			self._direction = 'W'
		else:
			raise ValueError('Latitude direction not in ("E", "+", "W", "-").',
				direction)
	
	degrees = property(_Coords._get_degrees, _set_degrees,
		doc="Longitude degrees [-180;180].")
	direction = property(_Coords._get_direction, _set_direction,
		doc="Longitude direction (E/W).")
	minutes = property(_Coords._get_minutes, _Coords._set_minutes,
		doc="Longitude minutes [0;59].")
	seconds = property(_Coords._get_seconds, _Coords._set_seconds,
		doc="Longitude seconds [0;59].")
	
	def __repr__(self):
		return "Longitude(%s, '%s', %s, %s)" % (
			self._degrees, self._direction, self._minutes, self._seconds)



class Altitude(int):
	"""Altitude type, in meters above sea level (default 0)."""
	
	__slots__ = tuple()
	
	def __new__(cls, altitude=0):
		"""Init Altitude.
		
		:type altitude: numeric
		"""
		altitude = int(altitude)
		if altitude < 0:
			raise ValueError(altitude)
		return int.__new__(cls, altitude)
	
	def __repr__(self):
		return "Altitude(%s)" % self



def _test():
	import doctest
	doctest.testmod()


if __name__ == "__main__":
	_test()

# End.
