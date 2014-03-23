#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Chart wheels.

"""

import os.path

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from oroboros.gui import app
from oroboros.gui.chtpainter import ChartPainter


__all__ = ['CentralWidget']


_iconsDir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'icons')


## oroboros.ui.centralwidget.CentralWidget
class CentralWidget(QTabWidget):
	
	def __init__(self, parent):
		QTabWidget.__init__(self, parent)
		self.connect(self, SIGNAL('currentChanged(int)'),
			parent.centralTabChangedEvent)
	
	def addTab(self, idx):
		"""Create a new chart tab."""
		tab = ChartWheelWidget(idx)
		QTabWidget.addTab(self, tab, app.desktop.charts[idx][0]._name)
	
	def tabRemoved(self, idx):
		for i in range(len(app.desktop.charts)):
			self.widget(i).resetIdx(i)
		app.mainwin.resetActions()
	
	def tabInserted(self, idx):
		app.mainwin.resetActions()
	
	def resetTab(self, idx):
		"""Reload chart tab."""
		self.setTabText(idx, app.desktop.charts[idx][0]._name)
		self.widget(idx).reset()
	
	def paintEvent(self, event):
		if len(app.desktop.charts) == 0:
			self.drawOroboros()
	
	def drawOroboros(self):
		"""Paint the Oroboros on empty window."""
		painter = QPainter(self)
		im = QImage(os.path.join(_iconsDir, 'oroboros.png'))
		target = QRect(
			(self.width()/2.0)-170, (self.height()/2.0)-170, 340, 340)
		painter.drawImage(target, im, QRect(0, 0, 340, 340))



## oroboros.ui.centralwidget.ChartWheelWidget
class ChartWheelWidget(QWidget):
	
	def __init__(self, idx):
		QWidget.__init__(self)
		self._idx = idx
	
	def paintEvent(self, event):
		"""Draw chart on widget."""
		painter = ChartPainter(self, app.desktop.charts[self._idx])
	
	def reset(self):
		"""Force repaint chart."""
		self.update()
	
	def resetIdx(self, idx):
		"""Modify chart idx."""
		self._idx = idx



# End.
