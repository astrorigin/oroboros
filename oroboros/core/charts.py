#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Chart objects.

"""

from oroboros.core.chartcalc import ChartCalc
from oroboros.core.aspectsresults import AspectDataList
from oroboros.core.results import PlanetDataList


__all__ = ['Chart']


class Chart(ChartCalc):
	"""Chart object including display and drawing helpers."""
	
	__slots__ = ChartCalc.__slots__ + ['_hidden']
	
	def _get_hidden(self):
		"""Get hidden flag.
		
		:rtype: bool
		"""
		return self._hidden
	
	def _set_hidden(self, boolean):
		"""Set hidden flag.
		
		:type boolean: bool
		"""
		self._hidden = bool(boolean)
	
	# from ChartFile
	path = ChartCalc.path
	name = ChartCalc.name
	datetime = ChartCalc.datetime
	calendar = ChartCalc.calendar
	location = ChartCalc.location
	latitude = ChartCalc.latitude
	longitude = ChartCalc.longitude
	altitude = ChartCalc.altitude
	country = ChartCalc.country
	zoneinfo = ChartCalc.zoneinfo
	timezone = ChartCalc.timezone
	comment = ChartCalc.comment
	keywords = ChartCalc.keywords
	dst = ChartCalc.dst
	utcoffset = ChartCalc.utcoffset
	# from ChartDate
	julday = ChartCalc.julday
	local_datetime = ChartCalc.local_datetime
	utc_datetime = ChartCalc.utc_datetime
	local_mean_datetime = ChartCalc.local_mean_datetime
	sidtime = ChartCalc.sidtime
	local_sidtime = ChartCalc.local_sidtime
	# from ChartCalc
	filter = ChartCalc.filter
	ecl_nut = ChartCalc.ecl_nut
	planets = ChartCalc.planets
	houses = ChartCalc.houses
	aspects = ChartCalc.aspects
	midpoints = ChartCalc.midpoints
	midp_aspects = ChartCalc.midp_aspects
	# Additional properties
	hidden = property(_get_hidden, _set_hidden,
		doc='Chart hidden state flag.')
	
	def __init__(self, path=None, set_default=True, do_calc=True):
		ChartCalc.__init__(self, path, set_default, do_calc)
		self._hidden = False
	
	def hide(self):
		"""Set hidden flag to True."""
		self._hidden = True
	
	def show(self):
		"""Set hidden flag to False."""
		self._hidden = False
	
	def _all_draw_planets(self):
		"""Return a list of all points to draw (incl. midpoints).
		
		:rtype: PlanetDataList
		"""
		ret = PlanetDataList()
		ret.extend(self._planets)
		if self._filter._draw_midp:
			ret.extend(self._midp_aspects.get_midpoints())
		return ret
	
	def _all_draw_aspects(self):
		"""Return a list of all aspects to draw (incl. midpoints).
		
		:rtype: AspectDataList
		"""
		ret = AspectDataList()
		ret.extend(self._aspects)
		if self._filter._draw_midp:
			ret.extend(self._midp_aspects)
		return ret
	
	def __iter__(self):
		"""Iterate over chart properties.
		
		:rtype: generator
		"""
		return (x for x in (self._path, self._name, self._datetime,
			self._calendar, self._location, self._latitude, self._longitude,
			self._altitude, self._country, self._zoneinfo, self._timezone,
			self._comment, self._keywords, self._dst, self._utcoffset,
			self._julday, self._local_datetime, self._utc_datetime,
			self._local_mean_datetime, self._sidtime, self._local_sidtime,
			self._filter, self._ecl_nut, self._houses, self._planets,
			self._aspects, self._midpoints, self._midp_aspects, self._hidden))
	
	def __repr__(self):
		if self._path != None:
			return "Chart('''%s''')" % self._path
		else:
			return repr(tuple(repr(x) for x in self))





# End.
