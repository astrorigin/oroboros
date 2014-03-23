#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Objects holding calculations results.

Provides functions for searching, retrieving, sorting results.

"""

import swisseph as swe

from oroboros.core.planets import Planet


__all__ = ['Data', 'PlanetData', 'PlanetDataList',
	'HousesDataList', 'MidPointData', 'MidPointDataList']


class Data(object):
	"""Object holding positions information as given by swe.calc_ut function."""
	
	__slots__ = ('_longitude', '_latitude', '_distance',
		'_lonspeed', '_latspeed', '_distspeed')
	
	def _get_longitude(self):
		"""Get longitude.
		
		:rtype: float
		"""
		return self._longitude
	
	def _get_latitude(self):
		"""Get latitude.
		
		:rtype: float
		"""
		return self._latitude
	
	def _get_distance(self):
		"""Get distance.
		
		:rtype: float
		"""
		return self._distance
	
	def _get_lonspeed(self):
		"""Get longitude speed.
		
		:rtype: float
		"""
		return self._lonspeed
	
	def _get_latspeed(self):
		"""Get latitude speed.
		
		:rtype: float
		"""
		return self._latspeed
	
	def _get_distspeed(self):
		"""Get distance speed.
		
		:rtype: float
		"""
		return self._distspeed
	
	longitude = property(_get_longitude)
	latitude = property(_get_latitude)
	distance = property(_get_distance)
	lonspeed = property(_get_lonspeed)
	latspeed = property(_get_latspeed)
	distspeed = property(_get_distspeed)
	
	def __init__(self, res):
		"""Init data object with a swe.calc result or a single longitude.
		
		:type res: sequence or numeric
		"""
		if isinstance(res, (tuple, list)):
			self._longitude, self._latitude, self._distance = res[:3]
			self._lonspeed, self._latspeed, self._distspeed = res[3:]
		else:
			self._longitude, self._latitude, self._distance = (float(res), 0, 0)
			self._lonspeed, self._latspeed, self._distspeed = (0, 0, 0)
	
	def __repr__(self):
		return 'PointData((%s, %s, %s, %s, %s, %s))' % (
			self._longitude, self._latitude, self._distance, self._lonspeed,
			self._latspeed, self._distspeed)



class PlanetData(Data):
	"""One planet object and its positions."""
	
	__slots__ = ('_planet', '_longitude', '_latitude', '_distance',
		'_lonspeed', '_latspeed', '_distspeed')
	
	def _get_planet(self):
		"""Get Planet object.
		
		:rtype: Planet
		"""
		return self._planet
	
	def _set_planet(self, pl):
		"""Set Planet object.
		
		Accepts Planet objects, name or index.
		
		:type pl: Planet or str or int
		:raise ValueError: invalid planet
		"""
		if not isinstance(pl, Planet):
			try:
				pl = Planet(pl)
			except:
				raise ValueError('Invalid planet object %s.' % pl)
		self._planet = pl
	
	planet = property(_get_planet, _set_planet, doc='Planet object.')
	longitude = property(Data._get_longitude, doc='Longitude.')
	latitude = property(Data._get_latitude, doc='Latitude.')
	distance = property(Data._get_distance, doc='Distance.')
	lonspeed = property(Data._get_lonspeed, doc='Longitude speed.')
	latspeed = property(Data._get_latspeed, doc='Latitude speed')
	distspeed = property(Data._get_distspeed, doc='Distance speed.')
	
	def __init__(self, pl, res):
		"""Init planet data object.
		
		:type pl: Planet or str or int
		:type res: sequence or numeric
		"""
		Data.__init__(self, res)
		self.planet = pl
	
	def __repr__(self):
		return 'PlanetData(%s, (%s, %s, %s, %s, %s, %s))' % (
			repr(x) for x in (
			self._planet, self._longitude, self._latitude, self._distance,
			self._lonspeed, self._latspeed, self._distspeed))



class PlanetDataList(list):
	"""List of PlanetData objects."""
	
	def feed(self, pl, res):
		"""Append a planet data object.
		
		  - pl -> planet
		  - res -> calculation results (value from swisseph)
		
		:type pl: Planet or str or int
		:type res: sequence or numeric
		"""
		self.append(PlanetData(pl, res))
	
	def get_data(self, plname):
		"""Get data for a planet (given its name).
		
		:type plname: str
		:rtype: PlanetData
		:raise KeyError: planet not found
		"""
		for elem in self:
			if elem._planet._name == plname:
				return elem
		raise KeyError(item)
	
	def __contains__(self, plname):
		"""Return True if planet is in results.
		
		:rtype: bool
		"""
		for elem in self:
			if elem._planet._name == plname:
				return True
		return False
	
	def sort_by_ranking(self, reverse=False):
		"""Sort elements by planets display rank.
		
		:type reverse: bool
		:rtype: self
		"""
		self.sort(self._sort_by_ranking, reverse=reverse)
		return self
	
	@staticmethod
	def _sort_by_ranking(x, y):
		"""Function to sort elements by planets ranking."""
		try:
			if x._planet._ranking > y._planet._ranking:
				return 1
			elif x._planet._ranking < y._planet._ranking:
				return -1
			return 0
		except:
			if isinstance(x, MidPointData):
				_x = x._data1._planet._ranking
			else:
				_x = x._planet._ranking
			if isinstance(y, MidPointData):
				_y = y._data1._planet._ranking
			else:
				_y = y._planet._ranking
			if _x > _y:
				return 1
			elif _x < _y:
				return -1
			else:
				return 0
	
	# following functions will fail if mixed with midpoints
	
	def only_planets(self):
		"""Return a new results object with planets only (family 0).
		
		:rtype: PlanetDataList
		"""
		ret = PlanetDataList()
		for e in self:
			if e._planet._family == 0:
				ret.append(e)
		return ret
	
	def only_uranian(self):
		"""Return a new list with uranian/fictitious only (family 1).
		
		:rtype: PlanetDataList
		"""
		ret = PlanetDataList()
		for e in self:
			if e._planet._family == 1:
				ret.append(e)
		return ret
	
	def only_stars(self):
		"""Return a new list with stars only (family 2).
		
		:rtype: PlanetDataList
		"""
		ret = PlanetDataList()
		for e in self:
			if e._planet._family == 2:
				ret.append(e)
		return ret
	
	def only_asteroids(self):
		"""Return a new list with asteroids only (family 3).
		
		:rtype: PlanetDataList
		"""
		ret = PlanetDataList()
		for e in self:
			if e._planet._family == 3:
				ret.append(e)
		return ret
	
	def only_houses(self):
		"""Return a new list with houses only (family 4).
		
		:rtype: PlanetDataList
		"""
		ret = PlanetDataList()
		for e in self:
			if e._planet._family == 4:
				ret.append(e)
		return ret
	
	def only_parts(self):
		"""Return a new list with parts only (family 5).
		
		:rtype: PlanetDataList
		"""
		ret = PlanetDataList()
		for e in self:
			if e._planet._family == 5:
				ret.append(e)
		return ret


class HousesDataList(PlanetDataList):
	"""Object holding houses cusps & asc/mc results."""
	
	__slots__ = ('_hsys')
	
	def _get_hsys(self):
		"""Get house system.
		
		:rtype: str
		"""
		return self._hsys
	
	def _set_hsys(self, hsys):
		"""Set house system.
		
		:type hsys: str
		"""
		self._hsys = hsys

	hsys = property(_get_hsys, _set_hsys, doc='House system.')
	
	def __init__(self, cusps, ascmc, hsys):
		"""Initialize object with swe_houses results.
		
			>>> cusps, ascmc = swe.houses(2454595, 46.5, 6.5, 'P')
			>>> res = HousesDataList(cusps, ascmc, 'P')
		
		This procedure also computes additional values for descendant
		and Imum Coeli.
		
		:type cusps: sequence
		:type ascmc: sequence
		:type hsys: str
		"""
		self._hsys = hsys
		# cusps. get their planet objects
		if len(cusps) == 12:
			for i, num in enumerate(range(-100, -112, -1)):
				self.append(PlanetData(num, cusps[i]))
		elif len(cusps) == 36: # gauquelin
			for i, num in enumerate(range(-112, -148, -1)):
				self.append(PlanetData(num, cusps[i]))
		else:
			raise ValueError('Invalid cusps results.')
		# ascmc
		for i, num in enumerate(range(-148, -156, -1)):
			self.append(PlanetData(num, ascmc[i]))
		# additional dsc, ic
		self.insert(-6, PlanetData(-156, swe.degnorm(ascmc[0] - 180))) # dsc
		self.insert(-6, PlanetData(-157, swe.degnorm(ascmc[1] - 180))) # ic



class MidPointData(Data):
	"""Object holding mid-point data."""
	
	__slots__ = ('_data1', '_data2', '_longitude', '_latitude',
		'_distance', '_lonspeed', '_latspeed', '_distspeed')
	
	def _get_data1(self):
		"""Get planet 1 data.
		
		:rtype: PlanetData
		"""
		return self._pos
	
	def _set_data1(self, data):
		"""Set planet 1 data object.
		
		:type data: PlanetData
		:raise TypeError: invalid data
		"""
		if not isinstance(data, PlanetData):
			raise TypeError('Invalid planet data %s.' % data)
		self._data1 = data
	
	def _get_data2(self):
		"""Get planet 2 data.
		
		:rtype: PlanetData
		"""
		return self._data2
	
	def _set_data2(self, data):
		"""Set planet 2 data object.
		
		:type data: PlanetData
		:raise TypeError: invalid data
		"""
		if not isinstance(data, PlanetData):
			raise TypeError('Invalid planet data %s.' % data)
		self._data2 = data
	
	data1 = property(_get_data1, _set_data1,
		doc='Planet 1 data object.')
	data2 = property(_get_data2, _set_data2,
		doc='Planet 2 data object.')
	longitude = property(Data._get_longitude, doc='Longitude.')
	latitude = property(Data._get_latitude, doc='Latitude.')
	distance = property(Data._get_distance, doc='Distance.')
	lonspeed = property(Data._get_lonspeed, doc='Longitude speed.')
	latspeed = property(Data._get_latspeed, doc='Latitude speed')
	distspeed = property(Data._get_distspeed, doc='Distance speed.')
	
	def __init__(self, data1, data2, res):
		"""Init midpoint data.
		
		:type data1: PlanetData
		:type data2: PlanetData
		:type res: sequence or numeric
		"""
		Data.__init__(self, res)
		self.data1 = data1
		self.data2 = data2
	
	def __repr__(self):
		return 'MidPointData(%s, %s, (%s, %s, %s, %s, %s, %s))' % (
			repr(x) for x in (
			self._data1, self._data2, self._longitude, self._latitude,
			self._distance, self._lonspeed, self._latspeed, self._distspeed))



class MidPointDataList(list):
	"""List of mid-points data objects."""
	
	def feed(self, data1, data2, res):
		"""Append a mid-point data.
		
		:type data1: PlanetData
		:type data2: PlanetData
		:type res: sequence or numeric
		"""
		self.append(MidPointData(data1, data2, res))
	
	def get_data(self, pl1, pl2):
		"""Get data for a midpoint (given planets names).
		
		:type pl1: str
		:type pl2: str
		:raise KeyError: midpoint not found
		"""
		for elem in self:
			if elem._data1._planet._name == pl1 and elem._data2._planet._name == pl2:
				return elem
		raise KeyError((pl1, pl2))



def _test():
	import doctest
	doctest.testmod()


if __name__ == '__main__':
	_test()

# End.
