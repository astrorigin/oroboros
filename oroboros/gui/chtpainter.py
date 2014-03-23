#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Chart painter object.

"""

import os.path
from math import sin, cos, radians

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import swisseph as swe

from oroboros.gui import chtflowers


__all__ = ['ChartPainter']


_baseDir = os.path.dirname(os.path.abspath(__file__))

_iconRect = QRect(0, 0, 300, 300) # original icons size 300x300 px

# in case using others than default glyphs
_zodiacDir = '.'
_cuspsDir = '.'
_planetsDir = '.'



def _getPointAt(ang, hyp, modx=0, mody=0):
	"""Get coordinates of a point.
	
	ang -> angle (0 is 3 o'clock, clockwise)
	hyp -> distance (hypothenuse)
	modx -> modification of point x leftwards
	mody -> modification of point y upwards
	
	"""
	x = (cos(radians(ang)) * hyp) - modx
	y = (sin(radians(ang)) * hyp) - mody
	return x, y


class ChartPainter(QPainter):
	"""Paint chart on device."""
	
	def __init__(self, device, chart):
		"""Paint on device.
		
		:type device: QPaintDevice
		:type chart: BiChart
		"""
		QPainter.__init__(self, device)
		self._chart = chart
		# set angle to vernal point
		self._vernalAng = swe.degnorm(chart[0]._houses[0]._longitude - 180)
		# set canvas
		self.setWindow(0, 0, 242, 242) # window is 240 x 240, +2 for antialias
		self.translate(121, 121) # set center at 0;0
		self.setRenderHints(QPainter.Antialiasing)
		# set colors
		if chart[0].filter._bg_color == 'black':
			self._bgColor = Qt.black
			self._drawColor = Qt.white
			self._lightColor = Qt.darkGray
			self._middleColor = Qt.gray
			self._darkColor = Qt.lightGray
		else: ## white
			self._bgColor = Qt.white
			self._drawColor = Qt.black
			self._lightColor = Qt.lightGray
			self._middleColor = Qt.gray
			self._darkColor = Qt.darkGray
		# fill background color
		self.fillRect(-121, -121, 242, 242, QBrush(self._bgColor))
		# set drawing color
		self.setPen(self._drawColor)
		# draw markers before circles to overwrite lighter pixels
		self.draw_zodiac()
		self.draw_cusps()
		self.draw_circles()
		self.draw_signs()
		self.draw_houses()
		# draw visible charts
		visible = [x for x in self._chart if not x._hidden]
		lenvisible = len(visible)
		if lenvisible == 0: ## all hidden
			return
		# draw aspects before planets to overwrite
		if lenvisible == 1:
			self.draw_aspects(visible[0]._all_draw_aspects(), lenvisible)
			self.draw_planets(0, lenvisible, visible[0]._all_draw_planets())
		else: ## interaspects
			self.draw_aspects(self._chart._all_draw_aspects(), lenvisible)
			if self._chart[0]._filter._draw_midp:
				self.draw_planets(0, lenvisible, self._chart._all_draw_planets(0))
			else:
				self.draw_planets(0, lenvisible, visible[0]._all_draw_planets())
			if self._chart[1]._filter._draw_midp:
				self.draw_planets(1, lenvisible, self._chart._all_draw_planets(1))
			else:
				self.draw_planets(1, lenvisible, visible[1]._all_draw_planets())
	
	def draw_circles(self):
		"""Draw all circles for zodiac, degree markers, houses."""
		self.drawArc(-120, -120, 240, 240, 0, 5760) # most outer circle
		self.drawArc(-100, -100, 200, 200, 0, 5760) # for zodiac
		self.drawArc(-93, -93, 186, 186, 0, 5760) # for degree markers
		self.drawArc(-80, -80, 160, 160, 0, 5760) # for houses markers
	
	def draw_zodiac(self):
		"""Draw zodiac limits and degrees markers."""
		self.save()
		zodiacline = (93, 0, 120, 0)
		degreeline = (93, 0, 100, 0)
		self.rotate(self._vernalAng)
		for i in range(360):
			if i % 30 == 0: # sign limit
				self.setPen(self._drawColor)
				self.drawLine(*zodiacline)
			elif i % 10 == 0: # decanate limit
				self.setPen(self._darkColor)
				self.drawLine(*degreeline)
			elif i % 5 == 0: # half-decanate limit
				self.setPen(self._middleColor)
				self.drawLine(*degreeline)
			else: # one degree
				self.setPen(self._lightColor)
				self.drawLine(*degreeline)
			self.rotate(1)
		self.restore()
	
	def draw_signs(self):
		"""Draw signs glyphs."""
		zodiacdir = os.path.join(_baseDir, 'icons', 'zodiac', _zodiacDir)
		ang = swe.degnorm(self._vernalAng - 15)
		for i in range(12):
			im = QImage(os.path.join(zodiacdir, 'sign_%.2d.png' % (i+1)))
			x, y = _getPointAt(ang, 111, 8, 8)
			target = QRect(x, y, 16, 16)
			self.drawImage(target, im, _iconRect)
			ang -= 30
	
	def draw_cusps(self):
		"""Draw houses cusps."""
		# get params, Gauquelin has 36 cusps
		mc = self._vernalAng - self._chart[0]._houses[9]._longitude
		if self._chart[0].filter._hsys != 'G':
			othercusps = (1, 2, 4, 5)
		else: # Gauquelin sectors
			othercusps = (1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17)
		# draw mc line
		w, x = _getPointAt(mc, 122)
		y, z = _getPointAt(mc + 180, 122)
		self.setPen(self._darkColor)
		self.drawLine(w, x, y, z)
		# draw other cusps
		pen1 = QPen(Qt.DotLine)
		pen1.setColor(self._lightColor)
		pen2 = QPen(self._middleColor)
		for i in othercusps:
			self.setPen(pen1)
			a = self._vernalAng - self._chart[0]._houses[i].longitude
			w, x = _getPointAt(a, 80.5)
			y, z = _getPointAt(a + 180, 80.5)
			self.drawLine(w, x, y, z)
			self.setPen(pen2)
			w1, x1 = _getPointAt(a, 93.5)
			y1, z1 = _getPointAt(a + 180, 93.5)
			self.drawLine(w, x, w1, x1)
			self.drawLine(y, z, y1, z1)
		# draw asc line finally to overwrite lighter pixels
		self.setPen(self._darkColor)
		self.drawLine(-121, 0, 121, 0)
		# reset pen
		self.setPen(self._drawColor)
	
	def draw_houses(self):
		"""Draw houses glyphs."""
		cuspsdir = os.path.join(_baseDir, 'icons', 'cusps', _cuspsDir)
		if self._chart[0].filter._hsys != 'G': ## traditional houses
			houses = self._chart[0]._houses[:12]
			for i in range(12):
				im = QImage(os.path.join(cuspsdir, 'cusp_%.2d.png' % (i+1)))
				diff = swe.difdeg2n(houses[i]._longitude,
					houses[i-11]._longitude) / 2.0
				a = self._vernalAng - (houses[i]._longitude - diff)
				x, y = _getPointAt(a, 87, 5, 5)
				target = QRect(x, y, 10, 10)
				self.drawImage(target, im, _iconRect)
		else: ## Gauquelin sectors
			houses = self._chart[0]._houses[:36]
			for i in range(36):
				im = QImage(os.path.join(cuspsdir, 'sector_%.2d.png' % (i+1)))
				diff = swe.difdeg2n(houses[i]._longitude,
					houses[i-35]._longitude) / 2.0
				a = self._vernalAng - (houses[i]._longitude - diff)
				x, y = _getPointAt(a, 87, 5, 5)
				target = QRect(x, y, 10, 10)
				self.drawImage(target, im, _iconRect)
	
	def draw_planets(self, num, lenvisible, plres):
		"""Draw planets glyphs."""
		if lenvisible == 2:
			if num == 1:
				w1, w2, w3, w4, gw = 50, 53, 68, 73, 16
				self.setPen(self._drawColor)
			elif num == 0:
				w1, w2, w3, w4, gw = 50, 53, 56, 61, 15
				self.setPen(self._lightColor)
		else:
			w1, w2, w3, w4, gw = 55, 58, 63, 70, 18
			self.setPen(self._drawColor)
		pldir = os.path.join(_baseDir, 'icons', 'planets', _planetsDir)
		plres.sort_by_ranking(reverse=True)
		# get arranged positions
		allpos = [x._longitude for x in plres]
		glyph = chtflowers.rearrange(allpos, 10)
		# draw midpoints
		for i, res in enumerate(plres):
			a = self._vernalAng - glyph[i]
			b = self._vernalAng - res._longitude
			# draw little marker
			if a == b:
				w, x = _getPointAt(b, w3)
				y, z = _getPointAt(b, w1)
				self.drawLine(w, x, y, z)
			else:
				w, x = _getPointAt(b, w2)
				y, z = _getPointAt(b, w1)
				self.drawLine(w, x, y, z)
				y, z = _getPointAt(a, w3)
				self.drawLine(w, x, y, z)
			# paste midp or planet glyph
			try: ## planet
				im = QImage(os.path.join(pldir, res._planet._glyph))
				x, y = _getPointAt(a, w4, gw/2.0, gw/2.0)
				target = QRect(x, y, gw, gw)
				self.drawImage(target, im, _iconRect)
			except: ## midp
				im1 = QImage(os.path.join(pldir, res._data1._planet._glyph))
				im2 = QImage(os.path.join(pldir, res._data2._planet._glyph))
				x, y = _getPointAt(a, w4+3, gw/3.2, gw/3.2)
				target = QRect(x, y, gw/1.6, gw/1.6)
				self.drawImage(target, im1, _iconRect)
				x, y = _getPointAt(a, w4-3, gw/3.2, gw/3.2)
				target = QRect(x, y, gw/1.6, gw/1.6)
				self.drawImage(target, im2, _iconRect)
		self.setPen(self._drawColor)
	
	def draw_aspects(self, aspectsres, numvisible):
		if numvisible == 1:
			width = 55
		else: ## 2
			width = 50
		for aspr in aspectsres.sort_by_ranking():
			a1 = self._vernalAng - aspr._data1._longitude
			a2 = self._vernalAng - aspr._data2._longitude
			w, x = _getPointAt(a1, width)
			y, z = _getPointAt(a2, width)
			pen = QPen(QColor(*tuple(aspr._aspect._color)))
			# dash line according to factor
			if aspr._factor > 0.1:
				if aspr._factor <= 0.2:
					pen.setDashPattern([8, 2])
				elif aspr._factor <= 0.3:
					pen.setDashPattern([6, 2])
				elif aspr._factor <= 0.4:
					pen.setDashPattern([5, 2])
				elif aspr._factor <= 0.5:
					pen.setDashPattern([4, 2])
				elif aspr._factor <= 0.6:
					pen.setDashPattern([3, 3])
				elif aspr._factor <= 0.7:
					pen.setDashPattern([2, 4])
				elif aspr._factor <= 0.8:
					pen.setDashPattern([1, 5])
				elif aspr._factor <= 0.9:
					pen.setDashPattern([1, 6])
				elif aspr._factor <= 1:
					pen.setDashPattern([1, 7])
			self.setPen(pen)
			self.drawLine(w, x, y, z)
		self.setPen(self._drawColor)




# End.
