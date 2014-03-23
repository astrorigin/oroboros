#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Produce charts images.

"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSvg import QSvgGenerator


from oroboros.gui.chtpainter import ChartPainter


__all__ = ['makeImage', 'makeSvg']


def makeImage(chart, path, ext, width, height, quality=-1):
	"""Create an image file for a chart.
	
	:type chart: BiChart
	:type path: str
	:type ext: str
	:type width: int
	:type height: int
	:type quality: int
	"""
	im = QImage(width, height, QImage.Format_ARGB32_Premultiplied)
	ChartPainter(im, chart)
	if not path.endswith(ext):
		path = '%s.%s' % (path, ext)
	im.save(path, None, quality)


def makeSvg(chart, path, width, height):
	"""Create a Svg file.
	
	:type chart: BiChart
	:type path: str
	:type width: int
	:type height: int
	"""
	svg = QSvgGenerator()
	if not path.endswith('.svg'):
		path = '%s%s' % (path, '.svg')
	svg.setFileName(path)
	svg.setSize(QSize(width, height))
	##svg.setResolution(100)
	ChartPainter(svg, chart)


# End.
