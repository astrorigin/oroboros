#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Parts calculations.

"""

import swisseph as swe


__all__ = ['calc_ut']


def calc_ut(part, cht):
	"""Calculate part positions.
	
	Chart should have houses calculated (asc, mc, etc).
	
	:type part: str
	:type cht: Chart
	"""
	if part == 'Part of Fortune (Rudhyar)':
		return part_of_fortune_rudhyar(cht)
	raise ValueError('Invalid part %s.' % part)


def part_of_fortune_rudhyar(cht):
	"""Calculate part of fortune (Rudhyar).
	
	:type cht: Chart
	"""
	flag = cht._filter.get_calcflag()
	sun = swe.calc_ut(cht.julday, swe.SUN, flag)
	moon = swe.calc_ut(cht.julday, swe.MOON, flag)
	pos = swe.degnorm(
		cht._houses.get_positions('Asc')._longitude + (
			swe.difdegn(moon[0], sun[0])))
	return (pos, 0, 0, 0, 0, 0)



def _test():
	import doctest
	doctest.testmod()


if __name__ == '__main__':
	_test()

# End.
