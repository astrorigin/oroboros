#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Colors.

	Create a color instance.
	
		>>> clr = RGBColor(120, 120)
		>>> clr.set(blue=30)
		>>> print clr
		120,120,30

"""


__all__ = ['RGBColor']


class RGBColor(object):
	"""RGB color type.
	
		rgb = RGBColor(128, 128, 128)
	
	"""
	
	__slots__ = ['_red', '_green', '_blue']
	
	def _get_red(self):
		return self._red
	
	def _set_red(self, red):
		red = int(red)
		if red < 0 or red > 255:
			raise ValueError(red)
		self._red = red
		return
	
	def _get_green(self):
		return self._green
	
	def _set_green(self, green):
		green = int(green)
		if green < 0 or green > 255:
			raise ValueError(green)
		self._green = green
		return
	
	def _get_blue(self):
		return self._blue
	
	def _set_blue(self, blue):
		blue = int(blue)
		if blue < 0 or blue > 255:
			raise ValueError(blue)
		self._blue = blue
		return
	
	red = property(_get_red, _set_red, doc="Color red value.")
	green = property(_get_green, _set_green, doc="Color green value.")
	blue = property(_get_blue, _set_blue, doc="Color blue value.")
	
	def set(self, red=None, green=None, blue=None):
		"""Set color properties."""
		if red != None:
			self.red = red
		if green != None:
			self.green = green
		if blue != None:
			self.blue = blue
	
	def __init__(self, red=0, green=0, blue=0):
		"""RGB color instanciation."""
		self.red = red
		self.green = green
		self.blue = blue
	
	def __iter__(self):
		"""Return iterator over red, green, blue values."""
		return (x for x in (self._red, self._green, self._blue))
	
	def __str__(self):
		"""Return color as string (for database input)."""
		return '%s,%s,%s' % (self._red, self._green, self._blue)
	
	def __repr__(self):
		return 'oroboros.colors.RGBColor(%s, %s, %s)' % (self._red, self._green,
			self._blue)



def _test():
	import doctest
	doctest.testmod()


if __name__ == "__main__":
	_test()

# End.
