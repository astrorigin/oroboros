#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Main window.

"""

import sys
import os.path

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import oroboros
from oroboros.core import cfg
from oroboros.core import astrolog32
from oroboros.core import skylendar
from oroboros.core import hgrepo
from oroboros.core.charts import Chart
from oroboros.core.filters import Filter

from oroboros.gui import app
from oroboros.gui import translations
from oroboros.gui import actions
from oroboros.gui import menubar
from oroboros.gui import toolbar
from oroboros.gui import chtimage

from oroboros.gui.dockwidget import DockWidget
from oroboros.gui.centralwidget import CentralWidget
from oroboros.gui.chtinfodialog import ChartInfoDialog
from oroboros.gui.newtabdialog import NewTabDialog
from oroboros.gui.saveimagedialog import SaveImageDialog
from oroboros.gui.cfgdialog import CfgDialog
from oroboros.gui.profectiondialog import ProfectionDialog
from oroboros.gui.harmonicsdialog import HarmonicsDialog
from oroboros.gui.filtersmandialog import FiltersManagerDialog
from oroboros.gui.filterdialog import FilterDialog
from oroboros.gui.plntfiltersmandialog import PlanetsFiltersManagerDialog
from oroboros.gui.aspfiltersmandialog import AspectsFiltersManagerDialog
from oroboros.gui.orbfiltersmandialog import OrbsFiltersManagerDialog
from oroboros.gui.asprestrmandialog import AspectsRestrictionsManagerDialog
from oroboros.gui.orbrestrmandialog import OrbsRestrictionsManagerDialog
from oroboros.gui.midpfiltersmandialog import MidPointsFiltersManagerDialog


__all__ = ['MainWindow', 'main']


_baseDir = os.path.dirname(os.path.abspath(__file__))
_iconsDir = os.path.join(_baseDir, 'icons')


class MainWindow(QMainWindow):
	
	def __init__(self):
		QMainWindow.__init__(self)
		tr = self.tr
		# create main window
		self.resize(900, 650)
		self.setWindowTitle(tr('Oroboros', 'Window title'))
		self.setWindowIcon(
			QIcon(os.path.join(_iconsDir, 'oroboros.png')))
		# actions
		actions.createActions(self)
		actions.reset(self, app)
		# menu bar
		menubar.createMenuBar(self)
		# tool bar
		toolbar.createToolBar(self)
		# dock widget
		self.dock = DockWidget(self)
		self.addDockWidget(Qt.LeftDockWidgetArea, self.dock)
		# central widget
		self.central = CentralWidget(self)
		self.setCentralWidget(self.central)
	
	def addTabs(self, idx):
		"""Create the tabs for a new chart."""
		self.dock.addTab(idx)
		self.central.addTab(idx)
		self.resetActions()
	
	def resetTabs(self, idx):
		"""Force reloading a chart."""
		self.dock.resetTab(idx)
		self.central.resetTab(idx)
		self.resetActions()
	
	def removeTabs(self, idx):
		"""Destroy chart tabs."""
		self.dock.removeTab(idx)
		self.central.removeTab(idx)
		self.resetActions()
	
	def dockTabChangedEvent(self):
		idx = self.dock.tabs.currentIndex()
		self.central.setCurrentIndex(idx)
		self.resetActions()
	
	def centralTabChangedEvent(self):
		idx = self.central.currentIndex()
		self.dock.tabs.setCurrentIndex(idx)
		self.resetActions()
	
	def resetActions(self):
		actions.reset(self, app)
	
	# ### about actions events ####
	
	def aboutQtEvent(self):
		QMessageBox.aboutQt(self, self.tr('About Qt'))
	
	def aboutOroborosEvent(self):
		msg = unicode(self.tr("""<qt>This is <b><i>Oroboros</i></b> astrology software (version %(version)s).<br><br>

Copyright &copy; 2008 Stanislas Marquis <a href="mailto:stnsls@gmail.com">stnsls@gmail.com</a><br>
Homepage <a href="http://pypi.python.org/pypi/oroboros">http://pypi.python.org/pypi/oroboros</a><br><br>

This is free software; see the license for copying conditions.<br>
There is NO warranty; not even for MERCHANTABILITY or<br>
FITNESS FOR A PARTICULAR PURPOSE.</qt>""")) % {'version': oroboros.__version__}
		QMessageBox.about(self, self.tr('About Oroboros'), msg)
	
	# ### file actions events ###
	
	def newMultiChartEvent(self):
		"""Open the Newtab dialog."""
		ok, do = NewTabDialog(self).exec_()
		if not ok:
			return
		if do == 0:
			self.hereNowMultiChartEvent()
		elif do == 1:
			self.openMultiChartEvent()
		elif do == 2:
			self.customMultiChartEvent()
		elif do == 3:
			self.openMultiChartA32Event()
		elif do == 4:
			self.openMultiChartSkifEvent()
	
	def hereNowMultiChartEvent(self):
		"""Create a default here-now chart."""
		app.appendMultiChart(Chart())
	
	def openMultiChartEvent(self):
		"""Open oroboros chart file."""
		tr = self.tr
		path = unicode(QFileDialog.getOpenFileName(self, tr('Open chart'),
			os.path.expanduser(cfg.charts_dir), tr('Oroboros (*.xml)')))
		if path != '':
			cht = Chart(path)
			app.appendMultiChart(cht)
	
	def openMultiChartA32Event(self):
		"""Open astrolog32 chart file."""
		tr = self.tr
		path = unicode(QFileDialog.getOpenFileName(self,
			tr('Import Astrolog32 chart'),
			os.path.expanduser(cfg.charts_dir), tr('Astrolog32 (*.dat)')))
		if path != '':
			cht = astrolog32.load(path)
			cht.calc()
			app.appendMultiChart(cht)
	
	def openMultiChartSkifEvent(self):
		"""Open skylendar chart file."""
		tr = self.tr
		path = unicode(QFileDialog.getOpenFileName(self,
			tr('Import Skylendar chart'),
			os.path.expanduser(cfg.charts_dir), tr('Skylendar (*.skif)')))
		if path != '':
			cht = skylendar.load(path)
			cht.calc()
			app.appendMultiChart(cht)
	
	def customMultiChartEvent(self):
		"""Open chart dialog for a new tab."""
		ChartInfoDialog(-1, 0, self).exec_()
	
	def saveImageEvent(self):
		"""Open image dialog and create image file."""
		idx = self.dock.tabs.currentIndex()
		ok, fname, ext, w, h = SaveImageDialog(self).exec_()
		if ok:
			if ext == 'svg':
				chtimage.makeSvg(app.desktop.charts[idx], fname, w, h)
			else:
				chtimage.makeImage(app.desktop.charts[idx], fname, ext, w, h)
	
	def closeMultiChartEvent(self):
		"""Close tab."""
		idx = self.dock.tabs.currentIndex()
		app.removeMultiChart(idx)
	
	# ### charts actions events ###
	
	def openChart1Event(self):
		tr = self.tr
		idx = self.dock.tabs.currentIndex()
		path = unicode(QFileDialog.getOpenFileName(self, tr('Open chart 1'),
			os.path.expanduser(cfg.charts_dir), tr('Oroboros (*.xml)')))
		if path != '':
			cht = Chart(path)
			app.replaceChart(idx, 0, cht)
	
	def openChart2Event(self):
		tr = self.tr
		idx = self.dock.tabs.currentIndex()
		path = unicode(QFileDialog.getOpenFileName(self, tr('Open chart 2'),
			os.path.expanduser(cfg.charts_dir), tr('Oroboros (*.xml)')))
		if path != '':
			cht = Chart(path)
			app.replaceChart(idx, 1, cht)
	
	def hideChart1Event(self):
		idx = self.central.currentIndex()
		app.desktop.charts[idx][0]._hidden = not app.desktop.charts[idx][0]._hidden
		self.central.resetTab(idx)
	
	def hideChart2Event(self):
		idx = self.central.currentIndex()
		app.desktop.charts[idx][1]._hidden = not app.desktop.charts[idx][1]._hidden
		self.central.resetTab(idx)
	
	def editChart1Event(self):
		idx = self.dock.tabs.currentIndex()
		ChartInfoDialog(idx, 0, self).exec_()
	
	def editChart2Event(self):
		idx = self.dock.tabs.currentIndex()
		ChartInfoDialog(idx, 1, self).exec_()
	
	def filterChart1Event(self):
		ok, filt = FiltersManagerDialog(self, mode='select').exec_()
		if ok:
			idx = self.dock.tabs.currentIndex()
			app.desktop.charts[idx].set(0, filter=filt)
			self.resetTabs(idx)
	
	def filterChart2Event(self):
		ok, filt = FiltersManagerDialog(self, mode='select').exec_()
		if ok:
			idx = self.dock.tabs.currentIndex()
			app.desktop.charts[idx].set(1, filter=filt)
			self.resetTabs(idx)
	
	def saveChart1Event(self):
		idx = self.dock.tabs.currentIndex()
		cht = app.desktop.charts[idx][0]
		tr = self.tr
		if cht._path == None:
			path = unicode(QFileDialog.getSaveFileName(self,
				tr('Save Chart 1'),
				os.path.expanduser(cfg.charts_dir), tr('Oroboros (*.xml)')))
			if path != '':
				if not path.endswith('.xml'):
					path = '%s%s' % (path, '.xml')
				cht._path = path
			else:
				return
		cht.write()
		QMessageBox.information(self, tr('Save Chart 1'),
			unicode(
				tr('Successfully saved chart \xab %(chart)s \xbb\nwith path \xab %(path)s \xbb')) % {
					'chart': cht._name, 'path': cht._path})
	
	def saveChart2Event(self):
		idx = self.dock.tabs.currentIndex()
		cht = app.desktop.charts[idx][1]
		tr = self.tr
		if cht._path == None:
			path = unicode(QFileDialog.getSaveFileName(self,
				tr('Save Chart 2'),
				os.path.expanduser(cfg.charts_dir), tr('Oroboros (*.xml)')))
			if path != '':
				if not path.endswith('.xml'):
					path = '%s%s' % (path, '.xml')
				cht._path = path
			else:
				return
		cht.write()
		QMessageBox.information(self, tr('Save Chart 2'),
			unicode(
				tr('Successfully saved chart \xab %(chart)s \xbb\nwith path \xab %(path)s \xbb')) % {
					'chart': cht._name, 'path': cht._path})
	
	def saveChart1AsEvent(self):
		idx = self.dock.tabs.currentIndex()
		cht = app.desktop.charts[idx][0]
		tr = self.tr
		path = str(QFileDialog.getSaveFileName(self,
			tr('Save Chart 1 as...'),
			os.path.expanduser(cfg.charts_dir), tr('Oroboros (*.xml)')))
		if path != '':
			if not path.endswith('.xml'):
				path = '%s%s' % (path, '.xml')
			cht.path = path
			cht.write()
			QMessageBox.information(self, tr('Save Chart 1 as...'),
				unicode(
					tr('Successfully saved chart \xab %(chart)s \xbb\nwith path %(path)s')) % {
						'path': cht._name, 'path': cht._path})
	
	def saveChart2AsEvent(self):
		idx = self.dock.tabs.currentIndex()
		cht = app.desktop.charts[idx][1]
		tr = self.tr
		path = str(QFileDialog.getSaveFileName(self,
			tr('Save Chart 2 As...'),
			os.path.expanduser(cfg.charts_dir), tr('Oroboros (*.xml)')))
		if path != '':
			if not path.endswith('.xml'):
				path = '%s%s' % (path, '.xml')
			cht.path = path
			cht.write()
			QMessageBox.information(self, tr('Save Chart 2 As...'),
				unicode(
					tr('Successfully saved chart \xab %(chart)s \xbb\nwith path %(path)s')) % {
						'path': cht._name, 'path': cht._path})
	
	def closeChart1Event(self):
		idx = self.dock.tabs.currentIndex()
		app.removeChart(idx, 0)
	
	def closeChart2Event(self):
		idx = self.dock.tabs.currentIndex()
		app.removeChart(idx, 1)
	
	def switchChartsEvent(self):
		idx = self.central.currentIndex()
		app.desktop.charts[idx].switch()
		self.resetActions()
		self.resetTabs(idx)
	
	def transitModeEvent(self):
		idx = self.central.currentIndex()
		if len(app.desktop.charts[idx]) == 1:
			ok = ChartInfoDialog(idx, 1).exec_()
			if not ok:
				return
		else:
			app.desktop.charts[idx].synastry_mode()
		self.resetTabs(idx)
	
	def progressionModeEvent(self):
		idx = self.central.currentIndex()
		if len(app.desktop.charts[idx]) == 1:
			ok = ChartInfoDialog(idx, 1).exec_()
			if not ok:
				return
		app.desktop.charts[idx].progression_of(0)
		self.resetTabs(idx)
	
	def directionModeEvent(self):
		return
		# TODO: directions
		if len(app.desktop.charts) == 1:
			ok = ChartInfoDialog(idx, 1).exec_()
			if not ok:
				return
		app.desktop.charts[idx].direction_of(0)
		self.resetTabs(idx)
	
	def multiplyPosEvent(self):
		idx = self.central.currentIndex()
		ok, value, mode, unit, dt = HarmonicsDialog(self).exec_()
		if ok != QDialog.Accepted:
			return
		# get non-hidden chart
		try:
			if app.desktop.charts[idx][1]._hidden:
				cht = 0
			else:
				cht = 1
		except IndexError:
			cht = 0
		if not mode: # absolute
			app.desktop.charts[idx].multiply_pos(value, cht)
		else: # relative (profection)
			app.desktop.charts[idx].profection('mul', value, unit, dt, cht)
		self.resetTabs(idx)
	
	def addPosEvent(self):
		idx = self.central.currentIndex()
		ok, value, mode, unit, dt = ProfectionDialog(self).exec_()
		if ok != QDialog.Accepted:
			return
		# get non-hidden chart
		try:
			if app.desktop.charts[idx][1]._hidden:
				cht = 0
			else:
				cht = 1
		except IndexError:
			cht = 0
		if not mode: # absolute
			app.desktop.charts[idx].add_pos(value, cht)
		else: # relative (profection)
			app.desktop.charts[idx].profection('add', value, unit, dt, cht)
		self.resetTabs(idx)
	
	def compositeEvent(self):
		pass
	
	def midSpaceTimeEvent(self):
		pass
	
	# ### configuration events ###
	
	def editSettingsEvent(self):
		CfgDialog(self).exec_()
	
	def manageFiltersEvent(self):
		FiltersManagerDialog(self).exec_()
	
	def managePlanetsFiltersEvent(self):
		PlanetsFiltersManagerDialog(self).exec_()
	
	def manageAspectsFiltersEvent(self):
		AspectsFiltersManagerDialog(self).exec_()
	
	def manageOrbsFiltersEvent(self):
		OrbsFiltersManagerDialog(self).exec_()
	
	def manageAspectsRestrictionsEvent(self):
		AspectsRestrictionsManagerDialog(self).exec_()
	
	def manageOrbsRestrictionsEvent(self):
		OrbsRestrictionsManagerDialog(self).exec_()
	
	def manageMidPointsFiltersEvent(self):
		MidPointsFiltersManagerDialog(self).exec_()






def main():
	# pull from hg repo on startup
	if cfg.use_hg:
		try:
			print('oroboros: pulling changes from distant repo...')
			hgrepo.pull()
		except:
			print('oroboros: unable to pull from hg repo.')
	# start
	qtApp = QApplication(sys.argv)
	main = MainWindow()
	app.mainwin = main # set mainwin
	translations.load(cfg.language, qtApp)
	main.show()
	qtApp.exec_()
	# push to hg repo on shutdown
	if cfg.use_hg:
		try:
			print('oroboros: commiting changes in local repo...')
			hgrepo.commit()
		except:
			print('oroboros: unable to commit.')
		try:
			print('oroboros: pushing changes to distant repo...')
			hgrepo.push()
		except:
			print('oroboros: unable to push to hg repo.')
	sys.exit()


if __name__ == '__main__':
	main()

# End.
