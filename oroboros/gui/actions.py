#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Main window actions.

"""

import os.path

from PyQt4.QtCore import *
from PyQt4.QtGui import *


__all__ = ['createActions', 'reset']


_baseDir = os.path.dirname(os.path.abspath(__file__))
_iconsDir = os.path.join(_baseDir, 'icons')


def createActions(self):
	"""Create main actions."""
	tr = self.tr
	
	# ### multi charts actions ###
	
	# New Chart
	self.actionNewMultiChart = QAction(
		QIcon(os.path.join(_iconsDir, 'new-all.png')),
		tr('New Chart'), self)
	self.actionNewMultiChart.setShortcut(tr('Ctrl+N', 'New chart shortcut'))
	self.actionNewMultiChart.setToolTip(tr('New Chart'))
	self.actionNewMultiChart.setStatusTip(tr('New Chart'))
	self.connect(self.actionNewMultiChart, SIGNAL('triggered()'),
		self.newMultiChartEvent)
	# Here-Now Chart
	self.actionHereNowMultiChart = QAction(
		QIcon(os.path.join(_iconsDir, 'gtk-home.png')),
		tr('Here-Now'), self)
	##self.actionHereNowMultiChart.setShortcut()
	self.actionHereNowMultiChart.setToolTip(tr('Here-Now'))
	self.actionHereNowMultiChart.setStatusTip(tr('Here-Now'))
	self.connect(self.actionHereNowMultiChart, SIGNAL('triggered()'),
		self.hereNowMultiChartEvent)
	# Open chart
	self.actionOpenMultiChart = QAction(
		QIcon(os.path.join(_iconsDir, 'open-all.png')),
		tr('Open Chart'), self)
	self.actionOpenMultiChart.setShortcut(tr('Ctrl+O', 'Open chart shortcut'))
	self.actionOpenMultiChart.setToolTip(tr('Open Chart'))
	self.actionOpenMultiChart.setStatusTip(tr('Open Chart'))
	self.connect(self.actionOpenMultiChart, SIGNAL('triggered()'),
		self.openMultiChartEvent)
	# Open Astrolog32 file
	self.actionOpenMultiChartA32 = QAction(
		QIcon(os.path.join(_iconsDir, 'astrolog32.png')),
		tr('Astrolog32 Chart'), self)
	self.actionOpenMultiChartA32.setToolTip(tr('Astrolog32 Chart'))
	self.actionOpenMultiChartA32.setStatusTip(tr('Astrolog32 Chart'))
	self.connect(self.actionOpenMultiChartA32, SIGNAL('triggered()'),
		self.openMultiChartA32Event)
	# Open Skylendar chart
	self.actionOpenMultiChartSkif = QAction(
		QIcon(os.path.join(_iconsDir, 'skif.png')),
		tr('Skylendar Chart'), self)
	self.actionOpenMultiChartSkif.setToolTip(tr('Skylendar Chart'))
	self.actionOpenMultiChartSkif.setStatusTip(tr('Skylendar Chart'))
	self.connect(self.actionOpenMultiChartSkif, SIGNAL('triggered()'),
		self.openMultiChartSkifEvent)
	# Custom chart
	self.actionCustomMultiChart = QAction(
		QIcon(os.path.join(_iconsDir, 'edit-all.png')),
		tr('Custom Chart'), self)
	##self.actionCustomMultiChart.setShortCut()
	self.actionCustomMultiChart.setToolTip(tr('Custom Chart'))
	self.actionCustomMultiChart.setStatusTip(tr('Custom Chart'))
	self.connect(self.actionCustomMultiChart, SIGNAL('triggered()'),
		self.customMultiChartEvent)
	# Close chart
	self.actionCloseMultiChart = QAction(
		QIcon(os.path.join(_iconsDir, 'close-all.png')),
		tr('Close Chart'), self)
	self.actionCloseMultiChart.setToolTip(tr('Close Chart'))
	self.actionCloseMultiChart.setStatusTip(tr('Close Chart'))
	self.connect(self.actionCloseMultiChart, SIGNAL('triggered()'),
		self.closeMultiChartEvent)
	# Save image
	self.actionSaveImage = QAction(
		QIcon(os.path.join(_iconsDir, 'image.png')),
		tr('Save Image...'), self)
	self.actionSaveImage.setToolTip(tr('Save Image...'))
	self.actionSaveImage.setStatusTip(tr('Save Image...'))
	self.connect(self.actionSaveImage, SIGNAL('triggered()'),
		self.saveImageEvent)
	# Quit Oroboros
	self.actionExit = QAction(
		QIcon(os.path.join(_iconsDir, 'gtk-quit.png')),
		tr('Quit Oroboros'), self)
	self.actionExit.setShortcut(tr('Ctrl+Q', 'Quit shortcut'))
	self.actionExit.setToolTip(tr('Quit Oroboros'))
	self.actionExit.setStatusTip(tr('Quit Oroboros'))
	self.connect(self.actionExit, SIGNAL('triggered()'),
		SLOT('close()'))
	
	# ## configuration ###
	
	# Edit settings
	self.actionSettings = QAction(
		QIcon(os.path.join(_iconsDir, 'gtk-preferences.png')),
		tr('Settings'), self)
	self.actionSettings.setToolTip(tr('Edit Settings'))
	self.actionSettings.setStatusTip(tr('Edit Settings'))
	self.connect(self.actionSettings, SIGNAL('triggered()'),
		self.editSettingsEvent)
	# Filters manager
	self.actionFilters = QAction(
		QIcon(os.path.join(_iconsDir, 'gtk-execute.png')),
		tr('Filters'), self)
	self.actionFilters.setToolTip(tr('Manage Filters'))
	self.actionFilters.setStatusTip(tr('Manage Filters'))
	self.connect(self.actionFilters, SIGNAL('triggered()'),
		self.manageFiltersEvent)
	# Planets filters manager
	self.actionPlanetsFilters = QAction(
		QIcon(os.path.join(_iconsDir, 'gtk-execute.png')),
			tr('Planets Filters'), self)
	self.actionPlanetsFilters.setToolTip(tr('Manage Planets Filters'))
	self.actionPlanetsFilters.setStatusTip(tr('Manage Planets Filters'))
	self.connect(self.actionPlanetsFilters, SIGNAL('triggered()'),
		self.managePlanetsFiltersEvent)
	# Aspects filters manager
	self.actionAspectsFilters = QAction(
		QIcon(os.path.join(_iconsDir, 'gtk-execute.png')),
			tr('Aspects Filters'), self)
	self.actionAspectsFilters.setToolTip(tr('Manage Aspects Filters'))
	self.actionAspectsFilters.setStatusTip(tr('Manage Aspects Filters'))
	self.connect(self.actionAspectsFilters, SIGNAL('triggered()'),
		self.manageAspectsFiltersEvent)
	# Orbs filters manager
	self.actionOrbsFilters = QAction(
		QIcon(os.path.join(_iconsDir, 'gtk-execute.png')),
			tr('Orbs Filters'), self)
	self.actionOrbsFilters.setToolTip(tr('Manage Orbs Filters'))
	self.actionOrbsFilters.setStatusTip(tr('Manage Orbs Filters'))
	self.connect(self.actionOrbsFilters, SIGNAL('triggered()'),
		self.manageOrbsFiltersEvent)
	# Aspects restrictions manager
	self.actionAspectsRestrictions = QAction(
		QIcon(os.path.join(_iconsDir, 'gtk-execute.png')),
			tr('Aspects Restrictions'), self)
	self.actionAspectsRestrictions.setToolTip(tr('Manage Aspects Restrictions'))
	self.actionAspectsRestrictions.setStatusTip(tr('Manage Aspects Restrictions'))
	self.connect(self.actionAspectsRestrictions, SIGNAL('triggered()'),
		self.manageAspectsRestrictionsEvent)
	# Orbs restrictions manager
	self.actionOrbsRestrictions = QAction(
		QIcon(os.path.join(_iconsDir, 'gtk-execute.png')),
			tr('Orbs Restrictions'), self)
	self.actionOrbsRestrictions.setToolTip(tr('Manage Orbs Restrictions'))
	self.actionOrbsRestrictions.setStatusTip(tr('Manage Orbs Restrictions'))
	self.connect(self.actionOrbsRestrictions, SIGNAL('triggered()'),
		self.manageOrbsRestrictionsEvent)
	# Midpoints filters manager
	self.actionMidPointsFilters = QAction(
		QIcon(os.path.join(_iconsDir, 'gtk-execute.png')),
			tr('MidPoints Filters'), self)
	self.actionMidPointsFilters.setToolTip(tr('Manage MidPoints Filters'))
	self.actionMidPointsFilters.setStatusTip(tr('Manage MidPoints Filters'))
	self.connect(self.actionMidPointsFilters, SIGNAL('triggered()'),
		self.manageMidPointsFiltersEvent)
	
	# ### sub charts actions ###
	
	# open chart 1
	self.actionOpenChart1 = QAction(
		QIcon(os.path.join(_iconsDir, 'open-1.png')),
		tr('Open Chart 1'), self)
	##self.actionOpenChart1.setShortcut(tr('Ctrl+O', 'Open chart 1'))
	self.actionOpenChart1.setToolTip(tr('Open Chart 1'))
	self.actionOpenChart1.setStatusTip(tr('Open Chart 1'))
	self.connect(self.actionOpenChart1, SIGNAL('triggered()'),
		self.openChart1Event)
	# open chart 2
	self.actionOpenChart2 = QAction(
		QIcon(os.path.join(_iconsDir, 'open-2.png')),
		tr('Open Chart 2'), self)
	##self.actionOpenChart2.setShortcut(tr('Ctrl+O', 'Open chart 2'))
	self.actionOpenChart2.setToolTip(tr('Open Chart 2'))
	self.actionOpenChart2.setStatusTip(tr('Open Chart 2'))
	self.connect(self.actionOpenChart2, SIGNAL('triggered()'),
		self.openChart2Event)
	# hide chart 1
	self.actionHideChart1 = QAction(
		QIcon(os.path.join(_iconsDir, 'find-1.png')),
		tr('Show/Hide Chart 1'), self)
	self.actionHideChart1.setToolTip(tr('Show/Hide Chart 1'))
	self.actionHideChart1.setStatusTip(tr('Show/Hide Chart 1'))
	self.actionHideChart1.setCheckable(True)
	self.connect(self.actionHideChart1, SIGNAL('triggered()'),
		self.hideChart1Event)
	# hide chart 2
	self.actionHideChart2 = QAction(
		QIcon(os.path.join(_iconsDir, 'find-2.png')),
		tr('Show/Hide Chart 2'), self)
	self.actionHideChart2.setToolTip(tr('Show/Hide Chart 2'))
	self.actionHideChart2.setStatusTip(tr('Show/Hide Chart 2'))
	self.actionHideChart2.setCheckable(True)
	self.connect(self.actionHideChart2, SIGNAL('triggered()'),
		self.hideChart2Event)
	# edit chart 1
	self.actionEditChart1 = QAction(
		QIcon(os.path.join(_iconsDir, 'edit-1.png')),
		tr('Edit Chart 1'), self)
	self.actionEditChart1.setToolTip(tr('Edit Chart 1'))
	self.actionEditChart1.setStatusTip(tr('Edit Chart 1'))
	self.connect(self.actionEditChart1, SIGNAL('triggered()'),
		self.editChart1Event)
	# edit chart 2
	self.actionEditChart2 = QAction(
		QIcon(os.path.join(_iconsDir, 'edit-2.png')),
		tr('Edit Chart 2'), self)
	self.actionEditChart2.setToolTip(tr('Edit Chart 2'))
	self.actionEditChart2.setStatusTip(tr('Edit Chart 2'))
	self.connect(self.actionEditChart2, SIGNAL('triggered()'),
		self.editChart2Event)
	# settings chart 1
	self.actionFilterChart1 = QAction(
		QIcon(os.path.join(_iconsDir, 'properties-1.png')),
		tr('Chart 1 Filter'), self)
	self.actionFilterChart1.setToolTip(tr('Chart 1 Filter'))
	self.actionFilterChart1.setStatusTip(tr('Chart 1 Filter'))
	self.connect(self.actionFilterChart1, SIGNAL('triggered()'),
		self.filterChart1Event)
	# settings chart 2
	self.actionFilterChart2 = QAction(
		QIcon(os.path.join(_iconsDir, 'properties-2.png')),
		tr('Chart 2 Filter'), self)
	self.actionFilterChart2.setToolTip(tr('Chart 2 Filter'))
	self.actionFilterChart2.setStatusTip(tr('Chart 2 Filter'))
	self.connect(self.actionFilterChart2, SIGNAL('triggered()'),
		self.filterChart2Event)
	# save chart 1
	self.actionSaveChart1 = QAction(
		QIcon(os.path.join(_iconsDir, 'save-1.png')),
		tr('Save Chart 1'), self)
	self.actionSaveChart1.setToolTip(tr('Save Chart 1'))
	self.actionSaveChart1.setStatusTip(tr('Save Chart 1'))
	self.connect(self.actionSaveChart1, SIGNAL('triggered()'),
		self.saveChart1Event)
	# save chart 2
	self.actionSaveChart2 = QAction(
		QIcon(os.path.join(_iconsDir, 'save-2.png')),
		tr('Save Chart 2'), self)
	self.actionSaveChart2.setToolTip(tr('Save Chart 2'))
	self.actionSaveChart2.setStatusTip(tr('Save Chart 2'))
	self.connect(self.actionSaveChart2, SIGNAL('triggered()'),
		self.saveChart2Event)
	# save chart 1 as
	self.actionSaveChart1As = QAction(
		QIcon(os.path.join(_iconsDir, 'save-as-1.png')),
		tr('Save Chart 1 As...'), self)
	self.actionSaveChart1As.setToolTip(tr('Save Chart 1 As...'))
	self.actionSaveChart1As.setStatusTip(tr('Save Chart 1 As...'))
	self.connect(self.actionSaveChart1As, SIGNAL('triggered()'),
		self.saveChart1AsEvent)
	# save chart 2 as
	self.actionSaveChart2As = QAction(
		QIcon(os.path.join(_iconsDir, 'save-as-2.png')),
		tr('Save Chart 2 As...'), self)
	self.actionSaveChart2As.setToolTip(tr('Save Chart 2 As...'))
	self.actionSaveChart2As.setStatusTip(tr('Save Chart 2 As...'))
	self.connect(self.actionSaveChart2As, SIGNAL('triggered()'),
		self.saveChart2AsEvent)
	# close chart 1
	self.actionCloseChart1 = QAction(
		QIcon(os.path.join(_iconsDir, 'close-1.png')),
		tr('Close Chart 1'), self)
	self.actionCloseChart1.setToolTip(tr('Close Chart 1'))
	self.actionCloseChart1.setStatusTip(tr('Close Chart 1'))
	self.connect(self.actionCloseChart1, SIGNAL('triggered()'),
		self.closeChart1Event)
	# close chart 2
	self.actionCloseChart2 = QAction(
		QIcon(os.path.join(_iconsDir, 'close-2.png')),
		tr('Close Chart 2'), self)
	self.actionCloseChart2.setToolTip(tr('Close Chart 2'))
	self.actionCloseChart2.setStatusTip(tr('Close Chart 2'))
	self.connect(self.actionCloseChart2, SIGNAL('triggered()'),
		self.closeChart2Event)
	
	# ### comparison modes ###
	
	# switch charts
	self.actionSwitchCharts = QAction(
		QIcon(os.path.join(_iconsDir, 'gtk-refresh.png')),
		tr('Switch Charts'), self)
	self.actionSwitchCharts.setToolTip(tr('Switch Charts'))
	self.actionSwitchCharts.setStatusTip(tr('Switch Charts'))
	self.actionSwitchCharts.setCheckable(True)
	self.connect(self.actionSwitchCharts, SIGNAL('triggered()'),
		self.switchChartsEvent)
	# transit mode
	self.actionTransitMode = QAction(
		QIcon(os.path.join(_iconsDir, 'transit.png')),
		tr('Transit'), self)
	self.actionTransitMode.setShortcut(tr('Ctrl+T', 'Transit shortcut'))
	self.actionTransitMode.setToolTip(tr('Transit'))
	self.actionTransitMode.setStatusTip(tr('Transit'))
	self.connect(self.actionTransitMode, SIGNAL('triggered()'),
		self.transitModeEvent)
	# progression mode
	self.actionProgressionMode = QAction(
		QIcon(os.path.join(_iconsDir, 'progression.png')),
		tr('Progression'), self)
	self.actionProgressionMode.setShortcut(tr('Ctrl+P', 'Progression Shortcut'))
	self.actionProgressionMode.setToolTip(tr('Progression'))
	self.actionProgressionMode.setStatusTip(tr('Progression'))
	self.connect(self.actionProgressionMode, SIGNAL('triggered()'),
		self.progressionModeEvent)
	# direction mode
	self.actionDirectionMode = QAction(
		QIcon(os.path.join(_iconsDir, 'direction.png')),
		tr('Direction'), self)
	self.actionDirectionMode.setShortcut(tr('Ctrl+D', 'Direction shortcut'))
	self.actionDirectionMode.setToolTip(tr('Direction'))
	self.actionDirectionMode.setStatusTip(tr('Direction'))
	self.connect(self.actionDirectionMode, SIGNAL('triggered()'),
		self.directionModeEvent)
	
	# ### transform ###
	
	# multiply positions
	self.actionMultiplyPos = QAction(
		QIcon(os.path.join(_iconsDir, 'multiply.png')),
		tr('Multiply Positions'), self)
	self.actionMultiplyPos.setShortcut(tr('Ctrl+M', 'Multiply pos shortcut'))
	self.actionMultiplyPos.setToolTip(tr('Multiply Positions'))
	self.actionMultiplyPos.setStatusTip(tr('Multiply Positions'))
	self.connect(self.actionMultiplyPos, SIGNAL('triggered()'),
		self.multiplyPosEvent)
	# add degrees value
	self.actionAddPos = QAction(
		QIcon(os.path.join(_iconsDir, 'add.png')),
		tr('Add Degrees'), self)
	self.actionAddPos.setShortcut(tr('Ctrl+A', 'Add degrees shortcut'))
	self.actionAddPos.setToolTip(tr('Add Degrees'))
	self.actionAddPos.setStatusTip(tr('Add Degrees'))
	self.connect(self.actionAddPos, SIGNAL('triggered()'),
		self.addPosEvent)
	
	# ### merge ###
	
	# composite chart
	self.actionComposite = QAction(
		QIcon(os.path.join(_iconsDir, 'composite.png')),
		tr('Composite'), self)
	self.actionComposite.setShortcut(tr('Ctrl+C', 'Composite shortcut'))
	self.actionComposite.setToolTip(tr('Composite'))
	self.actionComposite.setStatusTip(tr('Composite'))
	self.connect(self.actionComposite, SIGNAL('triggered()'),
		self.compositeEvent)
	# mid-space/time chart
	self.actionMidSpaceTime = QAction(
		QIcon(os.path.join(_iconsDir, 'midspacetime.png')),
		tr('Mid-Space/Time'), self)
	self.actionMidSpaceTime.setShortcut(tr('Ctrl+X', 'Mid-space/time shortcut'))
	self.actionMidSpaceTime.setToolTip(tr('Mid-Space/Time'))
	self.actionMidSpaceTime.setStatusTip(tr('Mid-Space/Time'))
	self.connect(self.actionMidSpaceTime, SIGNAL('triggered()'),
		self.midSpaceTimeEvent)
	
	# ### about actions ###
	
	# About Qt
	self.actionAboutQt = QAction(
		QIcon(os.path.join(_iconsDir, 'gtk-about.png')),
		tr('About Qt'), self)
	self.actionAboutQt.setToolTip(tr('About Qt'))
	self.actionAboutQt.setStatusTip(tr('About Qt'))
	self.connect(self.actionAboutQt, SIGNAL('triggered()'),
		self.aboutQtEvent)
	# About Oroboros
	self.actionAboutOroboros = QAction(
		QIcon(os.path.join(_iconsDir, 'gtk-about.png')),
		tr('About Oroboros'), self)
	self.actionAboutOroboros.setToolTip(tr('About Oroboros'))
	self.actionAboutOroboros.setStatusTip(tr('About Oroboros'))
	self.connect(self.actionAboutOroboros, SIGNAL('triggered()'),
		self.aboutOroborosEvent)



def reset(self, app):
	"""Enable/disable actions."""
	if len(app.desktop.charts) == 0:
		self.actionSaveImage.setDisabled(True)
		self.actionCloseMultiChart.setDisabled(True)
		self.actionOpenChart1.setDisabled(True)
		self.actionHideChart1.setDisabled(True)
		self.actionHideChart1.setChecked(False)
		self.actionEditChart1.setDisabled(True)
		self.actionFilterChart1.setDisabled(True)
		self.actionSaveChart1.setDisabled(True)
		self.actionSaveChart1As.setDisabled(True)
		self.actionCloseChart1.setDisabled(True)
		self.actionOpenChart2.setDisabled(True)
		self.actionHideChart2.setDisabled(True)
		self.actionHideChart2.setChecked(False)
		self.actionEditChart2.setDisabled(True)
		self.actionFilterChart2.setDisabled(True)
		self.actionSaveChart2.setDisabled(True)
		self.actionSaveChart2As.setDisabled(True)
		self.actionCloseChart2.setDisabled(True)
		self.actionSwitchCharts.setDisabled(True)
		self.actionSwitchCharts.setChecked(False)
		self.actionTransitMode.setDisabled(True)
		self.actionProgressionMode.setDisabled(True)
		self.actionDirectionMode.setDisabled(True)
		self.actionMultiplyPos.setDisabled(True)
		self.actionAddPos.setDisabled(True)
		self.actionComposite.setDisabled(True)
		self.actionMidSpaceTime.setDisabled(True)
	else: ## one multichart
		self.actionSaveImage.setEnabled(True)
		self.actionCloseMultiChart.setEnabled(True)
		self.actionOpenChart1.setEnabled(True)
		self.actionHideChart1.setEnabled(True)
		if app.desktop.charts[self.central.currentIndex()][0]._hidden:
			self.actionHideChart1.setChecked(True)
			self.actionMultiplyPos.setDisabled(True)
			self.actionAddPos.setDisabled(True)
		else:
			self.actionHideChart1.setChecked(False)
			self.actionMultiplyPos.setEnabled(True)
			self.actionAddPos.setEnabled(True)
		self.actionEditChart1.setEnabled(True)
		self.actionFilterChart1.setEnabled(True)
		self.actionSaveChart1.setEnabled(True)
		self.actionSaveChart1As.setEnabled(True)
		self.actionOpenChart2.setEnabled(True)
		self.actionTransitMode.setEnabled(True)
		self.actionProgressionMode.setEnabled(True)
		self.actionDirectionMode.setEnabled(True)
		self.actionDirectionMode.setEnabled(True)
		if len(app.desktop.charts[self.central.currentIndex()]) > 1: ## two subcharts
			self.actionCloseChart1.setEnabled(True)
			self.actionOpenChart2.setEnabled(True)
			self.actionHideChart2.setEnabled(True)
			if app.desktop.charts[self.central.currentIndex()][1]._hidden:
				self.actionHideChart2.setChecked(True)
			else:
				self.actionHideChart2.setChecked(False)
				self.actionMultiplyPos.setEnabled(True)
				self.actionAddPos.setEnabled(True)
			self.actionEditChart2.setEnabled(True)
			self.actionFilterChart2.setEnabled(True)
			self.actionSaveChart2.setEnabled(True)
			self.actionSaveChart2As.setEnabled(True)
			self.actionCloseChart2.setEnabled(True)
			self.actionSwitchCharts.setEnabled(True)
			if app.desktop.charts[self.central.currentIndex()]._switched:
				self.actionSwitchCharts.setChecked(True)
			else:
				self.actionSwitchCharts.setChecked(False)
			self.actionComposite.setEnabled(True)
			self.actionMidSpaceTime.setEnabled(True)
		else: ## one subchart
			self.actionCloseChart1.setDisabled(True)
			self.actionHideChart2.setDisabled(True)
			self.actionEditChart2.setDisabled(True)
			self.actionFilterChart2.setDisabled(True)
			self.actionSaveChart2.setDisabled(True)
			self.actionSaveChart2As.setDisabled(True)
			self.actionCloseChart2.setDisabled(True)
			self.actionSwitchCharts.setDisabled(True)
			self.actionSwitchCharts.setChecked(False)
			self.actionComposite.setDisabled(True)
			self.actionMidSpaceTime.setDisabled(True)
	


# End.
