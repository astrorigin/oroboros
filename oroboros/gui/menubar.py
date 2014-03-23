#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Menu bar.

"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *


__all__ = ['createMenuBar']


def createMenuBar(self):
	"""Create menu bar."""
	tr = self.tr
	menuBar = self.menuBar()
	# charts menu
	fileMenu = menuBar.addMenu(tr('&Desktop'))
	fileMenu.addAction(self.actionNewMultiChart)
	fileMenu.addAction(self.actionHereNowMultiChart)
	fileMenu.addAction(self.actionOpenMultiChart)
	fileMenu.addAction(self.actionCustomMultiChart)
	## chart imports
	importMenu = QMenu(tr('Import...'), self)
	importMenu.addAction(self.actionOpenMultiChartA32)
	importMenu.addAction(self.actionOpenMultiChartSkif)
	fileMenu.addMenu(importMenu)
	## chart exports
	exportMenu = QMenu(tr('Export...'), self)
	exportMenu.addAction(self.actionSaveImage)
	fileMenu.addMenu(exportMenu)
	fileMenu.addSeparator()
	fileMenu.addAction(self.actionCloseMultiChart)
	fileMenu.addSeparator()
	fileMenu.addAction(self.actionExit)
	# subcharts menu
	chartMenu = menuBar.addMenu(tr('&SubCharts'))
	chart1Menu = QMenu(tr('Chart 1'), self)
	chart1Menu.addAction(self.actionOpenChart1)
	chart1Menu.addAction(self.actionHideChart1)
	chart1Menu.addAction(self.actionEditChart1)
	chart1Menu.addAction(self.actionFilterChart1)
	chart1Menu.addAction(self.actionSaveChart1)
	chart1Menu.addAction(self.actionSaveChart1As)
	chart1Menu.addAction(self.actionCloseChart1)
	chartMenu.addMenu(chart1Menu)
	chart2Menu = QMenu(tr('Chart 2'), self)
	chart2Menu.addAction(self.actionOpenChart2)
	chart2Menu.addAction(self.actionHideChart2)
	chart2Menu.addAction(self.actionEditChart2)
	chart2Menu.addAction(self.actionFilterChart2)
	chart2Menu.addAction(self.actionSaveChart2)
	chart2Menu.addAction(self.actionSaveChart2As)
	chart2Menu.addAction(self.actionCloseChart2)
	chartMenu.addMenu(chart2Menu)
	chartMenu.addAction(self.actionSwitchCharts)
	chartMenu.addSeparator()
	# compare submenu
	compMenu = QMenu(tr('Compare'), self)
	compMenu.addAction(self.actionTransitMode)
	compMenu.addAction(self.actionProgressionMode)
	compMenu.addAction(self.actionDirectionMode)
	chartMenu.addMenu(compMenu)
	# transform submenu
	transMenu = QMenu(tr('Transform'), self)
	transMenu.addAction(self.actionMultiplyPos)
	transMenu.addAction(self.actionAddPos)
	chartMenu.addMenu(transMenu)
	# merge submenu
	mergeMenu = QMenu(tr('Merge'), self)
	mergeMenu.addAction(self.actionComposite)
	mergeMenu.addAction(self.actionMidSpaceTime)
	chartMenu.addMenu(mergeMenu)
	# configuration menu
	cfgMenu = menuBar.addMenu(tr('&Configuration'))
	cfgMenu.addAction(self.actionSettings)
	cfgMenu.addAction(self.actionFilters)
	cfgMenu.addSeparator()
	cfgMenu.addAction(self.actionPlanetsFilters)
	cfgMenu.addAction(self.actionAspectsFilters)
	cfgMenu.addAction(self.actionOrbsFilters)
	cfgMenu.addAction(self.actionAspectsRestrictions)
	cfgMenu.addAction(self.actionOrbsRestrictions)
	cfgMenu.addAction(self.actionMidPointsFilters)
	# about menu
	aboutMenu = menuBar.addMenu(tr('About'))
	aboutMenu.addAction(self.actionAboutQt)
	aboutMenu.addAction(self.actionAboutOroboros)




# End.
