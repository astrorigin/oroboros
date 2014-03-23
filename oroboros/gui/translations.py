#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Translations.

"""

import os.path

from PyQt4.QtCore import *
from PyQt4.QtGui import *


__all__ = ['languages', 'load']


# available translations (fr, en, ...)
languages = []


_baseDir = os.path.join(os.path.dirname(os.path.abspath(__file__)))


def load(lng, app):
	if lng not in languages:
		return
	ts = QTranslator(app)
	ts.load('%s.qm' % lng, os.path.join(_baseDir, 'tr'))
	app.installTranslator(ts)
	


# End.
