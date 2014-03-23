#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
New tab dialog.

"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *


__all__ = ['NewTabDialog']



class NewTabDialog(QDialog):
	
	def __init__(self, parent=None):
		QDialog.__init__(self, parent)
		tr = self.tr
		self.setWindowTitle(tr('New Chart'))
		self.setSizeGripEnabled(True)
		# layout
		layout = QVBoxLayout(self)
		self.setLayout(layout)
		# button group
		self.grpButtons = QButtonGroup(self)
		# here-now button
		hereNowButton = QRadioButton(tr('Here-Now Chart'), self)
		hereNowButton.setChecked(True)
		self.grpButtons.addButton(hereNowButton, 0)
		layout.addWidget(hereNowButton)
		# open chart
		openButton = QRadioButton(tr('Open File'), self)
		self.grpButtons.addButton(openButton, 1)
		layout.addWidget(openButton)
		# custom chart
		customButton = QRadioButton(tr('Custom Chart'), self)
		self.grpButtons.addButton(customButton, 2)
		layout.addWidget(customButton)
		# open astrolog32
		openA32Button = QRadioButton(tr('Open Astrolog32'), self)
		self.grpButtons.addButton(openA32Button, 3)
		layout.addWidget(openA32Button)
		# open skif
		openSkifButton = QRadioButton(tr('Open Skif'), self)
		self.grpButtons.addButton(openSkifButton, 4)
		layout.addWidget(openSkifButton)
		# dialog buttons
		bLayout = QHBoxLayout()
		layout.addLayout(bLayout)
		cancelButton = QPushButton(tr('Cancel'), self)
		self.connect(cancelButton, SIGNAL('clicked()'), self.reject)
		bLayout.addWidget(cancelButton)
		okButton = QPushButton(tr('OK'), self)
		okButton.setDefault(True)
		self.connect(okButton, SIGNAL('clicked()'), self.accept)
		bLayout.addWidget(okButton)
	
	def exec_(self):
		ok = QDialog.exec_(self)
		if ok:
			return ok, self.grpButtons.checkedId()
		else:
			return ok, None
	
	

def main():
	import sys
	app = QApplication(sys.argv)
	main = NewTabDialog()
	main.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()

# End.
