#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Aspects.

	Create an aspect.
	
		>>> myAsp = Aspect()
		>>> myAsp.name='my aspect'
		>>> myAsp.angle = 21.436
		>>> myAsp.ranking = 1
		>>> myAsp.bool_use = True
		>>> myAsp.default_orb = 2
		>>> myAsp.color = (128, 155, 0)
	
	Print aspect.
	
		>>> print myAsp
		(None, 'my aspect', oroboros.aspects.PiAngle("21.436"), 1, True, oroboros.orbs.Orb("2.0"), oroboros.colors.RGBColor(128, 155, 0), 'unknownaspect.png', '', None)
		>>> myAsp # repr() of aspect not in database
		'(None, \\'my aspect\\', oroboros.aspects.PiAngle("21.436"), 1, True, oroboros.orbs.Orb("2.0"), oroboros.colors.RGBColor(128, 155, 0), \\'unknownaspect.png\\', \\'\\', None)'
	
	Insert, update, delete the aspect definition.
	
		>>> myAsp.save()
		>>> myAsp # repr() of aspect in database
		Aspect('''my aspect''')
		>>> myAsp.set(name='Experimental')
		>>> myAsp.save()
		>>> myAsp.delete()
	
	Load an aspect definition.
	
		>>> asp = Aspect('Conjunction')
		>>> print asp
		(1, u'Conjunction', oroboros.aspects.PiAngle("0.0"), 1, True, oroboros.orbs.Orb("10.0"), oroboros.colors.RGBColor(255, 255, 0), u'conjunction.png', u'', None)
	
	Search functions.
	
		>>> all_aspects
		[oroboros.aspects.Aspect('''Conjunction'''), oroboros.aspects.Aspect('''Opposition'''), oroboros.aspects.Aspect('''Trine'''), oroboros.aspects.Aspect('''Square'''), oroboros.aspects.Aspect('''Sextile'''), oroboros.aspects.Aspect('''Quincunx'''), oroboros.aspects.Aspect('''SesquiSquare'''), oroboros.aspects.Aspect('''SemiSquare'''), oroboros.aspects.Aspect('''SemiSextile'''), oroboros.aspects.Aspect('''SquiSquare'''), oroboros.aspects.Aspect('''SquiSextile'''), oroboros.aspects.Aspect('''Quintile'''), oroboros.aspects.Aspect('''BiQuintile'''), oroboros.aspects.Aspect('''SemiQuintile'''), oroboros.aspects.Aspect('''Novile'''), oroboros.aspects.Aspect('''BiNovile'''), oroboros.aspects.Aspect('''QuadroNovile'''), oroboros.aspects.Aspect('''SemiNovile'''), oroboros.aspects.Aspect('''Septile'''), oroboros.aspects.Aspect('''BiSeptile'''), oroboros.aspects.Aspect('''TriSeptile'''), oroboros.aspects.Aspect('''Undecile'''), oroboros.aspects.Aspect('''BiUndecile'''), oroboros.aspects.Aspect('''TriUndecile'''), oroboros.aspects.Aspect('''QuadUndecile'''), oroboros.aspects.Aspect('''QuinUndecile''')]
	
	XML functions.
	
		TODO

"""

from decimal import Decimal

from oroboros.core import db
from oroboros.core.orbs import Orb
from oroboros.core.colors import RGBColor
from oroboros.core import xmlutils


__all__ = ['Aspect', 'AspectsList',
	'all_aspects', 'all_aspects_names',
	'xml_export_aspects', 'xml_import_aspects']



class PiAngle(Decimal):
	"""Aspect angle type (in degrees, despite the name) [0;180]."""
	
	__slots__ = tuple()
	
	def __new__(cls, angle=0):
		"""Aspect angle initialization (angle between 0 and 180)."""
		angle = float(angle)
		if angle < 0 or angle > 180:
			raise ValueError('Invalid angle %s.' % angle)
		return Decimal.__new__(cls, str(angle))
	
	def __repr__(self):
		return "PiAngle('%s')" % self


class Aspect(db.Object):
	"""Aspect type."""
	
	__slots__ = ('_idx_', '_name', '_angle', '_ranking', '_bool_use',
		'_default_orb', '_color', '_glyph', '_comment')
	
	def _get_name(self):
		"""Get aspect name.
		
		:rtype: str
		"""
		return self._name
	
	def _set_name(self, name):
		"""Set aspect name.
		
		:type name: str
		"""
		self._name = name
	
	def _get_angle(self):
		"""Get aspect angle.
		
		:rtype: PiAngle
		"""
		return self._angle
	
	def _set_angle(self, angle):
		"""Set aspect angle.
		
		:type angle: numeric
		"""
		self._angle = PiAngle(angle)
	
	def _get_ranking(self):
		"""Get aspect display rank.
		
		:rtype: int
		"""
		return self._ranking
	
	def _set_ranking(self, ranking):
		"""Set aspect display rank (must be >= 0).
		
		:type ranking: numeric
		:raise ValueError: rank < 0
		"""
		ranking = int(ranking)
		if ranking < 0:
			raise ValueError('Invalid display rank %s.' % ranking)
		self._ranking = ranking
	
	def _get_bool_use(self):
		"""Get aspect default usage (for new filters).
		
		:rtype: bool
		"""
		return self._bool_use
	
	def _set_bool_use(self, bool_use):
		"""Set aspect default usage (for new filters).
		
		:type bool_use: bool
		"""
		if bool_use in (True, '1', 1, 'True', 'true', 'yes'):
			self._bool_use = True
		elif bool_use in (False, '0', 0, 'False', 'false', 'no'):
			self._bool_use = False
		else:
			self._bool_use = bool(bool_use)
	
	def _get_default_orb(self):
		"""Get aspect default orb object (for new filters).
		
		:rtype: Orb
		"""
		return self._default_orb
	
	def _set_default_orb(self, default_orb):
		"""Set aspect default orb value (for new filters).
		
		Accepts Orb object, or float value.
		
		:type default_orb: Orb or numeric
		:raise TypeError: invalid orb
		"""
		if isinstance(default_orb , Orb):
			self._default_orb = default_orb
		elif isinstance(default_orb, (int, float)):
			self._default_orb = Orb(default_orb)
		else:
			raise TypeError('Invalid orb %s.' % default_orb)
	
	def _get_color(self):
		"""Get aspect color.
		
		:rtype: RGBColor
		"""
		return self._color
	
	def _set_color(self, color):
		"""Set aspect color.
		
		Accepts RGBColor object, sequence(r,g,b) or str 'r,g,b'
		
		:type color: RGBColor or sequence or str
		:raise TypeError: invalid color
		"""
		if isinstance(color, RGBColor):
			self._color = color
		elif isinstance(color, (tuple, list)):
			self._color = RGBColor(*color)
		elif isinstance(color, basestring): # must be str in py3
			self._color = RGBColor(*color.split(','))
		else:
			raise TypeError('Invalid color %s.' % color)
	
	def _get_glyph(self):
		"""Get aspect glyph (image).
		
		Actually not used.
		
		:rtype: str
		"""
		return self._glyph
	
	def _set_glyph(self, path):
		"""Set aspect glyph (image).
		
		:type path: str
		"""
		self._glyph = path
	
	def _get_comment(self):
		"""Get aspect comment.
		
		:rtype: str
		"""
		return self._comment
	
	def _set_comment(self, comment):
		"""Set aspect comment.
		
		:type comment: str
		"""
		self._comment = comment
	
	_idx = property(db.Object._get_idx, db.Object._set_idx,
		doc="Aspect db index value.")
	name = property(_get_name, _set_name,
		doc="Aspect name.")
	angle = property(_get_angle, _set_angle,
		doc="Aspect angle.")
	ranking = property(_get_ranking, _set_ranking,
		doc="Aspect display rank.")
	bool_use = property(_get_bool_use, _set_bool_use,
		doc="Aspect default usage (for new filters) (boolean).")
	default_orb = property(_get_default_orb, _set_default_orb,
		doc="Aspect default orb (for new filters).")
	color = property(_get_color, _set_color,
		doc="Aspect color.")
	glyph = property(_get_glyph, _set_glyph,
		doc="Aspect glyph.")
	comment = property(_get_comment, _set_comment,
		doc="Aspect comment.")
	
	def set(self, _idx=None, name=None, angle=None, ranking=None,
		bool_use=None, default_orb=None, color=None, glyph=None,
		comment=None):
		"""Set aspect properties.
		
		Args: 'name', 'angle', 'ranking', 'bool_use', 'default_orb',
			'color', 'comment'
		
		"""
		if _idx != None:
			self._idx = _idx
		if name != None:
			self.name = name
		if angle != None:
			self.angle = angle
		if ranking != None:
			self.ranking = ranking
		if bool_use != None:
			self.bool_use = bool_use
		if default_orb != None:
			self.default_orb = default_orb
		if color != None:
			self.color = color
		if glyph != None:
			self.glyph = glyph
		if comment != None:
			self.comment = comment
	
	def __init__(self, aspect=None):
		"""Aspect initialization.
		
		:type aspect: int or str or PiAngle or None
		"""
		if aspect != None:
			self._select(aspect)
		else:
			self._idx_ = None
			self._name = ''
			self._angle = PiAngle()
			self._ranking = 1
			self._bool_use = True
			self._default_orb = Orb()
			self._color = RGBColor()
			self._glyph = 'unknownaspect.png'
			self._comment = ''
	
	def _select(self, aspect):
		"""Select aspect by its name (str), angle object, or id (int).
		
		:raise TypeError: invalid aspect
		"""
		if isinstance(aspect, int):
			return self._select_by_idx(aspect)
		elif isinstance(aspect, basestring): # str in py3
			return self._select_by_name(aspect)
		elif isinstance(aspect, PiAngle):
			return self._select_by_angle(aspect)
		raise TypeError('Invalid aspect %s.' % aspect)
	
	def _select_by_idx(self, idx):
		"""Select aspect from database, with idx.
		
		:type idx: int
		:raise ValueError: not found
		"""
		sql = "select * from Aspects where _idx = ?;"
		res = db.execute(sql, (idx,)).fetchall()
		if len(res) == 0:
			raise ValueError('Invalid idx %s.' % idx)
		return self.set(*res[0])
	
	def _select_by_name(self, aspect):
		"""Select aspect from database, with name.
		
		:type aspect: str
		:raise ValueError: not found
		"""
		sql = "select * from Aspects where name = ?;"
		res = db.execute(sql, (aspect,)).fetchall()
		if len(res) == 0:
			raise ValueError('Invalid aspect %s.' % aspect)
		return self.set(*res[0])
	
	def _select_by_angle(self, angle):
		"""Select aspect from database, with angle (PiAngle).
		
		:type angle: PiAngle
		:raise ValueError: not found
		"""
		sql = "select * from Aspects where angle = ?;"
		res = db.execute(sql, (angle,)).fetchall()
		if len(res) == 0:
			raise ValueError('Invalid angle %s.' % angle)
		return self.set(*res[0])
	
	def save(self):
		"""Save aspect in database."""
		if self._idx_ == None:
			self._insert()
		else:
			self._update()
	
	def _insert(self):
		"""Insert new aspect in database.
		
		:raise ValueError: duplicate
		"""
		sql1 = """insert into Aspects (name, angle, ranking,
			bool_use, default_orb, color, glyph, comment) values (?, ?,
			?, ?, ?, ?, ?, ?);"""
		sql2 = "select _idx from Aspects where name = ?;"
		var = (self._name, str(self._angle), self._ranking,
			int(self._bool_use), str(self._default_orb),
			str(self._color), self._glyph, self._comment)
		try:
			db.execute(sql1, var)
		except: # sqlite3.IntegrityError
			raise ValueError('Duplicate filter %s.' % self._name)
		self._idx = db.execute(sql2, (self._name,)).fetchone()[0]
	
	def _update(self):
		"""Update aspect in database.
		
		:raise ValueError: duplicate
		"""
		sql = """update Aspects set name = ?, angle = ?, ranking = ?,
			bool_use = ?, default_orb = ?, color = ?, glyph = ?,
			comment = ? where _idx = ?;"""
		var = (self._name, str(self._angle), self._ranking,
			int(self._bool_use), str(self._default_orb),
			str(self._color), self._glyph, self._comment, self._idx_)
		try:
			db.execute(sql, var)
		except: # integrity error
			raise ValueError('Duplicate aspect.')
	
	def delete(self):
		"""Delete aspect in database.
		
		:raise TypeError: missing index
		"""
		if self._idx_ == None:
			raise TypeError('Missing idx.')
		sql = "delete from Aspects where _idx = ?;"
		db.execute(sql, (self._idx_,))
		self._idx_ = None
	
	def __iter__(self):
		"""Return iterator over aspect properties.
		
		:rtype: iterator
		"""
		return (x for x in (self._idx_, self._name, self._angle,
			self._ranking, self._bool_use, self._default_orb,
			self._color, self._glyph, self._comment))
	
	def __int__(self):
		"""Get aspect idx, or 0 if aspect is not loaded from database.
		
		:rtype: int
		"""
		if self._idx_ != None:
			return self._idx_
		return 0
	
	def __str__(self):
		"""Show aspect internals.
		
		:rtype: str
		"""
		return str(tuple(self))
	
	def __repr__(self):
		if self._idx_ == None:
			return repr(tuple(repr(x) for x in self))
		return "Aspect('''%s''')" % self._name
	
	def __getstate__(self):
		return {'_idx': None,
			'name': self._name,
			'angle': self._angle,
			'ranking': self._ranking,
			'bool_use': self._bool_use,
			'default_orb': self._default_orb,
			'color': self._color,
			'glyph': self._glyph,
			'comment': self._comment}
	
	def _to_xml(self, with_idx=False):
		"""Return aspects as xmlutils.Element('Aspect').
		
		:rtype: xmlutils.Element
		"""
		if with_idx:
			el = xmlutils.Element('Aspect', {'_idx': self._idx_}, '\n\t', '\n')
		else:
			el = xmlutils.Element('Aspect', {'_idx': None}, '\n\t', '\n')
		el.append('name', {}, self._name, '\n\t')
		el.append('angle', {}, self._angle, '\n\t')
		el.append('ranking', {}, self._ranking, '\n\t')
		el.append('bool_use', {}, self._bool_use, '\n\t')
		el.append('default_orb', {}, self._default_orb, '\n\t')
		el.append('color', {}, self._color, '\n\t')
		el.append('glyph', {}, self._glyph, '\n\t')
		el.append('comment', {}, self._comment, '\n')
		return el
	
	def _from_xml(self, elem, with_idx=False):
		"""Set aspect from a xmlutils.Element('Aspect').
		
		:type elem: xmlutils.Element
		:type with_idx: bool
		"""
		if with_idx:
			_idx = elem.get_attr('_idx')
			if _idx == 'None':
				self._idx_ = None
			else:
				self._idx = _idx
		self.set(name=elem.get_child_text(tag='name').replace('&lt;',
				'<').replace('&gt;', '>'),
			angle=elem.get_child_text(tag='angle'),
			ranking=elem.get_child_text(tag='ranking'),
			bool_use=elem.get_child_text(tag='bool_use'),
			default_orb=elem.get_child_text(tag='default_orb'),
			color=elem.get_child_text(tag='color'),
			glyph=elem.get_child_text(tag='gylph'),
			comment=elem.get_child_text(tag='comment').replace('&lt;',
				'<').replace('&gt;', '>'))
	
	def __eq__(self, other):
		"""Return True if other is the same object in database.
		
		:rtype: bool
		"""
		if not isinstance(other, Aspect):
			return False
		if other._idx_ == self._idx_:
			return True
		return False
	
	def __ne__(self, other):
		"""Return True if other is not the same object in database.
		
		:rtype: bool
		"""
		if not isinstance(other, Aspect):
			return True
		if other._idx_ != self._idx_:
			return True
		return False


class AspectsList(list):
	"""List of aspects objects."""
	
	def __getitem__(self, item):
		if isinstance(item, int):
			return list.__getitem__(self, item)
		for a in self:
			if a._name == item:
				return a
		raise KeyError(item)
	
	def __contains__(self, item):
		for a in self:
			if a._name == item:
				return True
		return False
	
	def get_idx(self, idx):
		for a in self:
			if a._idx_ == idx:
				return a
		raise KeyError(idx)


def all_aspects():
	"""Return a list of all aspect objects in database.
	
	:rtype: AspectsList
	"""
	ret = AspectsList()
	sql = 'select * from Aspects order by ranking, angle;'
	res = db.execute(sql).fetchall()
	for row in res:
		ret.append(Aspect())
		ret[-1].set(*row)
	return ret


def all_aspects_names():
	"""Return a list of all aspects names.
	
	:rtype: list
	"""
	ret = list()
	sql = 'select name from Aspects order by ranking, angle;'
	res = db.execute(sql).fetchall()
	for row in res:
		ret.append(row[0])
	return ret


def xml_export_aspects(with_idx=False):
	"""Return a xmlutils.Element('Aspects') containing all aspects.
	
	:type with_idx: bool
	:rtype: xmlutils.Element
	"""
	all = all_aspects()
	el = xmlutils.Element('Aspects', {}, '\n', '\n')
	for a in all:
		el.append(a._to_xml(with_idx=with_idx))
	return el


def xml_import_aspects(elem, with_idx=False):
	"""Return a list of aspects from a xmlutils.Element('Aspects').
	
	:type elem: xmlutils.Element
	:type with_idx: bool
	:rtype: AspectsList
	"""
	ret = AspectsList()
	for a in elem.get_iterator('Aspect'):
		ret.append(Aspect())
		ret[-1]._from_xml(a, with_idx=_with_idx)
	return ret



def _test():
	import doctest
	doctest.testmod()


if __name__ == "__main__":
	_test()

# End.
