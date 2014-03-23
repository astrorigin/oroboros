#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Arrangement of up to 4 calculated charts.

"""



__all__ = ['MultiChart']



class MultiChart(list):
	"""Multiple charts."""
	
	__slots__ = (
		## display
		'_switched')
	
	def _get_switched(self):
		return self._switched
	
	def _set_switched(self, boolean):
		self._switched = boolean
	
	switched = property(_get_switched, _set_switched,
		doc='Switched charts status.')
	
	def __init__(self, cht1=None, cht2=None):
		list.__init__(self)
		if cht1 != None:
			self.insert(0, cht1)
		if cht2 != None:
			self.insert(1, cht2)
		self._switched = False
		self.calc()
	
	def append(self, cht):
		if not isinstance(cht, Chart):
			cht = Chart(cht)
		list.append(self, cht)
		self.calc()
	
	def insert(self, idx, cht):
		if not isinstance(cht, Chart):
			cht = Chart(cht)
		list.insert(self, idx, cht)
		self.calc()
	
	def pop(self, idx):
		list.pop(self, idx)
		if len(self) != 2:
			self._switched = False
	
	def __setitem__(self, idx, cht):
		if not isinstance(cht, Chart):
			cht = Chart(cht)
		list.__setitem__(self, idx, cht)
		self.calc()
	
	def __delitem__(self, item):
		list.__delitem__(self, item)
		if len(self) != 2:
			self._switched = False
	
	




# End.
