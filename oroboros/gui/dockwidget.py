#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Dock widget area.

"""

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from oroboros.gui import app
from oroboros.gui import chthtml


__all__ = ['DockWidget']


class DockWidget(QDockWidget):
	"""Charts information area."""
	
	def __init__(self, parent):
		QDockWidget.__init__(self, parent.tr('Charts Information'), parent)
		self._parent = parent
		self.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
		self.setMinimumWidth(300)
		# tabs widget
		self.tabs = MultiChartTabWidget(self)
		self.connect(self.tabs, SIGNAL('currentChanged(int)'),
			parent.dockTabChangedEvent)
		self.setWidget(self.tabs)
	
	def addTab(self, idx):
		"""Create tab for a multichart."""
		self.tabs.addTab(idx)
	
	def removeTab(self, idx):
		"""Destroy multichart."""
		self.tabs.removeTab(idx)
	
	def resetTab(self, idx):
		"""Reload multichart."""
		self.tabs.setTabText(idx, app.desktop.charts[idx][0]._name)
		self.tabs.widget(idx).reset()



class MultiChartTabWidget(QTabWidget):
	"""Multi-charts container."""
	
	def addTab(self, idx):
		tab = ChartTabWidget(idx, self)
		QTabWidget.addTab(self, tab, app.desktop.charts[idx][0]._name)
	
	def tabRemoved(self, idx):
		"""Reset idx."""
		for i in range(len(app.desktop.charts)):
			self.widget(i).resetIdx(i)



class ChartTabWidget(QTabWidget):
	"""Charts container."""
	
	def __init__(self, idx, parent):
		QTabWidget.__init__(self, parent)
		self._idx = idx
		self.reset()
	
	def tabRemoved(self, idx):
		"""Reset charts nums."""
		for i in range(len(app.desktop.charts[self._idx])):
			self.widget(i).resetNum(i)
	
	def resetIdx(self, idx):
		self._idx = idx
		for i in range(len(app.desktop.charts[self._idx])):
			self.widget(i).resetIdx(idx)
	
	def reset(self):
		num = len(app.desktop.charts[self._idx])
		for i in range(num):
			try:
				self.widget(i).reset()
			except:
				tab = ChartInfoToolBox(self._idx, i)
				self.addTab(tab,
					unicode(self.tr('Chart %(num)s')) % {'num': i+1})
		# remove tabs or add/reset comparison info
		if num == 2:
			try: # update or create comparison tab
				self.widget(2).reset()
			except:
				self.addTab(CompareInfoToolBox(self._idx), self.tr('1 / 2'))
		else: # remove tabs
			for i in range(self.count() - num):
				self.removeTab(self.count() - 1)



class ChartInfoToolBox(QToolBox):
	"""Display chart data."""
	
	def __init__(self, idx, num):
		QToolBox.__init__(self)
		self._idx = idx
		self._num = num
		tr = self.tr
		# chart data
		scroll1 = QScrollArea(self)
		scroll1.setWidgetResizable(True)
		self.addItem(scroll1, tr('Data'))
		self.textEdit1 = QTextEdit(self)
		self.textEdit1.setReadOnly(True)
		scroll1.setWidget(self.textEdit1)
		# chart planets
		scroll2 = QScrollArea(self)
		scroll2.setWidgetResizable(True)
		self.addItem(scroll2, tr('Planets'))
		self.textEdit2 = QTextEdit(self)
		self.textEdit2.setReadOnly(True)
		scroll2.setWidget(self.textEdit2)
		# chart houses
		scroll3 = QScrollArea(self)
		scroll3.setWidgetResizable(True)
		self.addItem(scroll3, tr('Cusps'))
		self.textEdit3 = QTextEdit(self)
		self.textEdit3.setReadOnly(True)
		scroll3.setWidget(self.textEdit3)
		# chart aspects
		scroll4 = QScrollArea(self)
		scroll4.setWidgetResizable(True)
		self.addItem(scroll4, tr('Aspects'))
		self.textEdit4 = QTextEdit(self)
		self.textEdit4.setReadOnly(True)
		scroll4.setWidget(self.textEdit4)
		# chart midpoints
		if app.desktop.charts[self._idx][num]._filter._calc_midp:
			self.createMidPointsTab()
			self.has_midpoints = True
		else:
			self.has_midpoints = False
		# load data
		self.reset()
	
	def createMidPointsTab(self):
		scroll = QScrollArea(self)
		scroll.setWidgetResizable(True)
		self.insertItem(4, scroll, self.tr('MidPoints'))
		self.textEdit5 = QTextEdit(self)
		self.textEdit5.setReadOnly(True)
		scroll.setWidget(self.textEdit5)
		self.has_midpoints = True
	
	def removeMidPointsTab(self):
		self.removeItem(4)
		self.has_midpoints = False
	
	def reset(self):
		self.createData()
		self.createPlanets()
		self.createHouses()
		self.createAspects()
		if app.desktop.charts[self._idx][self._num]._filter._calc_midp:
			if not self.has_midpoints:
				self.createMidPointsTab()
			self.createMidPoints()
		else:
			if self.has_midpoints:
				self.removeMidPointsTab()
	
	def createData(self):
		txt = chthtml.html_data(
			app.desktop.charts[self._idx][self._num])
		self.textEdit1.setHtml(txt)
	
	def createPlanets(self):
		txt = chthtml.html_planets(
			app.desktop.charts[self._idx][self._num].planets)
		self.textEdit2.setHtml(txt)
	
	def createHouses(self):
		txt = chthtml.html_cusps(
			app.desktop.charts[self._idx][self._num].houses)
		self.textEdit3.setHtml(txt)
	
	def createAspects(self):
		txt = chthtml.html_aspects(
			app.desktop.charts[self._idx][self._num].aspects.sort_by_precision())
		self.textEdit4.setHtml(txt)
	
	def createMidPoints(self):
		txt = chthtml.html_midpoints(
			app.desktop.charts[self._idx][self._num].midpoints,
			app.desktop.charts[self._idx][self._num].midp_aspects.sort_by_precision())
		self.textEdit5.setHtml(txt)
	
	def resetIdx(self, idx):
		self._idx = idx
	
	def resetNum(self, num):
		self._num = num


class CompareInfoToolBox(QToolBox):
	"""Comparison info."""
	
	def __init__(self, idx):
		QToolBox.__init__(self)
		self._idx = idx
		tr = self.tr
		# interaspects
		scroll1 = QScrollArea(self)
		scroll1.setWidgetResizable(True)
		self.addItem(scroll1, tr('Inter Aspects'))
		self.textEdit1 = QTextEdit(self)
		self.textEdit1.setReadOnly(True)
		scroll1.setWidget(self.textEdit1)
		# aspects to midpoints 1
		if app.desktop.charts[idx][0]._filter._calc_midp:
			self.createMidPoints1Tab()
		else:
			self.has_midp1 = False
		# aspects to midpoints 2
		if app.desktop.charts[idx][1]._filter._calc_midp:
			self.createMidPoints2Tab()
		else:
			self.has_midp2 = False
		# inter midpoints aspects
		if app.desktop.charts[idx][0]._filter._calc_midp and (
			app.desktop.charts[idx][1]._filter._calc_midp):
			self.createInterMidPointsTab()
		else:
			self.has_intermidp = False
		self.reset()
	
	def createMidPoints1Tab(self):
		scroll2 = QScrollArea(self)
		scroll2.setWidgetResizable(True)
		self.addItem(scroll2, self.tr('Aspects MidPoints 1'))
		self.textEdit2 = QTextEdit(self)
		self.textEdit2.setReadOnly(True)
		scroll2.setWidget(self.textEdit2)
		self.has_midp1 = True
	
	def createMidPoints2Tab(self):
		scroll3 = QScrollArea(self)
		scroll3.setWidgetResizable(True)
		self.addItem(scroll3, self.tr('Aspects MidPoints 2'))
		self.textEdit3 = QTextEdit(self)
		self.textEdit3.setReadOnly(True)
		scroll3.setWidget(self.textEdit3)
		self.has_midp2 = 2 if self.has_midp1 else 1
	
	def createInterMidPointsTab(self):
		scroll4 = QScrollArea(self)
		scroll4.setWidgetResizable(True)
		self.addItem(scroll4, self.tr('Inter MidPoints'))
		self.textEdit4 = QTextEdit(self)
		self.textEdit4.setReadOnly(True)
		scroll4.setWidget(self.textEdit4)
		self.has_intermidp = True
	
	def reset(self):
		self.createAspects()
		if app.desktop.charts[self._idx][0]._filter._calc_midp:
			if not self.has_midp1:
				self.createMidPoints1Tab()
			self.createMidPoints1()
		else:
			if self.has_midp1:
				self.removeItem(1)
				self.has_midp1 = False
		if app.desktop.charts[self._idx][1]._filter._calc_midp:
			if not self.has_midp2:
				self.createMidPoints2Tab()
			self.createMidPoints2()
		else:
			if self.has_midp2:
				self.removeItem(self.has_midp2)
				self.has_midp2 = False
		if app.desktop.charts[self._idx][0]._filter._calc_midp and (
			app.desktop.charts[self._idx][1]._filter._calc_midp):
			if not self.has_intermidp:
				self.createInterMidPointsTab()
			self.createInterMidPoints()
		else:
			if self.has_intermidp:
				self.removeItem(self.count()-1)
				self.has_intermidp = False
	
	def createAspects(self):
		txt = chthtml.html_aspects(
			app.desktop.charts[self._idx].interaspects.sort_by_precision())
		self.textEdit1.setHtml(txt)
	
	def createMidPoints1(self):
		txt = chthtml.html_intermidp(
			app.desktop.charts[self._idx].intermidp1.sort_by_precision())
		self.textEdit2.setHtml(txt)
	
	def createMidPoints2(self):
		txt = chthtml.html_intermidp(
			app.desktop.charts[self._idx].intermidp2.sort_by_precision())
		self.textEdit3.setHtml(txt)
	
	def createInterMidPoints(self):
		txt = chthtml.html_intermidpoints(
			app.desktop.charts[self._idx].intermidpoints.sort_by_precision())
		self.textEdit4.setHtml(txt)


# End.
