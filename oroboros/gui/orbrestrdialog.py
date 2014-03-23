#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
New/edit orbs restrictions.

"""

import sys
import os.path

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from oroboros.core import cfg
from oroboros.core import db
from oroboros.core.orbsrestrictions import OrbsRestrictions

from oroboros.gui import app
from oroboros.gui import names
from oroboros.gui.orbmodifierwidget import OrbModifierSpinBox


__all__ = ['OrbsRestrictionsDialog']


_baseDir = os.path.dirname(os.path.abspath(__file__))



class OrbsRestrictionsDialog(QDialog):
	
	def __init__(self, parent=None, filt=None):
		QDialog.__init__(self, parent)
		self._parent = parent
		tr = self.tr
		if isinstance(filt, OrbsRestrictions):
			self._filt = filt
			title = unicode(tr('Edit Orbs Restrictions \xab %(filter)s \xbb')) % {
				'filter': filt._name}
		else:
			self._filt = OrbsRestrictions(cfg.dft_filter._orbrestr._idx_)
			self._filt._idx_ = None # copy dft filter and set idx to None
			title = tr('New Orbs Restrictions')
		self.setWindowTitle(title)
		# size
		self.setMinimumWidth(500)
		self.setMinimumHeight(450)
		self.setSizeGripEnabled(True)
		# layout
		grid = QGridLayout(self)
		self.setLayout(grid)
		# filter name
		grid.addWidget(QLabel(tr('Filter name')), 0, 0)
		self.nameEdit = QLineEdit(self)
		grid.addWidget(self.nameEdit, 0, 1)
		# tab widget
		tabs = QTabWidget(self)
		grid.addWidget(tabs, 1, 0, 1, 2)
		self._sb = dict() ## holds the spinboxes
		
		# ### main planets ###
		mainWidget = QWidget()
		tabs.addTab(mainWidget, tr('Main', 'Main planets'))
		mainGrid = QGridLayout()
		mainWidget.setLayout(mainGrid)
		# sun
		mainGrid.addWidget(QLabel(names.planets['Sun']), 0, 0)
		self._sb['Sun'] = OrbModifierSpinBox(self)
		mainGrid.addWidget(self._sb['Sun'], 0, 1)
		# moon
		mainGrid.addWidget(QLabel(names.planets['Moon']), 0, 2)
		self._sb['Moon'] = OrbModifierSpinBox(self)
		mainGrid.addWidget(self._sb['Moon'], 0, 3)
		# mercury
		mainGrid.addWidget(QLabel(names.planets['Mercury']), 0, 4)
		self._sb['Mercury'] = OrbModifierSpinBox(self)
		mainGrid.addWidget(self._sb['Mercury'], 0, 5)
		# venus
		mainGrid.addWidget(QLabel(names.planets['Venus']), 0, 6)
		self._sb['Venus'] = OrbModifierSpinBox(self)
		mainGrid.addWidget(self._sb['Venus'], 0, 7)
		# mars
		mainGrid.addWidget(QLabel(names.planets['Mars']), 1, 0)
		self._sb['Mars'] = OrbModifierSpinBox(self)
		mainGrid.addWidget(self._sb['Mars'], 1, 1)
		# jupiter
		mainGrid.addWidget(QLabel(names.planets['Jupiter']), 1, 2)
		self._sb['Jupiter'] = OrbModifierSpinBox(self)
		mainGrid.addWidget(self._sb['Jupiter'], 1, 3)
		# saturn
		mainGrid.addWidget(QLabel(names.planets['Saturn']), 1, 4)
		self._sb['Saturn'] = OrbModifierSpinBox(self)
		mainGrid.addWidget(self._sb['Saturn'], 1, 5)
		# uranus
		mainGrid.addWidget(QLabel(names.planets['Uranus']), 1, 6)
		self._sb['Uranus'] = OrbModifierSpinBox(self)
		mainGrid.addWidget(self._sb['Uranus'], 1, 7)
		# neptune
		mainGrid.addWidget(QLabel(names.planets['Neptune']), 2, 0)
		self._sb['Neptune'] = OrbModifierSpinBox(self)
		mainGrid.addWidget(self._sb['Neptune'], 2, 1)
		# pluto
		mainGrid.addWidget(QLabel(names.planets['Pluto']), 2, 2)
		self._sb['Pluto'] = OrbModifierSpinBox(self)
		mainGrid.addWidget(self._sb['Pluto'], 2, 3)
		# earth
		mainGrid.addWidget(QLabel(names.planets['Earth']), 2, 4)
		self._sb['Earth'] = OrbModifierSpinBox(self)
		mainGrid.addWidget(self._sb['Earth'], 2, 5)
		# chiron
		mainGrid.addWidget(QLabel(names.planets['Chiron']), 2, 6)
		self._sb['Chiron'] = OrbModifierSpinBox(self)
		mainGrid.addWidget(self._sb['Chiron'], 2, 7)
		# pholus
		mainGrid.addWidget(QLabel(names.planets['Pholus']), 3, 0)
		self._sb['Pholus'] = OrbModifierSpinBox(self)
		mainGrid.addWidget(self._sb['Pholus'], 3, 1)
		# ceres
		mainGrid.addWidget(QLabel(names.planets['Ceres']), 3, 2)
		self._sb['Ceres'] = OrbModifierSpinBox(self)
		mainGrid.addWidget(self._sb['Ceres'], 3, 3)
		# pallas
		mainGrid.addWidget(QLabel(names.planets['Pallas']), 3, 4)
		self._sb['Pallas'] = OrbModifierSpinBox(self)
		mainGrid.addWidget(self._sb['Pallas'], 3, 5)
		# juno
		mainGrid.addWidget(QLabel(names.planets['Juno']), 3, 6)
		self._sb['Juno'] = OrbModifierSpinBox(self)
		mainGrid.addWidget(self._sb['Juno'], 3, 7)
		# vesta
		mainGrid.addWidget(QLabel(names.planets['Vesta']), 4, 0)
		self._sb['Vesta'] = OrbModifierSpinBox(self)
		mainGrid.addWidget(self._sb['Vesta'], 4, 1)
		# rahu (mean)
		mainGrid.addWidget(QLabel(names.planets['Rahu (mean)']), 4, 2)
		self._sb['Rahu (mean)'] = OrbModifierSpinBox(self)
		mainGrid.addWidget(self._sb['Rahu (mean)'], 4, 3)
		# rahu (true)
		mainGrid.addWidget(QLabel(names.planets['Rahu (true)']), 4, 4)
		self._sb['Rahu (true)'] = OrbModifierSpinBox(self)
		mainGrid.addWidget(self._sb['Rahu (true)'], 4, 5)
		# ketu (mean)
		mainGrid.addWidget(QLabel(names.planets['Ketu (mean)']), 4, 6)
		self._sb['Ketu (mean)'] = OrbModifierSpinBox(self)
		mainGrid.addWidget(self._sb['Ketu (mean)'], 4, 7)
		# ketu (true)
		mainGrid.addWidget(QLabel(names.planets['Ketu (true)']), 5, 0)
		self._sb['Ketu (true)'] = OrbModifierSpinBox(self)
		mainGrid.addWidget(self._sb['Ketu (true)'], 5, 1)
		# lilith (mean)
		mainGrid.addWidget(QLabel(names.planets['Lilith (mean)']), 5, 2)
		self._sb['Lilith (mean)'] = OrbModifierSpinBox(self)
		mainGrid.addWidget(self._sb['Lilith (mean)'], 5, 3)
		# lilith (true)
		mainGrid.addWidget(QLabel(names.planets['Lilith (true)']), 5, 4)
		self._sb['Lilith (true)'] = OrbModifierSpinBox(self)
		mainGrid.addWidget(self._sb['Lilith (true)'], 5, 5)
		# priapus (mean)
		mainGrid.addWidget(QLabel(names.planets['Priapus (mean)']), 5, 6)
		self._sb['Priapus (mean)'] = OrbModifierSpinBox(self)
		mainGrid.addWidget(self._sb['Priapus (mean)'], 5, 7)
		# priapus (true)
		mainGrid.addWidget(QLabel(names.planets['Priapus (true)']), 6, 0)
		self._sb['Priapus (true)'] = OrbModifierSpinBox(self)
		mainGrid.addWidget(self._sb['Priapus (true)'], 6, 1)
		
		# ### uranians ###
		uranianWidget = QWidget()
		tabs.addTab(uranianWidget, tr('Uranians'))
		uranianGrid = QGridLayout()
		uranianWidget.setLayout(uranianGrid)
		# cupido
		uranianGrid.addWidget(QLabel(names.planets['Cupido']), 0, 0)
		self._sb['Cupido'] = OrbModifierSpinBox(self)
		uranianGrid.addWidget(self._sb['Cupido'], 0, 1)
		# hades
		uranianGrid.addWidget(QLabel(names.planets['Hades']), 0, 2)
		self._sb['Hades'] = OrbModifierSpinBox(self)
		uranianGrid.addWidget(self._sb['Hades'], 0, 3)
		# zeus
		uranianGrid.addWidget(QLabel(names.planets['Zeus']), 0, 4)
		self._sb['Zeus'] = OrbModifierSpinBox(self)
		uranianGrid.addWidget(self._sb['Zeus'], 0, 5)
		# kronos
		uranianGrid.addWidget(QLabel(names.planets['Kronos']), 0, 6)
		self._sb['Kronos'] = OrbModifierSpinBox(self)
		uranianGrid.addWidget(self._sb['Kronos'], 0, 7)
		# apollon
		uranianGrid.addWidget(QLabel(names.planets['Apollon']), 1, 0)
		self._sb['Apollon'] = OrbModifierSpinBox(self)
		uranianGrid.addWidget(self._sb['Apollon'], 1, 1)
		# admetos
		uranianGrid.addWidget(QLabel(names.planets['Admetos']), 1, 2)
		self._sb['Admetos'] = OrbModifierSpinBox(self)
		uranianGrid.addWidget(self._sb['Admetos'], 1, 3)
		# vulkanus
		uranianGrid.addWidget(QLabel(names.planets['Vulkanus']), 1, 4)
		self._sb['Vulkanus'] = OrbModifierSpinBox(self)
		uranianGrid.addWidget(self._sb['Vulkanus'], 1, 5)
		# poseidon
		uranianGrid.addWidget(QLabel(names.planets['Poseidon']), 1, 6)
		self._sb['Poseidon'] = OrbModifierSpinBox(self)
		uranianGrid.addWidget(self._sb['Poseidon'], 1, 7)
		
		# ### others fictitious ###
		othersWidget = QWidget()
		tabs.addTab(othersWidget, tr('Others'))
		othersGrid = QGridLayout()
		othersWidget.setLayout(othersGrid)
		# isis
		othersGrid.addWidget(QLabel(names.planets['Isis']), 0, 0)
		self._sb['Isis'] = OrbModifierSpinBox(self)
		othersGrid.addWidget(self._sb['Isis'], 0, 1)
		# nibiru
		othersGrid.addWidget(QLabel(names.planets['Nibiru']), 0, 2)
		self._sb['Nibiru'] = OrbModifierSpinBox(self)
		othersGrid.addWidget(self._sb['Nibiru'], 0, 3)
		# harrington
		othersGrid.addWidget(QLabel(names.planets['Harrington']), 0, 4)
		self._sb['Harrington'] = OrbModifierSpinBox(self)
		othersGrid.addWidget(self._sb['Harrington'], 0, 5)
		# neptune (leverrier)
		othersGrid.addWidget(QLabel(names.planets['Neptune (Leverrier)']), 0, 6)
		self._sb['Neptune (Leverrier)'] = OrbModifierSpinBox(self)
		othersGrid.addWidget(self._sb['Neptune (Leverrier)'], 0, 7)
		# neptune (adams)
		othersGrid.addWidget(QLabel(names.planets['Neptune (Adams)']), 1, 0)
		self._sb['Neptune (Adams)'] = OrbModifierSpinBox(self)
		othersGrid.addWidget(self._sb['Neptune (Adams)'], 1, 1)
		# pluto (lowell)
		othersGrid.addWidget(QLabel(names.planets['Pluto (Lowell)']), 1, 2)
		self._sb['Pluto (Lowell)'] = OrbModifierSpinBox(self)
		othersGrid.addWidget(self._sb['Pluto (Lowell)'], 1, 3)
		# pluto (pickering)
		othersGrid.addWidget(QLabel(names.planets['Pluto (Pickering)']), 1, 4)
		self._sb['Pluto (Pickering)'] = OrbModifierSpinBox(self)
		othersGrid.addWidget(self._sb['Pluto (Pickering)'], 1, 5)
		# vulcan
		othersGrid.addWidget(QLabel(names.planets['Vulcan']), 1, 6)
		self._sb['Vulcan'] = OrbModifierSpinBox(self)
		othersGrid.addWidget(self._sb['Vulcan'], 1, 7)
		# white moon
		othersGrid.addWidget(QLabel(names.planets['White Moon']), 2, 0)
		self._sb['White Moon'] = OrbModifierSpinBox(self)
		othersGrid.addWidget(self._sb['White Moon'], 2, 1)
		# proserpina
		othersGrid.addWidget(QLabel(names.planets['Proserpina']), 2, 2)
		self._sb['Proserpina'] = OrbModifierSpinBox(self)
		othersGrid.addWidget(self._sb['Proserpina'], 2, 3)
		# waldemath
		othersGrid.addWidget(QLabel(names.planets['Waldemath']), 2, 4)
		self._sb['Waldemath'] = OrbModifierSpinBox(self)
		othersGrid.addWidget(self._sb['Waldemath'], 2, 5)
		
		# ### cusps ###
		cuspsWidget = QWidget()
		tabs.addTab(cuspsWidget, tr('Cusps'))
		cuspsGrid = QGridLayout()
		cuspsWidget.setLayout(cuspsGrid)
		# house cusps
		x = (0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2)
		y = (0, 2, 4, 6, 0, 2, 4, 6, 0, 2, 4, 6)
		for i in range(12):
			cuspsGrid.addWidget(QLabel(
				names.houses['Cusp %.2d' % (i+1,)]), x[i], y[i])
			self._sb['Cusp %.2d' % (i+1,)] = OrbModifierSpinBox(self)
			cuspsGrid.addWidget(self._sb['Cusp %.2d' % (i+1,)], x[i], y[i]+1)
		# asc
		cuspsGrid.addWidget(QLabel(names.planets['Asc']), 3, 0)
		self._sb['Asc'] = OrbModifierSpinBox(self)
		cuspsGrid.addWidget(self._sb['Asc'], 3, 1)
		# mc
		cuspsGrid.addWidget(QLabel(names.planets['Mc']), 3, 2)
		self._sb['Mc'] = OrbModifierSpinBox(self)
		cuspsGrid.addWidget(self._sb['Mc'], 3, 3)
		# dsc
		cuspsGrid.addWidget(QLabel(names.planets['Dsc']), 3, 4)
		self._sb['Dsc'] = OrbModifierSpinBox(self)
		cuspsGrid.addWidget(self._sb['Dsc'], 3, 5)
		# ic
		cuspsGrid.addWidget(QLabel(names.planets['Ic']), 3, 6)
		self._sb['Ic'] = OrbModifierSpinBox(self)
		cuspsGrid.addWidget(self._sb['Ic'], 3, 7)
		# armc
		cuspsGrid.addWidget(QLabel(names.planets['Armc']), 4, 0)
		self._sb['Armc'] = OrbModifierSpinBox(self)
		cuspsGrid.addWidget(self._sb['Armc'], 4, 1)
		# vertex
		cuspsGrid.addWidget(QLabel(names.planets['Vertex']), 4, 2)
		self._sb['Vertex'] = OrbModifierSpinBox(self)
		cuspsGrid.addWidget(self._sb['Vertex'], 4, 3)
		# equatorial asc
		cuspsGrid.addWidget(QLabel(names.planets['Equatorial Ascendant']), 4, 4)
		self._sb['Equatorial Ascendant'] = OrbModifierSpinBox(self)
		cuspsGrid.addWidget(self._sb['Equatorial Ascendant'], 4, 5)
		# co-ascendant (koch)
		cuspsGrid.addWidget(QLabel(names.planets['Co-ascendant (Koch)']), 4, 6)
		self._sb['Co-ascendant (Koch)'] = OrbModifierSpinBox(self)
		cuspsGrid.addWidget(self._sb['Co-ascendant (Koch)'], 4, 7)
		# co-ascendant (munkasey)
		cuspsGrid.addWidget(QLabel(names.planets['Co-ascendant (Munkasey)']), 5, 0)
		self._sb['Co-ascendant (Munkasey)'] = OrbModifierSpinBox(self)
		cuspsGrid.addWidget(self._sb['Co-ascendant (Munkasey)'], 5, 1)
		# polar ascendant
		cuspsGrid.addWidget(QLabel(names.planets['Polar Ascendant (Munkasey)']), 5, 2)
		self._sb['Polar Ascendant (Munkasey)'] = OrbModifierSpinBox(self)
		cuspsGrid.addWidget(self._sb['Polar Ascendant (Munkasey)'], 5, 3)
		
		# ### gauquelin ###
		gauquelinWidget = QWidget()
		tabs.addTab(gauquelinWidget, tr('Gauquelin'))
		gauquelinGrid = QGridLayout()
		gauquelinWidget.setLayout(gauquelinGrid)
		# sectors
		x = (0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8)
		y = (0,2,4,6,0,2,4,6,0,2,4,6,0,2,4,6,0,2,4,6,0,2,4,6,0,2,4,6,0,2,4,6,0,2,4,6)
		for i in range(36):
			gauquelinGrid.addWidget(QLabel(
				names.houses['Sector %.2d' % (i+1,)]), x[i], y[i])
			self._sb['Sector %.2d' % (i+1,)] = OrbModifierSpinBox(self)
			gauquelinGrid.addWidget(self._sb['Sector %.2d' % (i+1,)], x[i], y[i]+1)
		
		# ### parts ###
		partsWidget = QWidget()
		tabs.addTab(partsWidget, tr('Parts'))
		partsGrid = QGridLayout()
		partsWidget.setLayout(partsGrid)
		# part of fortune (rudhyar)
		partsGrid.addWidget(QLabel(
			names.planets['Part of Fortune (Rudhyar)']), 0, 0)
		self._sb['Part of Fortune (Rudhyar)'] = OrbModifierSpinBox(self)
		partsGrid.addWidget(self._sb['Part of Fortune (Rudhyar)'], 0, 1)
		
		# ### fixed stars ###
		# get all stars
		sql = 'select name from Planets where family = 2 order by name;'
		res = db.execute(sql).fetchall()
		# stars tab
		starsScroll = QScrollArea(self)
		starsScroll.setWidgetResizable(True)
		starsWidget = QWidget()
		starsScroll.setWidget(starsWidget)
		tabs.addTab(starsScroll, tr('Stars'))
		starsGrid = QGridLayout()
		starsWidget.setLayout(starsGrid)
		y = 0
		i = 0
		for star in res:
			s = str(star[0])
			starsGrid.addWidget(QLabel(s), y, i % 10)
			self._sb[s] = OrbModifierSpinBox(self)
			starsGrid.addWidget(self._sb[s], y, (i%10) + 1)
			if i % 10 == 8:
				y += 1
			i += 2
		
		# ### asteroids ###
		# get all asteroids
		sql = 'select name from Planets where family = 3 order by name;'
		res = db.execute(sql).fetchall()
		# asteroids tab
		asteroidsScroll = QScrollArea()
		asteroidsScroll.setWidgetResizable(True)
		asteroidsWidget = QWidget()
		asteroidsScroll.setWidget(asteroidsWidget)
		tabs.addTab(asteroidsScroll, tr('Asteroids'))
		asteroidsGrid = QGridLayout()
		asteroidsWidget.setLayout(asteroidsGrid)
		y = 0
		i = 0
		for ast in res:
			s = str(ast[0])
			asteroidsGrid.addWidget(QLabel(s), y, i % 10)
			self._sb[s] = OrbModifierSpinBox(self)
			asteroidsGrid.addWidget(self._sb[s], y, (i%10) + 1)
			if i % 10 == 8:
				y += 1
			i += 2
		
		# ### end planets ###
		
		# comment
		grid.addWidget(QLabel(tr('Comment')), 2, 0, Qt.AlignTop)
		self.commentEdit = QTextEdit('', self)
		grid.addWidget(self.commentEdit, 2, 1)
		# buttons
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
		grid.addLayout(buttonsLayout, 3, 0, 1, 2)
		# load entries
		self.reset()
		# resize
		self.resize(550, 300)
	
	def reset(self):
		"""Reset entries."""
		# name
		self.nameEdit.setText(self._filt._name)
		# comment
		self.commentEdit.setPlainText(self._filt._comment)
		# values
		for pl, val in self._filt.items():
				self._sb[pl].setValue(float(val.replace('%', '')))
	
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
		# comment
		cmt = unicode(self.commentEdit.toPlainText())
		# set values
		self._filt.set(name=name, comment=cmt)
		for pl, sb in self._sb.items():
			self._filt[pl] = '%s%%' % sb.value()
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
			app.orbsRestrictionsUpdatedEvent(self._filt._idx_)
		# done
		self.done(QDialog.Accepted)



def main():
	app = QApplication(sys.argv)
	main = OrbsRestrictionsDialog()
	main.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()

# End.
