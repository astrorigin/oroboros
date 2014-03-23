#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Object holding aspects calculations results.

Provides functions for searching, retrieving, sorting results.

"""

from oroboros.core.aspects import Aspect
from oroboros.core.results import PlanetData, MidPointData


__all__ = ['AspectData', 'AspectDataList', 'MidPointAspectData',
	'MidPointAspectDataList', 'InterMidPointAspectData',
	'InterMidPointAspectDataList']



class AspectData(object):
	"""Aspect data element."""
	
	__slots__ = ('_data1', '_data2', '_aspect', '_diff', '_apply', '_factor')
	
	def _get_data1(self):
		"""Get planet 1 data.
		
		:rtype: PlanetData
		"""
		return self._data1
	
	def _set_data1(self, data):
		"""Set planet 1 data.
		
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
		"""Set planet 2 data.
		
		:type data: PlanetData
		:raise TypeError: invalid data
		"""
		if not isinstance(data, PlanetData):
			raise TypeError('Invalid planet data %s.' % data)
		self._data2 = data
	
	def _get_aspect(self):
		"""Get aspect object.
		
		:rtype: Aspect
		"""
		return self._aspect
	
	def _set_aspect(self, asp):
		"""Set aspect object.
		
		Accepts aspect object or aspect name or index.
		
		:type asp: Aspect or str or int
		:raise TypeError: invalid aspect
		"""
		if not isinstance(asp, Aspect):
			try:
				asp = Aspect(asp)
			except:
				raise TypeError('Invalid aspect object %s.' % asp)
		self._aspect = asp
	
	def _get_diff(self):
		"""Get difference with exact (no orb) aspect.
		
		:rtype: float
		"""
		return self._diff
	
	def _set_diff(self, diff):
		"""Set difference.
		
		:type diff: float
		"""
		self._diff = diff
	
	def _get_apply(self):
		"""Get applying flag.
		
			- True -> applying
			- False -> separating
			- None -> stable
		
		:rtype: bool or None
		"""
		return self._apply
	
	def _set_apply(self, apply):
		"""Set applying flag.
		
		:type apply: bool or None
		:raise TypeError: invalid flag
		"""
		if apply not in (True, False, None):
			raise TypeError('Invalid apply flag %s.' % apply)
		self._apply = apply
	
	def _get_factor(self):
		"""Get factor (percentage of orb used).
		
		:rtype: float
		"""
		return self._factor
	
	def _set_factor(self, factor):
		"""Set factor.
		
		:type factor: float
		"""
		self._factor = factor
	
	data1 = property(_get_data1, _set_data1, doc='First planet data.')
	data2 = property(_get_data2, _set_data2, doc='Second planet data')
	aspect = property(_get_aspect, _set_aspect, doc='Aspect object.')
	diff = property(_get_diff, _set_diff, doc='Difference (numeric).')
	apply = property(_get_apply, _set_apply, doc='Apply flag.')
	factor = property(_get_factor, _set_factor, doc='Strength factor.')
	
	def __init__(self, data1, data2, asp, diff, apply, factor):
		self.data1 = data1
		self.data2 = data2
		self.aspect = asp
		self.diff = diff
		self.apply = apply
		self.factor = factor
	
	def __str__(self):
		return str([self._data1, self._data2, self._aspect, self._diff,
			self._apply, self._factor])
	
	def __repr__(self):
		return 'AspectData(%s, %s, %s, %s, %s, %s)' % (
			repr(x) for x in (
			self._data1, self._data2, self._aspect, self._diff, self._apply,
			self._factor))


class AspectDataList(list):
	"""Aspects data list."""
	
	def feed(self, data1, data2, asp, diff, apply, factor):
		"""Append calculation results.
		
			- data* -> PlanetData
			- asp -> Aspect
			- diff, apply, factor -> swisseph.match_aspect results
		
		"""
		self.append(AspectData(data1, data2, asp, diff, apply, factor))
	
	def sort_by_precision(self, reverse=False):
		"""Sort results by precision.
		
		:rtype: self
		"""
		self.sort(self._sort_by_precision, reverse=reverse)
		return self
	
	@staticmethod
	def _sort_by_precision(x, y):
		"""Function to sort aspects list by aspect precision."""
		if x._diff > y._diff:
			return 1
		elif x._diff < y._diff:
			return -1
		return 0
	
	def sort_by_ranking(self, reverse=False):
		"""Sort results by aspect ranking.
		
		:rtype: self
		"""
		self.sort(self._sort_by_ranking, reverse=reverse)
		return self
	
	@staticmethod
	def _sort_by_ranking(x, y):
		"""Function to sort results list by aspect ranking."""
		if x._aspect._ranking > y._aspect._ranking:
			return 1
		elif x._aspect._ranking < y._aspect._ranking:
			return -1
		return 0
	
	def sort_by_factor(self, reverse=False):
		"""Sort aspects list by aspect strength factor.
		
		:rtype: self
		"""
		self.sort(self._sort_by_factor, reverse=reverse)
		return self
	
	@staticmethod
	def _sort_by_factor(x, y):
		"""Function to sort results by strength factor."""
		if x._factor > y._factor:
			return 1
		elif x._factor < y._factor:
			return -1
		return 0
	
	def __getitem__(self, aspname):
		"""Get all results for an aspect.
		
		:type aspname: str
		:rtype: AspectDataList
		"""
		ret = AspectDataList()
		for e in self:
			if e._aspect._name == aspname:
				ret.append(e)
		return ret


class MidPointAspectData(AspectData):
	"""Aspect data for midpoints/planets."""
	
	__slots__ = ('_data1', '_data2', '_aspect', '_diff',
		'_apply', '_factor')
	
	def _get_data1(self):
		"""Get midpoint data.
		
		:rtype: MidPointData
		"""
		return self._data1
	
	def _set_data1(self, mpdata):
		"""Set midpoint data.
		
		:type mpdata: MidPointData
		:raise TypeError: invalid data
		"""
		if not isinstance(mpdata, MidPointData):
				raise TypeError('Invalid midpoint data %s.' % mpdata)
		self._data1 = mpdata
	
	data1 = property(_get_data1, _set_data1,
		doc='Midpoint data.')
	data2 = property(AspectData._get_data2, AspectData._set_data2,
		doc='Planet data.')
	aspect = property(AspectData._get_aspect, AspectData._set_aspect,
		doc='Aspect object.')
	diff = property(AspectData._get_diff, AspectData._set_diff,
		doc='Difference.')
	apply = property(AspectData._get_apply, AspectData._set_apply,
		doc='Apply flag.')
	factor = property(AspectData._get_factor, AspectData._set_factor,
		doc='Strength factor.')
	
	def __repr__(self):
		return 'MidPointAspectData(%s, %s, %s, %s, %s, %s)' % (
			repr(x) for x in (
			self._data1, self._data2, self._aspect,
			self._diff, self._apply, self._factor))


class MidPointAspectDataList(AspectDataList):
	"""Aspects data list for midpoints/planets."""
	
	def feed(self, data1, data2, asp, diff, apply, factor):
		"""Append an aspect result.
		
		:type data1: MidPointData
		:type data2: PlanetData
		:type asp: Aspect
		:type diff: numeric
		:type apply: bool or None
		:type factor: numeric
		"""
		self.append(MidPointAspectData(data1, data2, asp, diff, apply, factor))
	
	def __getitem__(self, aspname):
		"""Get all results for an aspect.
		
		:type aspname: str
		:rtype: MidPointAspectDataList
		"""
		ret = MidPointAspectDataList()
		for e in self:
			if e._aspect._name == aspname:
				ret.append(e)
		return ret
	
	def get_midpoints(self):
		"""Get a set of midpoints data.
		
		:rtype: list
		"""
		ret = list()
		for res in self:
			if res._data1 not in ret:
				ret.append(res._data1)
		return ret


class InterMidPointAspectData(MidPointAspectData):
	"""Aspect data list for midpoints/midpoints."""
	
	__slots__ = MidPointAspectData.__slots__
	
	def _get_data2(self):
		"""Get midpoint data.
		
		:rtype: MidPointData
		"""
		return self._data2
	
	def _set_data2(self, mpdata):
		"""Set midpoint data.
		
		:type mpdata: MidPointData
		:raise TypeError: invalid data
		"""
		if not isinstance(mpdata, MidPointData):
				raise TypeError('Invalid midpoint data %s.' % mpdata)
		self._data2 = mpdata
	
	data1 = property(MidPointAspectData._get_data1, MidPointAspectData._set_data1,
		doc='Midpoint data.')
	data2 = property(_get_data2, _set_data2,
		doc='Planet data.')
	aspect = property(MidPointAspectData._get_aspect, MidPointAspectData._set_aspect,
		doc='Aspect object.')
	diff = property(MidPointAspectData._get_diff, MidPointAspectData._set_diff,
		doc='Difference.')
	apply = property(MidPointAspectData._get_apply, MidPointAspectData._set_apply,
		doc='Apply flag.')
	factor = property(MidPointAspectData._get_factor, MidPointAspectData._set_factor,
		doc='Strength factor.')
	
	def __repr__(self):
		return 'InterMidPointAspectData(%s, %s, %s, %s, %s, %s)' % (
			repr(x) for x in (
			self._data1, self._data2, self._aspect,
			self._diff, self._apply, self._factor))


class InterMidPointAspectDataList(MidPointAspectDataList):
	"""List of midpoints/midpoints aspects."""
	
	def feed(self, data1, data2, asp, diff, apply, factor):
		"""Append an aspect result.
		
		:type data1: MidPointData
		:type data2: MidPointData
		:type asp: Aspect
		:type diff: numeric
		:type apply: bool or None
		:type factor: numeric
		"""
		self.append(InterMidPointAspectData(data1, data2, asp, diff, apply, factor))
	
	def __getitem__(self, aspname):
		"""Get all results for an aspect.
		
		:type aspname: str
		:rtype: InterMidPointAspectDataList
		"""
		ret = InterMidPointAspectDataList()
		for e in self:
			if e._aspect._name == aspname:
				ret.append(e)
		return ret
	
	def get_midpoints2(self):
		"""Get a set of midpoints data.
		
		:rtype: list
		"""
		ret = list()
		for res in self:
			if res._data2 not in ret:
				ret.append(res._data2)
		return ret




def _test():
	import doctest
	doctest.testmod()

if __name__ == '__main__':
	_test()

# End.
