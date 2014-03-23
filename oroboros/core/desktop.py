#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Desktop manager.

"""

from oroboros.core.bicharts import BiChart


__all__ = ['charts']


class OpenedCharts(list):
	"""Opened charts object."""
	
	def append(self, cht):
		if not isinstance(cht, BiChart):
			cht = BiChart(cht)
		list.append(self, cht)
	
	def insert(self, idx, cht):
		if not isinstance(cht, BiChart):
			cht = BiChart(cht)
		list.insert(self, idx, cht)
	
	def __setitem__(self, item):
		if not isinstance(item, BiChart):
			item = BiChart(item)
		list.__setitem__(self, item)


#: Opened charts singleton
charts = OpenedCharts()



# End.
