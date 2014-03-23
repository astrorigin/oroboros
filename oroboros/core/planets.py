#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oroboros planets, asteroids, cusps, parts, etc.

	Load a planet object.
	
		>>> plnt = Planet('Sun')
		>>> print(plnt.num)
		0
		>>> plnt.bool_aspect, plnt.default_orbmod, plnt.bool_use
		(True, OrbModifier("0"), True)
		>>> plnt.family
		0
	
	Create a planet object.
	
		>>> plnt = Planet()
		>>> plnt.name = '128 Nemesis'
		>>> plnt.num = 10128 # swisseph number
		>>> plnt.bool_use = False # is not displayed by default
		>>> plnt.bool_aspect = True # is aspected by default
		>>> plnt.default_orbmod = '-10%' # remove 10% orb
		>>> plnt.glyph = 'glyphs/nemesis128.png' # relative path to glyph
		>>> plnt.comment = 'Asteroid 128 Nemesis'
		>>> plnt.family
		0
		>>> plnt.family = 3 # asteroids family
	
	Save planet object.
	
		>>> try:
		...     plnt.save() # is duplicate
		... except ValueError, err:
		...     print(err)
		...
		Duplicate planet 128 Nemesis.


"""

import swisseph as swe

from oroboros.core import db
from oroboros.core.orbs import OrbModifier
import oroboros.core.parts


__all__ = ['Planet', 'PlanetsList',
	'all_planets', 'all_planets_names',
	'xml_export_planets', 'xml_import_planets']



class Planet(db.Object):
	"""Planet(-like) object type.
	
	Includes asteroids, houses cusps, parts, etc.
	
	"""
	
	__slots__ = ('_idx_', '_num', '_name', '_family', '_ranking',
		'_bool_use', '_bool_aspect', '_default_orbmod', '_glyph', '_comment')
	
	def _get_num(self):
		"""Get planet swisseph number.
		
		:rtype: int
		"""
		return self._num
	
	def _set_num(self, num):
		"""Set planet number.
		
		:type num: int
		"""
		self._num = int(num)
	
	def _get_name(self):
		"""Get planet name.
		
		:rtype: str
		"""
		return self._name
	
	def _set_name(self, name):
		"""Set planet name.
		
		:type name: str
		"""
		self._name = name
	
	def _get_family(self):
		"""Get planet family.
		
			- 0 -> traditional planets
			- 1 -> uranian + fictitous bodies
			- 2 -> fixed stars
			- 3 -> additional asteroids
			- 4 -> houses
			- 5 -> parts
			- -1 -> no family (obliquity/nutation)
		
		:rtype: int
		"""
		return self._family
	
	def _set_family(self, family):
		"""Set planet family.
		
		:type family: int
		:raise ValueError: invalid family
		"""
		family = int(family)
		if family < -1 or family > 5:
			raise ValueError('Invalid family %s.' % family)
		self._family = family
	
	def _get_ranking(self):
		"""Get planet display rank.
		
		:rtype: int
		"""
		return self._ranking
	
	def _set_ranking(self, rank):
		"""Set display rank (0+).
		
		:type rank: int
		:raise ValueError: invalid rank
		"""
		rank = int(rank)
		if rank < 0:
			raise ValueError('Invalid display rank %s < 0.' % rank)
		self._ranking = rank
	
	def _get_bool_use(self):
		"""Get planet default usage (for new filters).
		
		:rtype: bool
		"""
		return self._bool_use
	
	def _set_bool_use(self, bool_use):
		"""Set planet default usage (for new plnt filters).
		
		:type bool_use: bool
		"""
		if bool_use in (True, '1', 1, 'True', 'true', 'yes'):
			self._bool_use = True
		elif bool_use in (False, '0', 0, 'False', 'false', 'no'):
			self._bool_use = False
		else:
			self._bool_use = bool(bool_use)
	
	def _get_bool_aspect(self):
		"""Get planet default show aspects (for new plntasp filters).
		
		:rtype: bool
		"""
		return self._bool_aspect
	
	def _set_bool_aspect(self, bool_asp):
		"""Set planet default show aspects (for new plntasp filters).
		
		:type bool_asp: bool
		"""
		if bool_asp in (True, '1', 1, 'True', 'true', 'yes'):
			self._bool_aspect = True
		elif bool_asp in (False, '0', 0, 'False', 'false', 'no'):
			self._bool_aspect = False
		else:
			self._bool_aspect = bool(bool_asp)
	
	def _get_default_orbmod(self):
		"""Return planet default orb modifier (for new filters).
		
		:rtype: OrbModifier
		"""
		return self._default_orbmod
	
	def _set_default_orbmod(self, orbmod):
		"""Set planet default orb modifier (for new filters).
		
		:type orbmod: OrbModifier or str or numeric
		"""
		if isinstance(orbmod, OrbModifier):
			self._default_orbmod = orbmod
		else:
			self._default_orbmod = OrbModifier(orbmod)
	
	def _get_glyph(self):
		"""Get planet glyph (image).
		
		:rtype: str
		"""
		return self._glyph
	
	def _set_glyph(self, imgpath):
		"""Set planet glyph (image).
		
		:type imgpath: str
		"""
		self._glyph = imgpath
	
	def _get_comment(self):
		"""Get planet comment.
		
		:rtype: str
		"""
		return self._comment
	
	def _set_comment(self, comment):
		"""Set planet comment.
		
		:type comment: str
		"""
		self._comment = comment
	
	_idx = property(db.Object._get_idx, db.Object._set_idx,
		doc="Planet db index value.")
	num = property(_get_num, _set_num,
		doc="Planet swisseph number.")
	name = property(_get_name, _set_name,
		doc="Planet name.")
	family = property(_get_family, _set_family,
		doc='Planet family.')
	ranking = property(_get_ranking, _set_ranking,
		doc='Planet display rank.')
	bool_use = property(_get_bool_use, _set_bool_use,
		doc="Planet default usage (boolean) (for new filters).")
	bool_aspect = property(_get_bool_aspect, _set_bool_aspect,
		doc="Planet default show aspects (boolean) (for new filters).")
	default_orbmod = property(_get_default_orbmod, _set_default_orbmod,
		doc="Planet default orb modifier (for new filters).")
	glyph = property(_get_glyph, _set_glyph,
		doc="Planet glyph (image).")
	comment = property(_get_comment, _set_comment,
		doc="Planet comment.")
	
	def set(self, _idx=None, num=None, name=None, family=None, ranking=None,
		bool_use=None, bool_aspect=None, default_orbmod=None, glyph=None,
		comment=None):
		"""Set planet properties.
		
		Args: 'num', 'name', 'ranking', 'family', 'bool_use', 'bool_aspect',
		'default_orbmod', 'glyph', 'comment'
		
		"""
		if _idx != None:
			self._idx = _idx
		if num != None:
			self.num = num
		if name != None:
			self.name = name
		if family != None:
			self.family = family
		if ranking != None:
			self.ranking = ranking
		if bool_use != None:
			self.bool_use = bool_use
		if bool_aspect != None:
			self.bool_aspect = bool_aspect
		if default_orbmod != None:
			self.default_orbmod = default_orbmod
		if glyph != None:
			self.glyph = glyph
		if comment != None:
			self.comment = comment
	
	def __init__(self, planet=None):
		"""Planet initialization.
		
		:type planet: str or int or None
		"""
		if planet != None:
			self._select(planet)
		else:
			self._idx_ = None
			self._num = None
			self._name = ''
			self._family = None
			self._ranking = 0
			self._bool_use = True
			self._bool_aspect = True
			self._default_orbmod = OrbModifier('0')
			self._glyph = 'unknownplanet.png'
			self._comment = ''
	
	def _select(self, planet):
		"""Select a planet by num or by name.
		
		:type planet: str or int
		:raise TypeError: invalid planet
		"""
		if isinstance(planet, int):
			return self._select_by_num(planet)
		elif isinstance(planet, basestring): # str in py3
			return self._select_by_name(planet)
		raise TypeError('Invalid planet %s.' % planet)
	
	def _select_by_idx(self, idx):
		"""Select a planet definition in database (by idx).
		
		:type idx: int
		:raise ValueError: not found
		"""
		sql = "select * from Planets where _idx = ?;"
		res = db.execute(sql, (idx,)).fetchall()
		if len(res) == 0:
			raise ValueError('Invalid planet idx: %s.' % idx)
		self.set(*res[0])
	
	def _select_by_name(self, planet):
		"""Select a planet definition in database (by name).
		
		:type planet: str
		:raise ValueError: not found
		"""
		sql = "select * from Planets where name = ?;"
		res = db.execute(sql, (planet,)).fetchall()
		if len(res) == 0:
			raise ValueError('Invalid planet name: %s.' % planet)
		self.set(*res[0])
	
	def _select_by_num(self, num):
		"""Select a planet definition in database (by swisseph num).
		
		:type num: int
		:raise ValueError: not found
		"""
		sql = "select * from Planets where num = ?;"
		res = db.execute(sql, (num,)).fetchall()
		if len(res) == 0:
			raise ValueError('Invalid swisseph num: %s' % num)
		self.set(*res[0])
	
	def save(self):
		"""Save planet in database."""
		if self._idx_ == None:
			self._insert()
		else:
			self._update()
	
	def _insert(self):
		"""Insert planet in database.
		
		:raise ValueError: duplicate
		"""
		sql1 = """insert into Planets (num, name, family, ranking, bool_use,
			bool_aspect, default_orbmod, glyph, comment) values (?, ?, ?,
			?, ?, ?, ?, ?);"""
		sql2 = "select _idx from Planets where num = ?;"
		var = (self._num, self._name, self._family, self._ranking,
			self._bool_use, self._bool_aspect, self._default_orbmod,
			self._glyph, self._comment)
		try:
			db.execute(sql1, var)
		except: # sqlite3.IntegrityError
			raise ValueError('Duplicate planet %s.' % self._name)
		self._idx = db.execute(sql2, (self._num,)).fetchone()[0]
	
	def _update(self):
		"""Update planet definition in database.
		
		:raise ValueError: duplicate
		"""
		sql = """update Planets set num = ?, name = ?, family = ?, ranking = ?,
			bool_use = ?, bool_aspect = ?, default_orbmod = ?, glyph = ?,
			comment = ? where _idx = ?;"""
		var = (self._num, self._name, self._family, self._bool_use,
			self._bool_aspect, self._default_orbmod, self._glyph,
			self._comment, self._idx_)
		try:
			db.execute(sql, var)
		except: # integrity error
			raise ValueError('Duplicate planet %s.' % self._name)
	
	def delete(self):
		"""Delete planet definition in database (by idx).
		
		:raise TypeError: invalid index
		"""
		if self._idx_ == None:
			raise TypeError('Missing planet idx.')
		sql = "delete from Planets where _idx = ?;"
		db.execute(sql, (self._idx_,))
		self._idx_ = None
	
	def __iter__(self):
		"""Return iterator over planet properties (including planet type).
		
		:rtype: iterator
		"""
		return (x for x in (self._idx_, self._num, self._name, self._family,
			self._ranking, self._bool_use, self._bool_aspect,
			self._default_orbmod, self._glyph, self._comment))
	
	def __str__(self):
		"""Show planet internals.
		
		:rtype: str
		"""
		return str(tuple(self))
	
	def __repr__(self):
		if self._idx_ == None:
			return repr(tuple(repr(x) for x in self))
		return "Planet('''%s''')" % self.name
	
	def __getstate__(self):
		return {'_idx': None,
			'num': self._num,
			'name': self._name,
			'family': self._family,
			'ranking': self._ranking,
			'bool_use': self._bool_use,
			'bool_aspect': self._bool_aspect,
			'default_orbmod': self._default_orbmod,
			'glyph': self._glyph,
			'comment': self._comment}
	
	def _to_xml(self, with_idx=False):
		"""Return a xmlutils.Element('Planet').
		
		:type with_idx: bool
		:rtype: xmlutils.Element
		"""
		if with_idx:
			el = xmlutils.Element('Planet', {'_idx': self._idx_}, '\n\t', '\n')
		else:
			el = xmlutils.Element('Planet', {'_idx': None}, '\n\t', '\n')
		el.append('num', {}, self._num, '\n\t')
		el.append('name', {}, self._name, '\n\t')
		el.append('family', {}, self._family, '\n\t')
		el.append('ranking', {}, self._ranking, '\n\t')
		el.append('bool_use', {}, self._bool_use, '\n\t')
		el.append('bool_aspect', {}, self._bool_aspect, '\n\t')
		el.append('default_orbmod', {}, self._default_orbmod, '\n\t')
		el.append('glyph', {}, self._glyph, '\n\t')
		el.append('comment', {}, self._comment, '\n\t')
		return el
	
	def _from_xml(self, elem, with_idx=False):
		"""Set aspect from a xmlutils.Element('Planet').
		
		:type elem: xmlutils.Element
		:type with_idx: bool
		"""
		if with_idx:
			_idx = elem.get_attr('_idx')
			if _idx == 'None':
				self._idx_ = None
			else:
				self._idx = _idx
		self.set(num=elem.get_child_text(tag='num'),
			name=elem.get_child_text(tag='name').replace('&lt;',
				'<').replace('&gt;', '>'),
			family=elem.get_child_text(tag='family'),
			ranking=elem.get_child_text(tag='ranking'),
			bool_use=elem.get_child_text(tag='bool_use'),
			bool_aspect=elem.get_child_text(tag='bool_aspect'),
			default_orbmod=elem.get_child_text(tag='default_orbmod'),
			glyph=elem.get_child_text(tag='gylph'),
			comment=elem.get_child_text(tag='comment').replace('&lt;',
				'<').replace('&gt;', '>'))
	
	def calc_ut(self, jd, flag, chart=None):
		"""Return calculations results.
		
		Houses cusps are calculated in block (see chartcalc).
		Parts require that you pass the chart object.
		
		:type jd: numeric
		:type flag: int
		:type chart: ChartCalc
		:raise ValueError: invalid planet (houses)
		"""
		if self._family == 4:
			raise ValueError('Cannot calculate houses.')
		# "inverted objects". Should invert latitude too??
		elif self._num == -2: # ketu (mean)
			r = swe.calc_ut(jd, 10, flag)
			return (swe.degnorm(r[0]-180),
				r[1], r[2], r[3], r[4], r[5])
		elif self._num == -3: # ketu (true)
			r = swe.calc_ut(jd, 11, flag)
			return (swe.degnorm(r[0]-180),
				r[1], r[2], r[3], r[4], r[5])
		elif self._num == -4: # priapus (mean)
			r = swe.calc_ut(jd, 12, flag)
			return (swe.degnorm(r[0]-180),
				r[1], r[2], r[3], r[4], r[5])
		elif self._num == -5: # priapus (true)
			r = swe.calc_ut(jd, 13, flag)
			return (swe.degnorm(r[0]-180),
				r[1], r[2], r[3], r[4], r[5])
		# planets, asteroids, etc
		elif self._family in (0, 1, 3):
			return swe.calc_ut(jd, self._num, flag)
		# fixed stars
		elif self._family == 2:
			return swe.fixstar_ut(self._name, jd, flag)
		# parts
		elif self._family == 5:
			return oroboros.core.parts.calc_ut(self._name, chart)



class PlanetsList(list):
	"""Planets list object."""
	
	def __getitem__(self, item):
		if isinstance(item, int):
			return list.__getitem__(self, item)
		for p in self:
			if p._name == item:
				return p
		raise KeyError(item)
	
	def __contains__(self, item):
		for p in self:
			if p._name == item:
				return True
		return False
	
	def get_idx(self, idx):
		for p in self:
			if p._idx_ == idx:
				return p
		raise KeyError(idx)
	
	def get_num(self, num):
		for p in self:
			if p._num == num:
				return p
		raise KeyError(num)


def all_planets():
	"""Return a list of all planet objects.
	
	:rtype: PlanetsList
	"""
	ret = PlanetsList()
	sql = "select * from Planets order by ranking;"
	res = db.execute(sql)
	for row in res:
		ret.append(Planet())
		ret[-1].set(*row)
	return ret


def all_planets_names():
	"""Return a list of all planets names.
	
	:rtype: list
	"""
	ret = list()
	sql = 'select name from Planets order by ranking;'
	res = db.execute(sql).fetchall()
	for row in res:
		ret.append(row[0])
	return ret


def xml_export_planets(with_idx=False):
	"""Return a xmlutils.Element('Planets') containing all planets.
	
	:type with_idx: bool
	:rtype: xmlutils.Element
	"""
	all = all_planets()
	el = xmlutils.Element('Planets', {}, '\n', '\n')
	for a in all:
		el.append(a._to_xml(with_idx=with_idx))
	return el


def xml_import_planets(elem, with_idx=False):
	"""Return a list of planets from a xmlutils.Element.
	
	:type elem: xmlutils.Element
	:type with_idx: bool
	:rtype: PlanetsList
	"""
	ret = PlanetsList()
	for a in elem.get_iterator('Planet'):
		ret.append(Planet())
		ret[-1]._from_xml(a, with_idx=_with_idx)
	return ret



def _test():
	import doctest
	doctest.testmod()


if __name__ == "__main__":
	_test()

# End.

