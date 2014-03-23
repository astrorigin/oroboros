#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Charts with two subcharts.

"""

from decimal import Decimal

import swisseph as swe

from oroboros.core.charts import Chart
from oroboros.core.planets import all_planets
from oroboros.core.aspects import all_aspects
from oroboros.core.results import PlanetDataList
from oroboros.core.aspectsresults import AspectDataList, MidPointAspectDataList, InterMidPointAspectDataList


__all__ = ['BiChart']


class BiChart(list):
	"""Chart object with comparisons functions for two subcharts."""
	
	__slots__ = ('_interaspects', '_intermidp1', '_intermidp2',
		'_intermidpoints', '_switched')
	
	def _get_interaspects(self):
		"""Get inter-aspects.
		
		:rtype: AspectDataList
		"""
		if self._interaspects == None:
			self._calc_interaspects()
		return self._interaspects
	
	def _get_intermidp1(self):
		"""Get aspects between chart 1 midpoints and chart 2 planets.
		
		:rtype: MidPointAspectDataList
		"""
		if self._intermidp1 == None:
			self._calc_intermidp(0)
		return self._intermidp1
	
	def _get_intermidp2(self):
		"""Get aspects between chart 2 midpoints and chart 1 planets.
		
		:rtype: MidPointAspectDataList
		"""
		if self._intermidp2 == None:
			self._calc_intermidp(1)
		return self._intermidp2
	
	def _get_intermidpoints(self):
		"""Get aspects between midpoints.
		
		:rtype: InterMidPointAspectDataList
		"""
		if self._intermidpoints == None:
			self._calc_intermidpoints()
		return self._intermidpoints
	
	def _get_switched(self):
		"""Get switch state flag.
		
		:rtype: bool
		"""
		return self._switched
	
	def _set_switched(self, boolean):
		"""Set switched state flag.
		
		:type boolean: bool
		"""
		self._switched = bool(boolean)
	
	interaspects = property(_get_interaspects,
		doc='Inter-aspects.')
	intermidp1 = property(_get_intermidp1,
		doc='Aspects to chart 1 midpoints.')
	intermidp2 = property(_get_intermidp2,
		doc='Aspects to chart 2 midpoints.')
	intermidpoints = property(_get_intermidpoints,
		doc='Aspects between midpoints.')
	switched = property(_get_switched, _set_switched,
		doc='Bichart switched state (bool).')
	
	def __init__(self, cht1=None, cht2=None):
		"""Init bi-chart.
		
		:type cht1: Chart, str, int or None
		:type cht2: Chart, str, int or None
		"""
		self._switched = False
		if cht1 != None:
			self.append(cht1)
		if cht2 != None:
			self.append(cht2)
		self.calc()
	
	def append(self, cht):
		"""Append a chart.
		
		:type cht: Chart, str or int
		:raise TypeError: invalid chart
		"""
		if not isinstance(cht, Chart):
			try:
				cht = Chart(cht)
			except:
				raise
				raise TypeError('Invalic chart %s.' % cht)
		list.append(self, cht)
		self.calc()
	
	def insert(self, idx, cht):
		"""Insert a chart.
		
		:type idx: int
		:type cht: Chart, str or int
		:raise IndexError: invalid index
		:raise TypeError: invalid chart
		"""
		if idx > 1 or idx < -2:
			raise IndexError('Invalid index %s.' % idx)
		if not isinstance(cht, Chart):
			try:
				cht = Chart(cht)
			except:
				raise TypeError('Invalic chart %s.' % cht)
		list.insert(self, idx, cht)
		self.calc()
	
	def __setitem__(self, idx, cht):
		if idx > 1 or idx < -2:
			raise IndexError('Invalid index %s.' % idx)
		if not isinstance(cht, Chart):
			try:
				cht = Chart(cht)
			except:
				raise TypeError('Invalic chart %s.' % cht)
		list.__setitem__(self, idx, cht)
		self.calc()
	
	def __delitem__(self, idx):
		self._switched = False
		list.__delitem__(self, idx)
	
	def set(self, idx, **kwargs):
		"""Set charts properties."""
		self[idx].set(**kwargs)
		if any((x for x in kwargs if x in ('datetime', 'calendar', 'location',
			'latitude', 'longitude', 'altitude', 'zoneinfo', 'timezone', 'dst',
			'utcoffset', 'filter'))):
			self.reset_calc()
	
	def reset_calc(self):
		"""Trigger recalculation of aspects."""
		self._interaspects = None
		self._intermidp1 = None
		self._intermidp2 = None
		self._intermidpoints = None
	
	# calculations
	
	def _calc_interaspects(self):
		"""Calculate inter-aspects of planets between charts 1 and 2."""
		res = AspectDataList()
		if len(self) != 2:
			self._interaspects = res
			return
		f1 = self[0]._filter
		f2 = self[1]._filter
		all_asp = all_aspects()
		for pos1 in self[0]._planets:
			p1, lon1, lonsp1 = pos1._planet, pos1._longitude, pos1._lonspeed
			for pos2 in self[1]._planets:
				p2, lon2, lonsp2 = pos2._planet, pos2._longitude, pos2._lonspeed
				for asp, doasp in f1._aspects.items():
					if not doasp:
						continue
					if not f2._aspects[asp]:
						continue
					if not f1._asprestr[p1._name] or not f2._asprestr[p1._name]:
						continue
					if not f2._asprestr[p2._name] or not f2._asprestr[p2._name]:
						continue
					asp = all_asp[asp]
					orb = (f1._orbs[asp._name]+f2._orbs[asp._name])/Decimal('2')
					orbmod1 = f1.orbrestr[p1._name].get_absolute(orb)
					orbmod2 = f2.orbrestr[p2._name].get_absolute(orb)
					orb += (orbmod1 + orbmod2) / Decimal('2')
					if orb < 0:
						continue
					diff, apply, factor = swe._match_aspect2(
						lon1, lonsp1, lon2, lonsp2,
						float(asp._angle), float(orb))
					if diff != None:
						res.feed(pos1, pos2, asp, diff, apply, factor)
		self._interaspects = res
	
	def _calc_intermidp(self, idx):
		"""Calculate aspects between one midpoints and other planets."""
		res = MidPointAspectDataList()
		try:
			if len(self) != 2 or not self[idx]._filter._calc_midp:
				if idx == 0:
					self._intermidp1 = res
				else:
					self._intermidp2 = res
				return
		except IndexError:
			if idx == 0:
				self._intermidp1 = res
			else:
				self._intermidp2 = res
			return
		# ok do calc
		oth = 1 if idx in (0, -2) else 0 # other's idx
		midpres = self[idx]._midpoints
		jd = self[oth].julday
		flag = self[oth]._filter.get_calcflag()
		self[oth]._setup_swisseph()
		f = self[idx]._filter._midpoints
		all_pl = all_planets()
		all_asp = all_aspects()
		# get all concerned planets, if not already calculated
		plres = PlanetDataList()
		for pl in [x for x in f._planets if f._planets[x] and f._asprestr[x]]:
			try:
				plres.append(self[oth]._planets.get_data(pl))
			except KeyError:
				p = all_pl[pl]
				plres.feed(p, p.calc_ut(jd, flag, self[oth]))
		# get midp aspects
		plres.sort_by_ranking()
		for i, midp in enumerate(midpres):
			##p1, p2 = midp._planet, midp._planet2
			lon1, lonsp1 = midp._longitude, midp._lonspeed
			for pos in plres:
				pl, lon2, lonsp2 = pos._planet, pos._longitude, pos._lonspeed
				for asp, doasp in f._aspects.items():
					if not doasp: # dont use this aspect
						continue
					asp = all_asp[asp]
					# modify orb
					orb = f._orbs[asp._name]
					#orbmod1 = plorbfilt[p1._name].get_absolute(orb)
					orbmod1 = 0 # todo?: midp obrestr
					orbmod2 = f._orbrestr[pl._name].get_absolute(orb)
					orb += (orbmod1 + orbmod2) / Decimal('2')
					if orb < 0: # we'll never get such a precision
						continue
					# check aspect match
					diff, apply, factor = swe._match_aspect2(
						lon1, lonsp1, lon2, lonsp2,
						float(asp._angle), float(orb))
					if diff != None:
						res.feed(midp, pos, asp, diff, apply, factor)
		if idx == 0:
			self._intermidp1 = res
		else:
			self._intermidp2 = res
	
	def _calc_intermidpoints(self):
		"""Calculate aspects between midpoints."""
		res = InterMidPointAspectDataList()
		if len(self) != 2:
			self._intermidpoints = res
			return
		elif not self[0]._filter._calc_midp or not self[1]._filter._calc_midp:
			self._intermidpoints = res
			return
		f1 = self[0]._filter._midpoints
		f2 = self[1]._filter._midpoints
		all_asp = all_aspects()
		# begin calc
		for i, pos1 in enumerate(self[0]._midpoints):
			p1, lon1, lonsp1 = pos1._data2, pos1._longitude, pos1._lonspeed
			for pos2 in self[1]._midpoints:
				p2, lon2, lonsp2 = pos2._data2, pos2._longitude, pos2._lonspeed
				for asp, doasp in f1._aspects.items():
					if not doasp: # dont use this aspect
						continue
					if not f2._aspects[asp]:
						continue
					# no asp restr
					asp = all_asp[asp]
					# modify orb
					orb1 = f1._orbs[asp._name]
					orb2 = f2._orbs[asp._name]
					orb = orb1 + orb2 / Decimal('2')
					# nor orb restr
					# check aspect match
					diff, apply, factor = swe._match_aspect2(
						lon1, lonsp1, lon2, lonsp2,
						float(asp._angle), float(orb))
					if diff != None:
						res.feed(pos1, pos2, asp, diff, apply, factor)
		self._intermidpoints = res
	
	def calc(self):
		"""Do all calculations."""
		self._calc_interaspects()
		self._calc_intermidp(0)
		self._calc_intermidp(1)
		self._calc_intermidpoints()
	
	def _all_draw_aspects(self):
		"""Return a list of all drawable aspects (incl. activated midpoints).
		
		:rtype: AspectDataList
		"""
		ret = AspectDataList()
		ret.extend(self._interaspects)
		try:
			if self[0]._filter._draw_midp:
				ret.extend(self._intermidp1)
		except IndexError: # none chart
			pass
		try:
			if self[1]._filter._draw_midp:
				ret.extend(self._intermidp2)
		except IndexError: # none chart
			pass
#		try:
#			if self[0]._filter._draw_midp and self[1]._filter._draw_midp:
#				ret.extend(self._intermidpoints)
#		except IndexError: # none chart
#			pass
		return ret
	
	def _all_draw_planets(self, idx=0):
		"""Get all planets and midpoints to draw when comparing charts.
		
		:type idx: int
		:rtype: PlanetDataList
		"""
		ret = PlanetDataList()
		if idx == 0:
			ret.extend(self[0]._planets)
			ret.extend(self._intermidp1.get_midpoints())
		else:
			ret.extend(self[1]._planets)
			ret.extend(self._intermidp2.get_midpoints())
		return ret
	
	def switch(self):
		"""Switch chart 1 and 2."""
		self.reverse()
		self._switched = not self._switched
		self.calc()
	
	def synastry_mode(self):
		"""Set comparison mode transit/synastry."""
		for i, cht in enumerate(self):
			self[i].calc()
		self.calc()
	
	def progression_of(self, idx=0):
		"""Set comparison mode progression.
		
		:type idx: int
		:raise IndexError: missing chart
		"""
		if len(self) != 2:
			raise IndexError('Missing chart(s).')
		if idx == 0:
			cht1 = 0
			cht2 = 1
		elif idx == 1:
			cht1 = 1
			cht2 = 0
		self[cht2].progression_of(self[cht1].julday)
		self.calc()
	
	def direction_of(self, idx=0):
		"""Set comparison mode direction.
		
		:type idx: int
		:raise IndexError: missing chart
		"""
		if len(self) != 2:
			raise IndexError('Missing chart(s)')
		if idx == 0:
			cht1 = 0
			cht2 = 1
		elif idx == 1:
			cht1 = 1
			cht2 = 0
		self[cht2].direction_of(self[cht1].julday)
		self.calc()
	
	def multiply_pos(self, value, idx):
		"""Multiply positions by value.
		
		:type value: numeric
		:type idx: int
		"""
		self[idx].multiply_pos(value)
		self.calc()
	
	def add_pos(self, value, idx):
		"""Add value to positions.
		
		:type value: numeric
		:type idx: int
		"""
		self[idx].add_pos(value)
		self.calc()
	
	def profection_of(self, op, value, unit, idx=0):
		"""Profection.
		
		:type op: str
		:type value: numeric
		:type unit: str
		:type idx: int
		:raise IndexError: missing chart
		"""
		if len(self) != 2:
			raise IndexError('Missing chart(s)')
		if idx == 0:
			cht1 = 0
			cht2 = 1
		elif idx == 1:
			cht1 = 1
			cht2 = 0
		self[cht2].profection_of(op, value, unit, self[cht1].julday)
		self.calc()
	
	def __repr__(self):
		return "BiChart(%s)" % ', '.join([repr(x) for x in self])





# End.
