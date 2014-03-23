#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Astrological orbs and orbs-modifiers.

	Create orbs.
	
		>>> Orb(10)
		oroboros.orbs.Orb("10.0")
		>>> try:
		...     Orb(40.7) # limited to 30
		... except ValueError:
		...     print('Invalid orb value.')
		Invalid orb value.
	
	Create orb modifier:
	
		>>> om = OrbModifier("3") # add three degrees orbs
		>>> om
		oroboros.orbs.OrbModifier("3")
		>>> om = OrbModifier("-30%") # remove 30 % of orb
		>>> om
		oroboros.orbs.OrbModifier("-30%")

"""

import re
from decimal import Decimal


__all__ = ['Orb', 'OrbModifier']


# orb-modifiers regular expression
_regexp_orbmod = re.compile('^[+-]?[0-9]+\.?[0-9]*[%]?$')


class Orb(Decimal):
	"""Astrological orb type."""
	
	__slots__ = tuple()
	
	def __new__(cls, orb=0):
		"""Orb initialization (orb between 0 and 30).
		
		:type orb: numeric
		"""
		orb = float(orb)
		if orb < 0 or orb > 30: # we consider larger orbs to be errors...
			raise ValueError('Invalid orb value %s.' % orb)
		return Decimal.__new__(cls, str(orb))
	
	def __repr__(self):
		return "Orb('%s')" % self


class OrbModifier(str):
	"""Orb modifier type.
	
	Used to adjust orbs depending on the aspected planet.
	
	Either a float value, to add or substrat degrees (absolute),
	or a percentage value, to adjust the default orb (relative).
	
	"""

	__slots__ = tuple()
	
	def __new__(cls, modifier):
		"""New orb modifier.
		
		:type modifier: str or numeric
		"""
		modifier = str(modifier)
		if _regexp_orbmod.search(modifier) == None:
			raise ValueError('Invalid orb modifier %s.' % modifier)
		return str.__new__(cls, modifier)
	
	def get_absolute(self, orb):
		"""Get orb absolute value, compared to base orb.
		
		:type orb: numeric
		:rtype: Decimal
		"""
		if not self.endswith('%'):
			return Decimal(self)
		else:
			return (orb/Decimal('100')) * Decimal(self[:-1])
	
	def __repr__(self):
		return "OrbModifier('%s')" % self



def _test():
	import doctest
	doctest.testmod()


if __name__ == "__main__":
	_test()

# End.
