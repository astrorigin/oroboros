#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Orbs modifiers widgets.

"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *


__all__ = ['OrbModifierSpinBox']


class OrbModifierSpinBox(QDoubleSpinBox):
	"""Orb modifier spin box.
	
	For the moment only relative modifiers are supported (percent).
	
	"""
	
	def __init__(self, parent):
		QDoubleSpinBox.__init__(self, parent)
		self.setRange(-100, 100)
		self.setSuffix(self.tr('%', 'percent'))
		self.setButtonSymbols(QAbstractSpinBox.PlusMinus)



# End.
