#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Tool bar.

"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *


__all__ = ['createToolBar']


def createToolBar(self):
	"""Create tool bar."""
	tr = self.tr
	# file actions
	toolBar = self.addToolBar(tr('Toolbar'))
	toolBar.addAction(self.actionNewMultiChart)
	toolBar.addAction(self.actionCloseMultiChart)
	toolBar.addSeparator()
	# charts actions
	toolBar.addAction(self.actionOpenChart1)
	toolBar.addAction(self.actionHideChart1)
	toolBar.addAction(self.actionEditChart1)
	toolBar.addAction(self.actionFilterChart1)
	toolBar.addAction(self.actionSaveChart1)
	toolBar.addAction(self.actionCloseChart1)
	toolBar.addSeparator()
	toolBar.addAction(self.actionOpenChart2)
	toolBar.addAction(self.actionHideChart2)
	toolBar.addAction(self.actionEditChart2)
	toolBar.addAction(self.actionFilterChart2)
	toolBar.addAction(self.actionSaveChart2)
	toolBar.addAction(self.actionCloseChart2)
	toolBar.addSeparator()
	toolBar.addAction(self.actionSwitchCharts)
	toolBar.addSeparator()
	toolBar.addAction(self.actionTransitMode)
	toolBar.addAction(self.actionProgressionMode)
	toolBar.addAction(self.actionDirectionMode)
##	toolBar.addSeparator()
##	toolBar.addAction(self.actionMultiplyPos)
##	toolBar.addAction(self.actionAddPos)
##	toolBar.addSeparator()
##	toolBar.addAction(self.actionComposite)
##	toolBar.addAction(self.actionMidSpaceTime)
	# quit
	toolBar.addSeparator()
	toolBar.addAction(self.actionExit)


# End.
