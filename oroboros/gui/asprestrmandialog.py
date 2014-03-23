#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Aspects restrictions manager.

"""

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from oroboros.core.aspectsrestrictions import AspectsRestrictions, all_aspects_restrictions_names
from oroboros.gui.asprestrdialog import AspectsRestrictionsDialog


__all__ = ['AspectsRestrictionsManagerDialog']


class AspectsRestrictionsManagerDialog(QDialog):
	
	def __init__(self, parent=None):
		QDialog.__init__(self, parent)
		self._parent = parent
		tr = self.tr
		self.setWindowTitle(tr('Aspects Restrictions Manager'))
		self.setSizeGripEnabled(True)
		# layout
		grid = QGridLayout(self)
		self.setLayout(grid)
		# list of filters
		self.filtersBox = QComboBox(self)
		self.filtersBox.setEditable(False)
		self.filtersBox.addItems(all_aspects_restrictions_names())
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
		new = AspectsRestrictionsDialog(self)
		ok = new.exec_()
		if ok:
			self.reset()
	
	def editFilterEvent(self):
		filt = AspectsRestrictions(
			all_aspects_restrictions_names()[self.filtersBox.currentIndex()])
		edit = AspectsRestrictionsDialog(self, filt)
		ok = edit.exec_()
		if ok:
			self.reset()
	
	def deleteFilterEvent(self):
		tr = self.tr
		name = all_aspects_restrictions_names()[self.filtersBox.currentIndex()]
		ret = QMessageBox.warning(self, tr('Delete Aspects Restrictions'),
			unicode(tr('Are you sure you want to delete aspects restrictions \xab %(filter)s \xbb ?')) % {
				'filter': name},
			QMessageBox.Cancel|QMessageBox.Yes, QMessageBox.Yes)
		if ret == QMessageBox.Yes:
			filt = AspectsRestrictions(name)
			try:
				filt.delete()
			except ValueError: # cannot delete default filter
				QMessageBox.critical(self, tr('Required Aspects Restrictions'),
					tr('Cannot delete required aspects restrictions.'))
			self.reset()
	
	def reset(self):
		"""Reload filters list."""
		self.filtersBox.clear()
		self.filtersBox.addItems(all_aspects_restrictions_names())



def main():
	app = QApplication(sys.argv)
	main = AspectsRestrictionsManagerDialog()
	main.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()

# End.
