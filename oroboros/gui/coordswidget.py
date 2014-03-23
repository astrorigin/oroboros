#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Editable boxes for geocoords.

"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from oroboros.core.geocoords import Latitude, Longitude


__all__ = ['LatitudeEdit', 'LongitudeEdit']


class _CoordsWidget(QHBoxLayout):
	"""Base class.
	
	coords -> Latitude or Longitude object
	
	"""
	
	def __init__(self, coords, parent):
		QHBoxLayout.__init__(self)
		if isinstance(coords, Latitude):
			self._typ = 'lat'
		elif isinstance(coords, Longitude):
			self._typ = 'lon'
		else:
			raise TypeError('Invalid coords %s.' % coords)
		self._coords = coords
		tr = self.tr
		# set params
		if self._typ == 'lat':
			maxdg = 90
			self.drlist = ['N', 'S']
			strlst = [tr('N', 'North'), tr('S', 'South')]
		elif self._typ == 'lon':
			maxdg = 180
			self.drlist = ['E', 'W']
			strlst = [tr('E', 'East'), tr('W', 'West')]
		# degrees
		self.dgspin = QSpinBox(parent)
		self.dgspin.setMaximum(maxdg)
		self.dgspin.setMinimum(0)
		self.dgspin.setSuffix(tr('\xb0', 'Degrees'))
		self.dgspin.setAccelerated(True)
		self.dgspin.setButtonSymbols(QAbstractSpinBox.PlusMinus)
		self.addWidget(self.dgspin)
		# direction
		self.drbox = QComboBox(parent)
		self.drbox.addItems(strlst)
		self.drbox.setEditable(False)
		self.addWidget(self.drbox)
		# minutes
		self.mnspin = QSpinBox(parent)
		self.mnspin.setMaximum(59)
		self.mnspin.setMinimum(0)
		self.mnspin.setSuffix(tr("'", 'Minutes'))
		self.mnspin.setAccelerated(True)
		self.mnspin.setButtonSymbols(QAbstractSpinBox.PlusMinus)
		self.addWidget(self.mnspin)
		# seconds
		self.scspin = QSpinBox(parent)
		self.scspin.setMaximum(59)
		self.scspin.setMinimum(0)
		self.scspin.setSuffix(tr('"', 'Seconds'))
		self.scspin.setAccelerated(True)
		self.scspin.setButtonSymbols(QAbstractSpinBox.PlusMinus)
		self.addWidget(self.scspin)
		# set values
		self.reset()
	
	def reset(self):
		self.dgspin.setValue(self._coords._degrees)
		if self._coords._direction == self.drlist[0]:
			self.drbox.setCurrentIndex(0)
		else:
			self.drbox.setCurrentIndex(1)
		self.mnspin.setValue(self._coords._minutes)
		self.scspin.setValue(self._coords._seconds)
	
	def value(self):
		dg = self.dgspin.value()
		mn = self.mnspin.value()
		sc = self.scspin.value()
		if self.drbox.currentIndex() == 0:
			if self._typ == 'lat':
				dr = 'N'
			else:
				dr = 'E'
		else:
			if self._typ == 'lat':
				dr = 'S'
			else:
				dr = 'W'
		if self._typ == 'lat':
			return Latitude(dg, dr, mn, sc)
		else:
			return Longitude(dg, dr, mn, sc)
	



class LatitudeEdit(_CoordsWidget):
	
	def latitude(self):
		return _CoordsWidget.value(self)
	
	def setLatitude(self, lat):
		self._coords = lat
		self.reset()


class LongitudeEdit(_CoordsWidget):
	
	def longitude(self):
		return _CoordsWidget.value(self)
	
	def setLongitude(self, lon):
		self._coords = lon
		self.reset()


class AltitudeEdit(QSpinBox):
	
	def __init__(self, alt, parent):
		QSpinBox.__init__(self, parent)
		self._alt = alt
		self.setMaximum(10000)
		self.setMinimum(0)
		self.setSuffix(self.tr(' m.', 'meters'))
		self.setAccelerated(True)
		self.setButtonSymbols(QAbstractSpinBox.PlusMinus)
		self.reset()
	
	def reset(self):
		self.setValue(int(self._alt))
	
	def altitude(self):
		return QSpinBox.value(self)
	
	def setAltitude(self, alt):
		self._alt = alt
		self.reset()


# End.
