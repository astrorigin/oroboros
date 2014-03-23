#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Translated names.

"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *


__all__ = ['_encoding', 'signs', 'planets', 'houses', 'houseSystems',
	'sidModes', 'objects']


tr = lambda x, y=None: qApp.translate('names.py', x, y)


_encoding = unicode(tr('iso-8859-1', 'Encoding (reading non-utf8 files)'))


#: Signs
signs = {
	'Ari': unicode(tr('Ari', 'Aries')),
	'Tau': unicode(tr('Tau', 'Taurus')),
	'Gem': unicode(tr('Gem', 'Gemini')),
	'Can': unicode(tr('Can', 'Cancer')),
	'Leo': unicode(tr('Leo', 'Leo')),
	'Vir': unicode(tr('Vir', 'Virgo')),
	'Lib': unicode(tr('Lib', 'Libra')),
	'Sco': unicode(tr('Sco', 'Scorpio')),
	'Sag': unicode(tr('Sag', 'Sagittarius')),
	'Cap': unicode(tr('Cap', 'Capricorn')),
	'Aqu': unicode(tr('Aqu', 'Aquarius')),
	'Pis': unicode(tr('Pis', 'Pisces'))
	}

#: Planets
planets = {
	'Sun': unicode(tr('Sun')),
	'Moon': unicode(tr('Moon')),
	'Mercury': unicode(tr('Mercury')),
	'Venus': unicode(tr('Venus')),
	'Mars': unicode(tr('Mars')),
	'Jupiter': unicode(tr('Jupiter')),
	'Saturn': unicode(tr('Saturn')),
	'Uranus': unicode(tr('Uranus')),
	'Neptune': unicode(tr('Neptune')),
	'Pluto': unicode(tr('Pluto')),
	'Earth': unicode(tr('Earth')),
	'Chiron': unicode(tr('Chiron')),
	'Pholus': unicode(tr('Pholus')),
	'Ceres': unicode(tr('Ceres')),
	'Pallas': unicode(tr('Pallas')),
	'Juno': unicode(tr('Juno')),
	'Vesta': unicode(tr('Vesta')),
	'Rahu (mean)': unicode(tr('Rahu (mean)')),
	'Rahu (true)': unicode(tr('Rahu (true)')),
	'Ketu (mean)': unicode(tr('Ketu (mean)')),
	'Ketu (true)': unicode(tr('Ketu (true)')),
	'Lilith (mean)': unicode(tr('Lilith (mean)')),
	'Lilith (true)': unicode(tr('Lilith (true)')),
	'Priapus (mean)': unicode(tr('Priapus (mean)')),
	'Priapus (true)': unicode(tr('Priapus (true)')),
	'Cupido': unicode(tr('Cupido')),
	'Hades': unicode(tr('Hades')),
	'Zeus': unicode(tr('Zeus')),
	'Kronos': unicode(tr('Kronos')),
	'Apollon': unicode(tr('Apollon')),
	'Admetos': unicode(tr('Admetos')),
	'Vulkanus': unicode(tr('Vulkanus')),
	'Poseidon': unicode(tr('Poseidon')),
	'Isis': unicode(tr('Isis')),
	'Nibiru': unicode(tr('Nibiru')),
	'Harrington': unicode(tr('Harrington')),
	'Neptune (Leverrier)': unicode(tr('Neptune (Leverrier)')),
	'Neptune (Adams)': unicode(tr('Neptune (Adams)')),
	'Pluto (Lowell)': unicode(tr('Pluto (Lowell)')),
	'Pluto (Pickering)': unicode(tr('Pluto (Pickering)')),
	'Vulcan': unicode(tr('Vulcan')),
	'White Moon': unicode(tr('White Moon')),
	'Proserpina': unicode(tr('Proserpina')),
	'Waldemath': unicode(tr('Waldemath')),
	'Asc': unicode(tr('Asc')),
	'Mc': unicode(tr('Mc')),
	'Dsc': unicode(tr('Dsc')),
	'Ic': unicode(tr('Ic')),
	'Armc': unicode(tr('Armc')),
	'Vertex': unicode(tr('Vertex')),
	'Equatorial Ascendant': unicode(tr('Equatorial Ascendant')),
	'Co-ascendant (Koch)': unicode(tr('Co-ascendant (Koch)')),
	'Co-ascendant (Munkasey)': unicode(tr('Co-ascendant (Munkasey)')),
	'Polar Ascendant (Munkasey)': unicode(tr('Polar Ascendant (Munkasey)')),
	'Part of Fortune (Rudhyar)': unicode(tr('Part of Fortune (Rudhyar)')),
	'128 Nemesis': unicode(tr('128 Nemesis'))
	}

#: Houses
houses = {
	'Cusp 01': unicode(tr('Cusp 01')),
	'Cusp 02': unicode(tr('Cusp 02')),
	'Cusp 03': unicode(tr('Cusp 03')),
	'Cusp 04': unicode(tr('Cusp 04')),
	'Cusp 05': unicode(tr('Cusp 05')),
	'Cusp 06': unicode(tr('Cusp 06')),
	'Cusp 07': unicode(tr('Cusp 07')),
	'Cusp 08': unicode(tr('Cusp 08')),
	'Cusp 09': unicode(tr('Cusp 09')),
	'Cusp 10': unicode(tr('Cusp 10')),
	'Cusp 11': unicode(tr('Cusp 11')),
	'Cusp 12': unicode(tr('Cusp 12')),
	'Sector 01': unicode(tr('Sector 01')),
	'Sector 02': unicode(tr('Sector 02')),
	'Sector 03': unicode(tr('Sector 03')),
	'Sector 04': unicode(tr('Sector 04')),
	'Sector 05': unicode(tr('Sector 05')),
	'Sector 06': unicode(tr('Sector 06')),
	'Sector 07': unicode(tr('Sector 07')),
	'Sector 08': unicode(tr('Sector 08')),
	'Sector 09': unicode(tr('Sector 09')),
	'Sector 10': unicode(tr('Sector 10')),
	'Sector 11': unicode(tr('Sector 11')),
	'Sector 12': unicode(tr('Sector 12')),
	'Sector 13': unicode(tr('Sector 13')),
	'Sector 14': unicode(tr('Sector 14')),
	'Sector 15': unicode(tr('Sector 15')),
	'Sector 16': unicode(tr('Sector 16')),
	'Sector 17': unicode(tr('Sector 17')),
	'Sector 18': unicode(tr('Sector 18')),
	'Sector 19': unicode(tr('Sector 19')),
	'Sector 20': unicode(tr('Sector 20')),
	'Sector 21': unicode(tr('Sector 21')),
	'Sector 22': unicode(tr('Sector 22')),
	'Sector 23': unicode(tr('Sector 23')),
	'Sector 24': unicode(tr('Sector 24')),
	'Sector 25': unicode(tr('Sector 25')),
	'Sector 26': unicode(tr('Sector 26')),
	'Sector 27': unicode(tr('Sector 27')),
	'Sector 28': unicode(tr('Sector 28')),
	'Sector 29': unicode(tr('Sector 29')),
	'Sector 30': unicode(tr('Sector 30')),
	'Sector 31': unicode(tr('Sector 31')),
	'Sector 32': unicode(tr('Sector 32')),
	'Sector 33': unicode(tr('Sector 33')),
	'Sector 34': unicode(tr('Sector 34')),
	'Sector 35': unicode(tr('Sector 35')),
	'Sector 36': unicode(tr('Sector 36'))
	}

#: Objects (planets and houses)
objects = dict()
for k, v in planets.items():
	objects[k] = v
for k, v in houses.items():
	objects[k] = v


#: Aspects
aspects = {
	'Conjunction': unicode(tr('Conjunction')),
	'Opposition': unicode(tr('Opposition')),
	'Trine': unicode(tr('Trine')),
	'Square': unicode(tr('Square')),
	'Sextile': unicode(tr('Sextile')),
	'Quincunx': unicode(tr('Quincunx')),
	'SesquiSquare': unicode(tr('SesquiSquare')),
	'SemiSquare': unicode(tr('SemiSquare')),
	'SemiSextile': unicode(tr('SemiSextile')),
	'SquiSquare': unicode(tr('SquiSquare')),
	'SquiSextile': unicode(tr('SquiSextile')),
	'Quintile': unicode(tr('Quintile')),
	'BiQuintile': unicode(tr('BiQuintile')),
	'SemiQuintile': unicode(tr('SemiQuintile')),
	'Novile': unicode(tr('Novile')),
	'BiNovile': unicode(tr('BiNovile')),
	'QuadriNovile': unicode(tr('QuadriNovile')),
	'SemiNovile': unicode(tr('SemiNovile')),
	'Septile': unicode(tr('Septile')),
	'BiSeptile': unicode(tr('BiSeptile')),
	'TriSeptile': unicode(tr('TriSeptile')),
	'Undecile': unicode(tr('Undecile')),
	'BiUndecile': unicode(tr('BiUndecile')),
	'TriUndecile': unicode(tr('TriUndecile')),
	'QuadUndecile': unicode(tr('QuadUndecile')),
	'QuinUndecile': unicode(tr('QuinUndecile'))
	}

#: Available house systems
houseSystems = [ ## order matters so it's a list
	('P', unicode(tr('Placidus'))),
	('K', unicode(tr('Koch'))),
	('R', unicode(tr('Regiomontanus'))),
	('C', unicode(tr('Campanus'))),
	('B', unicode(tr('Alcabitus'))),
	('O', unicode(tr('Porphyrus'))),
	('A', unicode(tr('Equal'))),
	('H', unicode(tr('Aziumtal/horizontal'))),
	('V', unicode(tr('Vehlow equal'))),
	('X', unicode(tr('Axial rotation'))),
	('G', unicode(tr('Gauquelin sectors'))),
	('U', unicode(tr('Krusinski'))),
	('W', unicode(tr('Whole sign')))
	]

#: Sidereal modes
sidModes = [
	(-1, unicode(tr('None (western tropical)'))),
	(0, unicode(tr('Fagan-Bradley'))),
	(1, unicode(tr('Lahiri'))),
	(2, unicode(tr('Deluce'))),
	(3, unicode(tr('Raman'))),
	(4, unicode(tr('Ushashashi'))),
	(5, unicode(tr('Krishnamurti'))),
	(6, unicode(tr('Djwhal Khul'))),
	(7, unicode(tr('Yukteshwar'))),
	(8, unicode(tr('Jn Bhasin'))),
	(9, unicode(tr('Babyl. Kugler 1'))),
	(10, unicode(tr('Babyl. Kugler 2'))),
	(11, unicode(tr('Babyl. Kugler 3'))),
	(12, unicode(tr('Babyl. Huber'))),
	(13, unicode(tr('Babyl. ETPSC'))),
	(14, unicode(tr('Aldebaran 15Tau'))),
	(15, unicode(tr('Hipparchos'))),
	(16, unicode(tr('Sassanian'))),
	(17, unicode(tr('Gal. Center 0Sag'))),
	(18, unicode(tr('J2000'))),
	(19, unicode(tr('J1900'))),
	(20, unicode(tr('B1950'))),
	(255, unicode(tr('User-defined')))
	]



# End.
