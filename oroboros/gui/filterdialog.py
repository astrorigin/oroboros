#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
New/edit filters set and options.

"""

import sys
import os.path

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from oroboros.core import cfg
from oroboros.core.filters import Filter
from oroboros.core.planetsfilters import PlanetsFilter, all_planets_filters_names
from oroboros.core.aspectsfilters import AspectsFilter, all_aspects_filters_names
from oroboros.core.orbsfilters import OrbsFilter, all_orbs_filters_names
from oroboros.core.aspectsrestrictions import AspectsRestrictions, all_aspects_restrictions_names
from oroboros.core.orbsrestrictions import OrbsRestrictions, all_orbs_restrictions_names
from oroboros.core.midpfilters import MidPointsFilter, all_midpoints_filters_names

from oroboros.gui import app
from oroboros.gui import names
from oroboros.gui.plntfilterdialog import PlanetsFilterDialog
from oroboros.gui.aspfilterdialog import AspectsFilterDialog
from oroboros.gui.orbfilterdialog import OrbsFilterDialog
from oroboros.gui.asprestrdialog import AspectsRestrictionsDialog
from oroboros.gui.orbrestrdialog import OrbsRestrictionsDialog
from oroboros.gui.midpfilterdialog import MidPointsFilterDialog


__all__ = ['FilterDialog']


_baseDir = os.path.dirname(os.path.abspath(__file__))


## oroboros.ui.filterdialog.FilterDialog
class FilterDialog(QDialog):
	
	def __init__(self, parent=None, filt=None):
		QDialog.__init__(self, parent)
		self._parent = parent
		tr = self.tr
		if isinstance(filt, Filter):
			self._filt = filt
			title = unicode(tr('Edit Filter \xab %(filter)s \xbb')) % {
				'filter': filt._name}
		else:
			self._filt = Filter(cfg.dft_filter._idx_)
			self._filt._idx_ = None # copy dft filter and set idx to None
			title = tr('New Filter')
		self.setWindowTitle(title)
		# size
		self.setMinimumWidth(300)
		self.setMinimumHeight(380)
		self.setSizeGripEnabled(True)
		# layout
		layout = QVBoxLayout(self)
		self.setLayout(layout)
		# tabs
		tabs = QTabWidget(self)
		layout.addWidget(tabs)
		
		# ### general settings ###
		generalWidget = QWidget()
		tabs.addTab(generalWidget, tr('Main', 'Main settings'))
		# layout
		grid = QGridLayout()
		generalWidget.setLayout(grid)
		# filter name
		grid.addWidget(QLabel(tr('Filter name')), 0, 0)
		self.nameEdit = QLineEdit(self)
		grid.addWidget(self.nameEdit, 0, 1)
		# bg color
		grid.addWidget(QLabel(tr('Background')), 1, 0)
		self.bgcolorEdit = QComboBox(self)
		self.bgcolorEdit.setEditable(False)
		self.bgcolorEdit.addItems([tr('Black'), tr('White')])
		grid.addWidget(self.bgcolorEdit, 1, 1)
		# ephe type
		grid.addWidget(QLabel(tr('Ephemeris')), 2, 0)
		self.ephetypeEdit = QComboBox(self)
		self.ephetypeEdit.setEditable(False)
		self.ephetypeEdit.addItems([tr('Swiss'), tr('JPL'), tr('Moshier')])
		grid.addWidget(self.ephetypeEdit, 2, 1)
		# ephe path
		grid.addWidget(QLabel(tr('Ephem. path')), 3, 0)
		ephLayout = QHBoxLayout()
		self.ephepathEdit = QLineEdit(self)
		self.ephepathEdit.setReadOnly(True)
		ephLayout.addWidget(self.ephepathEdit)
		selectButton = QToolButton(self)
		selectButton.setIcon(QIcon(os.path.join(_baseDir,
			'icons', 'gtk-directory.png')))
		selectButton.setToolTip(tr('Select ephemeris path'))
		self.connect(selectButton, SIGNAL('clicked()'), self.ephePathSelect)
		ephLayout.addWidget(selectButton)
		grid.addLayout(ephLayout, 3, 1)
		# house system
		grid.addWidget(QLabel(tr('Domification')), 4, 0)
		self.hsysEdit = QComboBox(self)
		self.hsysEdit.setEditable(False)
		self.hsysEdit.addItems([y for x, y in names.houseSystems])
		grid.addWidget(self.hsysEdit, 4, 1)
		# sidereal mode
		grid.addWidget(QLabel(tr('Sidereal mode')), 5, 0)
		self.sidmodeEdit = QComboBox(self)
		self.sidmodeEdit.setEditable(False)
		self.sidmodeEdit.addItems([y for x, y in names.sidModes])
		grid.addWidget(self.sidmodeEdit, 5, 1)
		# sidereal t0
		grid.addWidget(QLabel(tr('Sidereal T0')), 6, 0)
		self.sidt0Edit = QDoubleSpinBox(self)
		self.sidt0Edit.setDecimals(6)
		self.sidt0Edit.setMaximum(9999999)
		self.sidt0Edit.setSuffix(tr(' JD', 'Julian day suffix'))
		self.sidt0Edit.setButtonSymbols(QAbstractSpinBox.PlusMinus)
		grid.addWidget(self.sidt0Edit, 6, 1)
		# sidereal ayanamsa at t0
		grid.addWidget(QLabel(tr('Ayanamsa T0')), 7, 0)
		self.sidayant0Edit = QDoubleSpinBox(self)
		self.sidayant0Edit.setDecimals(6)
		self.sidayant0Edit.setMaximum(360)
		self.sidayant0Edit.setSuffix(tr('\xb0', 'Degrees'))
		self.sidayant0Edit.setButtonSymbols(QAbstractSpinBox.PlusMinus)
		grid.addWidget(self.sidayant0Edit, 7, 1)
		# true positions
		grid.addWidget(QLabel(tr('Calc. positions')), 8, 0)
		self.trueposEdit = QComboBox(self)
		self.trueposEdit.setEditable(False)
		self.trueposEdit.addItems(
			[tr('Apparent', 'Positions'), tr('True', 'Positions')])
		grid.addWidget(self.trueposEdit, 8, 1)
		# xcentric
		grid.addWidget(QLabel(tr('Situation')), 9, 0)
		self.xcentricEdit = QComboBox(self)
		self.xcentricEdit.setEditable(False)
		self.xcentricEdit.addItems(
			[tr('Geocentric'), tr('Topocentric'), tr('Heliocentric'),
			tr('Barycentric')])
		grid.addWidget(self.xcentricEdit, 9, 1)
		# comment
		grid.addWidget(QLabel(tr('Comment')), 10, 0, Qt.AlignTop)
		self.commentEdit = QTextEdit('', self)
		grid.addWidget(self.commentEdit, 10, 1)
		
		# ### filters settings ###
		filtersWidget = QWidget()
		tabs.addTab(filtersWidget, tr('Filters'))
		# layout
		grid = QGridLayout()
		filtersWidget.setLayout(grid)
		# planets filter
		grid.addWidget(QLabel(tr('Planets filter')), 0, 0)
		pfLayout = QHBoxLayout()
		self.planetsEdit = QComboBox(self)
		self.planetsEdit.setEditable(False)
		pfLayout.addWidget(self.planetsEdit)
		pfButton = QToolButton(self)
		pfButton.setIcon(QIcon(os.path.join(_baseDir, 'icons',
			'gtk-execute.png')))
		pfButton.setToolTip(tr('Edit planets filter'))
		self.connect(pfButton, SIGNAL('clicked()'), self.editPlanetsFilter)
		pfLayout.addWidget(pfButton)
		grid.addLayout(pfLayout, 0, 1)
		# aspects filter
		grid.addWidget(QLabel(tr('Aspects filter')), 1, 0)
		afLayout = QHBoxLayout()
		self.aspectsEdit = QComboBox(self)
		self.aspectsEdit.setEditable(False)
		afLayout.addWidget(self.aspectsEdit)
		afButton = QToolButton(self)
		afButton.setIcon(QIcon(os.path.join(_baseDir, 'icons',
			'gtk-execute.png')))
		afButton.setToolTip(tr('Edit aspects filter'))
		self.connect(afButton, SIGNAL('clicked()'), self.editAspectsFilter)
		afLayout.addWidget(afButton)
		grid.addLayout(afLayout, 1, 1)
		# orbs filter
		grid.addWidget(QLabel(tr('Orbs filter')), 2, 0)
		ofLayout = QHBoxLayout()
		self.orbsEdit = QComboBox(self)
		self.orbsEdit.setEditable(False)
		ofLayout.addWidget(self.orbsEdit)
		ofButton = QToolButton(self)
		ofButton.setIcon(QIcon(os.path.join(_baseDir, 'icons',
			'gtk-execute.png')))
		ofButton.setToolTip(tr('Edit orbs filter'))
		self.connect(ofButton, SIGNAL('clicked()'), self.editOrbsFilter)
		ofLayout.addWidget(ofButton)
		grid.addLayout(ofLayout, 2, 1)
		# aspects restrictions
		grid.addWidget(QLabel(tr('Aspects restrictions')), 3, 0)
		arLayout = QHBoxLayout()
		self.asprestrEdit = QComboBox(self)
		self.asprestrEdit.setEditable(False)
		arLayout.addWidget(self.asprestrEdit)
		arButton = QToolButton(self)
		arButton.setIcon(QIcon(os.path.join(_baseDir, 'icons',
			'gtk-execute.png')))
		arButton.setToolTip(tr('Edit aspects restrictions'))
		self.connect(arButton, SIGNAL('clicked()'), self.editAspectsRestrictions)
		arLayout.addWidget(arButton)
		grid.addLayout(arLayout, 3, 1)
		# orbs restrictions
		grid.addWidget(QLabel(tr('Orbs modifiers')), 4, 0)
		orLayout = QHBoxLayout()
		self.orbrestrEdit = QComboBox(self)
		self.orbrestrEdit.setEditable(False)
		orLayout.addWidget(self.orbrestrEdit)
		orButton = QToolButton(self)
		orButton.setIcon(QIcon(os.path.join(_baseDir, 'icons',
			'gtk-execute.png')))
		orButton.setToolTip(tr('Edit orbs restrictions'))
		self.connect(orButton, SIGNAL('clicked()'), self.editOrbsRestrictions)
		orLayout.addWidget(orButton)
		grid.addLayout(orLayout, 4, 1)
		# midpoints settings
		## calc midpoints
		self.calc_midpEdit = QCheckBox(tr('Calc. midpoints'), self)
		self.connect(self.calc_midpEdit, SIGNAL('stateChanged(int)'),
			self.calc_midpEditChanged)
		grid.addWidget(self.calc_midpEdit, 5, 0)
		## draw midpoints
		self.draw_midpEdit = QCheckBox(tr('Draw midpoints aspects'), self)
		self.connect(self.draw_midpEdit, SIGNAL('stateChanged(int)'),
			self.draw_midpEditChanged)
		grid.addWidget(self.draw_midpEdit, 5, 1)
		## filters
		grid.addWidget(QLabel(tr('MidPoints filter')), 6, 0)
		mpLayout = QHBoxLayout()
		self.midpointsEdit = QComboBox(self)
		self.midpointsEdit.setEditable(False)
		mpLayout.addWidget(self.midpointsEdit)
		mpButton = QToolButton(self)
		mpButton.setIcon(QIcon(os.path.join(_baseDir, 'icons',
			'gtk-execute.png')))
		mpButton.setToolTip(tr('Edit MidPoints filter'))
		self.connect(mpButton, SIGNAL('clicked()'), self.editMidPointsFilter)
		mpLayout.addWidget(mpButton)
		grid.addLayout(mpLayout, 6, 1)
		
		# ### buttons ###
		buttonsLayout = QHBoxLayout()
		resetButton = QPushButton(tr('Reset'), self)
		self.connect(resetButton, SIGNAL('clicked()'), self.reset)
		buttonsLayout.addWidget(resetButton)
		cancelButton = QPushButton(tr('Cancel'), self)
		self.connect(cancelButton, SIGNAL('clicked()'), self.reject)
		buttonsLayout.addWidget(cancelButton)
		okButton = QPushButton(tr('Ok'), self)
		okButton.setDefault(True)
		self.connect(okButton, SIGNAL('clicked()'), self.accept)
		buttonsLayout.addWidget(okButton)
		layout.addLayout(buttonsLayout)
		
		# load entries
		self.reset()
	
	def ephePathSelect(self):
		"""Select directory (for swisseph) or a file (for jpl)."""
		path = ''
		if self.ephetypeEdit.currentIndex() == 0: # swisseph
			path = unicode(QFileDialog.getExistingDirectory(self,
				self.tr('Set Swisseph directory'),
				os.path.expanduser('~')))
		elif self.ephetypeEdit.currentIndex() == 1: # jpl
			path = unicode(QFileDialog.getOpenFileName(self,
				self.tr('Set JPL file'),
				os.path.expanduser('~')))
		else: # moshier
			QMessageBox.information(self, self.tr('Moshier ephemeris'),
				self.tr('No ephemeris path needed for Moshier ephemeris.'))
		if path != '':
				self.ephepathEdit.setText(path)
	
	def calc_midpEditChanged(self, val):
		if not self.calc_midpEdit.isChecked():
			self.draw_midpEdit.setChecked(False)
	
	def draw_midpEditChanged(self, val):
		if self.draw_midpEdit.isChecked():
			self.calc_midpEdit.setChecked(True)
	
	# ### edit filters ###
	
	def editPlanetsFilter(self):
		"""Open planets filter edit dialog."""
		pf = PlanetsFilter(
			all_planets_filters_names()[self.planetsEdit.currentIndex()])
		edit = PlanetsFilterDialog(self, pf)
		ok = edit.exec_()
		if ok: ## reset our filters
			if pf == self._filt._planets:
				self._filt._planets.reset()
			self.resetPlanetsFilters()
	
	def editAspectsFilter(self):
		"""Open aspects filter edit dialog."""
		af = AspectsFilter(
			all_aspects_filters_names()[self.aspectsEdit.currentIndex()])
		edit = AspectsFilterDialog(self, af)
		ok = edit.exec_()
		if ok: ## reset our filters
			if af == self._filt._aspects:
				self._filt._aspects.reset()
			self.resetAspectsFilters()
	
	def editOrbsFilter(self):
		of = OrbsFilter(
			all_orbs_filters_names()[self.orbsEdit.currentIndex()])
		edit = OrbsFilterDialog(self, of)
		ok = edit.exec_()
		if ok: ## reset our filters
			if of == self._filt._orbs:
				self._filt._orbs.reset()
			self.resetOrbsFilters()
	
	def editAspectsRestrictions(self):
		ar = AspectsRestrictions(
			all_aspects_restrictions_names()[self.asprestrEdit.currentIndex()])
		edit = AspectsRestrictionsDialog(self, ar)
		ok = edit.exec_()
		if ok: ## reset our filters
			if ar == self._filt._asprestr:
				self._filt._asprestr.reset()
			self.resetAspectsRestrictions()
	
	def editOrbsRestrictions(self):
		orb = OrbsRestrictions(
			all_orbs_restrictions_names()[self.orbrestrEdit.currentIndex()])
		edit = OrbsRestrictionsDialog(self, orb)
		ok = edit.exec_()
		if ok: ## reset our filters
			if orb == self._filt._orbrestr:
				self._filt._orbrestr.reset()
			self.resetOrbsRestrictions()
	
	def editMidPointsFilter(self):
		mp = MidPointsFilter(
			all_midpoints_filters_names()[self.midpointsEdit.currentIndex()])
		edit = MidPointsFilterDialog(self, mp)
		ok = edit.exec_()
		if ok: ## reset our filters
			if mp == self._filt._midpoints:
				self._filt._midpoints.reset()
			self.resetMidPointsFilters()
	
	# ### reset filters boxes ###
	
	def resetPlanetsFilters(self):
		"""Reset planets filter box."""
		self.planetsEdit.clear()
		all = all_planets_filters_names()
		self.planetsEdit.addItems(all)
		i = all.index(self._filt._planets._name)
		self.planetsEdit.setCurrentIndex(i)
	
	def resetAspectsFilters(self):
		"""Reset aspects filters box."""
		self.aspectsEdit.clear()
		all = all_aspects_filters_names()
		self.aspectsEdit.addItems(all)
		i = all.index(self._filt._aspects._name)
		self.aspectsEdit.setCurrentIndex(i)
	
	def resetOrbsFilters(self):
		"""Reset orbs filters box."""
		self.orbsEdit.clear()
		all = all_orbs_filters_names()
		self.orbsEdit.addItems(all)
		i = all.index(self._filt._orbs._name)
		self.orbsEdit.setCurrentIndex(i)
	
	def resetAspectsRestrictions(self):
		"""Reset aspects restrictions box."""
		self.asprestrEdit.clear()
		all = all_aspects_restrictions_names()
		self.asprestrEdit.addItems(all)
		i = all.index(self._filt._asprestr._name)
	
	def resetOrbsRestrictions(self):
		"""Reset orbs restrictions box."""
		self.orbrestrEdit.clear()
		all = all_orbs_restrictions_names()
		self.orbrestrEdit.addItems(all)
		i = all.index(self._filt._orbrestr._name)
		self.orbrestrEdit.setCurrentIndex(i)
	
	def resetMidPointsFilters(self):
		"""Reset midpoints filters box."""
		self.midpointsEdit.clear()
		all = all_midpoints_filters_names()
		self.midpointsEdit.addItems(all)
		i = all.index(self._filt._midpoints._name)
		self.midpointsEdit.setCurrentIndex(i)
	
	def reset(self):
		"""Reset entries."""
		filt = self._filt
		# name
		self.nameEdit.setText(filt._name)
		# bg color
		self.bgcolorEdit.setCurrentIndex(0 if filt._bg_color == 'black' else 1)
		# ephe type
		t = filt._ephe_type
		if t == 'swiss':
			t = 0
		elif t == 'jpl':
			t = 1
		else:
			t = 2
		self.ephetypeEdit.setCurrentIndex(t)
		# ephe path
		self.ephepathEdit.setText(os.path.expanduser(filt._ephe_path))
		# domification
		hsys = filt._hsys
		for i, a in enumerate(names.houseSystems):
			if a[0] == hsys:
				self.hsysEdit.setCurrentIndex(i)
				break
		# sid mode
		sidm = filt._sid_mode
		for i, a in enumerate(names.sidModes):
			if a[0] == sidm:
				self.sidmodeEdit.setCurrentIndex(i)
				break
		# sid t0
		self.sidt0Edit.setValue(filt._sid_t0)
		# sid ayan t0
		self.sidayant0Edit.setValue(filt._sid_ayan_t0)
		# true pos
		self.trueposEdit.setCurrentIndex(0 if filt._true_pos == False else 1)
		# xcentric
		xcentric = filt._xcentric
		if xcentric == 'geo':
			i = 0
		elif xcentric == 'topo':
			i = 1
		elif xcentric == 'helio':
			i = 2
		else: # bary
			i = 3
		self.xcentricEdit.setCurrentIndex(i)
		# planets
		self.resetPlanetsFilters()
		# aspects
		self.resetAspectsFilters()
		# orbs
		self.resetOrbsFilters()
		# aspects restrictions
		self.resetAspectsRestrictions()
		# orbs modifiers
		self.resetOrbsRestrictions()
		# calc midp
		self.calc_midpEdit.setChecked(self._filt._calc_midp)
		# draw midp
		self.draw_midpEdit.setChecked(self._filt._draw_midp)
		# midpoints filter
		self.resetMidPointsFilters()
		# comment
		self.commentEdit.setPlainText(filt._comment)
	
	def accept(self):
		"""Set filter new values and save."""
		tr = self.tr
		# name
		name = unicode(self.nameEdit.text())
		if name == '':
			QMessageBox.critical(self, tr('Missing Name'),
				tr('Please set filter name.'))
			self.nameEdit.setFocus()
			return
		# bg color
		bg = self.bgcolorEdit.currentIndex()
		if bg == 0:
			bg = 'black'
		else:
			bg = 'white'
		# ephe type
		ephetype = self.ephetypeEdit.currentIndex()
		if ephetype == 0:
			ephetype = 'swiss'
		elif ephetype == 1:
			ephetype = 'jpl'
		else:
			ephetype = 'moshier'
		# ephe path
		ephepath = unicode(self.ephepathEdit.text())
		# hsys
		hsys = names.houseSystems[self.hsysEdit.currentIndex()][0]
		# sidereal mode
		sidm = names.sidModes[self.sidmodeEdit.currentIndex()][0]
		# sidereal t0
		sidt0 = self.sidt0Edit.value()
		# sidereal ayanamsa t0
		sidayant0 = self.sidayant0Edit.value()
		# true pos
		truepos = False if self.trueposEdit.currentIndex() == 0 else True
		# xcentric
		xcentric = self.xcentricEdit.currentIndex()
		if xcentric == 0:
			xcentric = 'geo'
		elif xcentric == 1:
			xcentric = 'topo'
		elif xcentric == 2:
			xcentric = 'helio'
		else:
			xcentric = 'bary'
		# planets filter
		planets = all_planets_filters_names()[self.planetsEdit.currentIndex()]
		# aspects filter
		aspects = all_aspects_filters_names()[self.aspectsEdit.currentIndex()]
		# orbs filter
		orbs = all_orbs_filters_names()[self.orbsEdit.currentIndex()]
		# aspects restrictions
		asprestr = all_aspects_restrictions_names()[self.asprestrEdit.currentIndex()]
		# orbs restrictions
		orbrestr = all_orbs_restrictions_names()[self.orbrestrEdit.currentIndex()]
		# midpoints settings
		calc_midp = self.calc_midpEdit.isChecked()
		draw_midp = self.draw_midpEdit.isChecked()
		# midpoints filter
		midpoints = all_midpoints_filters_names()[self.midpointsEdit.currentIndex()]
		# comment
		cmt = unicode(self.commentEdit.toPlainText())
		# ### set filter ###
		self._filt.set(name=name, bg_color=bg, ephe_type=ephetype,
			ephe_path=ephepath, hsys=hsys, sid_mode=sidm, sid_t0=sidt0,
			sid_ayan_t0=sidayant0, true_pos=truepos, xcentric=xcentric,
			calc_midp=calc_midp, draw_midp=draw_midp,
			planets=planets, aspects=aspects, orbs=orbs, asprestr=asprestr,
			orbrestr=orbrestr, midpoints=midpoints, comment=cmt)
		# save
		try:
			self._filt.save()
		except ValueError: # duplicate filter
			QMessageBox.critical(self, tr('Error'),
				unicode(tr('Duplicate filter name \xab %(filter)s \xbb.')) % {
					'filter': self._filt._name})
			self.nameEdit.setFocus()
			return
		# reload cfg in case filter is default,
		# and opened charts if using this filter
		if __name__ != '__main__':
			app.filterUpdatedEvent(self._filt._idx_)
		# done
		self.done(QDialog.Accepted)



## oroboros.ui.filterdialog.main
def main():
	app = QApplication(sys.argv)
	main = FilterDialog()
	main.show()
	sys.exit(app.exec_())


## __main__
if __name__ == '__main__':
	main()

# End.
