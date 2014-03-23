#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Mid-points filters manager.

"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from oroboros.core.midpfilters import MidPointsFilter, all_midpoints_filters_names
from oroboros.gui.midpfilterdialog import MidPointsFilterDialog


__all__ = ['MidPointsFiltersManagerDialog']



class MidPointsFiltersManagerDialog(QDialog):
	
	def __init__(self, parent=None):
		QDialog.__init__(self, parent)
		self._parent = parent
		tr = self.tr
		self.setWindowTitle(tr('MidPoints Filters Manager'))
		self.setSizeGripEnabled(True)
		# layout
		grid = QGridLayout(self)
		self.setLayout(grid)
		# list of filters
		self.filtersBox = QComboBox(self)
		self.filtersBox.setEditable(False)
		self.filtersBox.addItems(all_midpoints_filters_names())
		grid.addWidget(self.filtersBox, 0, 0)
		# buttons
		buttonsLayout = QHBoxLayout()
		grid.addLayout(buttonsLayout, 1, 0)
		newButton = QPushButton(tr('New'), self)
		self.connect(newButton, SIGNAL('clicked()'), self.newFilterEvent)
		buttonsLayout.addWidget(newButton)
		editButton = QPushButton(tr('Edit'), self)
		self.connect(editButton, SIGNAL('clicked()'), self.editFilterEvent)
		buttonsLayout.addWidget(editButton)
		deleteButton = QPushButton(tr('Delete'), self)
		self.connect(deleteButton, SIGNAL('clicked()'), self.deleteFilterEvent)
		buttonsLayout.addWidget(deleteButton)
		closeButton = QPushButton(tr('Close'), self)
		closeButton.setDefault(True)
		self.connect(closeButton, SIGNAL('clicked()'), SLOT('close()'))
		buttonsLayout.addWidget(closeButton)
	
	def newFilterEvent(self):
		new = MidPointsFilterDialog(self)
		ok = new.exec_()
		if ok:
			self.reset()
	
	def editFilterEvent(self):
		filt = MidPointsFilter(
			all_midpoints_filters_names()[self.filtersBox.currentIndex()])
		edit = MidPointsFilterDialog(self, filt)
		ok = edit.exec_()
		if ok:
			self.reset()
	
	def deleteFilterEvent(self):
		tr = self.tr
		name = all_midpoints_filters_names()[self.filtersBox.currentIndex()]
		ret = QMessageBox.warning(self, tr('Delete MidPoints Filter'),
			unicode(tr('Are you sure you want to delete mid-points filter \xab %(filter)s \xbb ?')) % {
				'filter': name},
			QMessageBox.Cancel|QMessageBox.Yes, QMessageBox.Yes)
		if ret == QMessageBox.Yes:
			filt = MidPointsFilter(name)
			try:
				filt.delete()
			except ValueError: # cannot delete default filter
				QMessageBox.critical(self, tr('Default MidPoints Filter'),
					tr('Cannot delete filter used as default.'))
			self.reset()
	
	def reset(self):
		"""Reload filters list."""
		self.filtersBox.clear()
		self.filtersBox.addItems(all_midpoints_filters_names())



def main():
	import sys
	app = QApplication(sys.argv)
	main = MidPointsFiltersManagerDialog()
	main.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()

# End.
