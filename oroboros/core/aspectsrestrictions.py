#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Aspects restrictions (list of all planets associated with a boolean).

Aspects are calculated only if both planets are set to True. Usefull if you
need some planet displayed but not aspected.

Create an aspects restrictions filter.

	>>> ar = AspectsRestrictions()
	>>> ar.set(name='foobar')

Filter details.

	>>> ar['Sun']
	True
	>>> ar['Chiron'] = False
	>>> 'Mayakowski' in ar
	False

Save, update, delete filter.

	>>> ar.save()
	>>> ar
	AspectsRestrictions('''foobar''')
	>>> ar['Moon'] = False
	>>> ar.save()
	>>> ar.delete()

Search functions.

	>>> all_aspects_restrictions
	[AspectsRestrictions('''<Planets-Aspects Filter 1>''')]

"""

from oroboros.core import db
from oroboros.core import xmlutils


__all__ = ['AspectsRestrictions', 'AspectsRestrictionsList',
	'all_aspects_restrictions', 'all_aspects_restrictions_names',
	'xml_export_aspects_restrictions', 'xml_import_aspects_restrictions']


class AspectsRestrictions(db.Object):
	"""Aspects restrictions filter type."""
	
	__slots__ = ('_idx_', '_name', '_comment', '_dict_')
	
	def _get_name(self):
		"""Get filter name.
		
		:rtype: str
		"""
		return self._name
	
	def _set_name(self, name):
		"""Set filter name.
		
		:type name: str
		"""
		self._name = name
	
	def _get_comment(self):
		"""Get filter comment.
		
		:rtype: str
		"""
		return self._comment
	
	def _set_comment(self, comment):
		"""Set filter comment.
		
		:type comment: str
		"""
		self._comment = comment
	
	def _get_dict(self):
		"""Return internal dict of planets.
		
		:rtype: dict
		"""
		return self._dict_
	
	def _set_dict(self, res):
		"""Set internal dict of planets (with db result rows).
		
		:type res: sequence
		"""
		self._dict_.clear()
		for x, y in res:
			if y in (True, '1', 1, 'True', 'true'):
				y = True
			else:
				y = False
			self._dict_[x] = y
	
	_idx = property(db.Object._get_idx, db.Object._set_idx,
		doc="Aspects restrictions filter db index value.")
	name = property(_get_name, _set_name,
		doc="Aspects restrictions filter name.")
	comment = property(_get_comment, _set_comment,
		doc="Aspects restrictions filter comment.")
	_dict = property(_get_dict, _set_dict,
		doc="Aspects restrictions filter internal dict.")
	
	def set(self, _idx=None, name=None, comment=None):
		"""Set filter properties.
		
		Args: 'name', 'comment'
		
		"""
		if _idx != None:
			self._idx = _idx
		if name != None:
			self.name = name
		if comment != None:
			self.comment = comment
	
	def __init__(self, filt=None, set_default=True):
		"""Aspects restrictions initialization.
		
		:type filt: int or str or None
		:type set_default: bool
		"""
		self._dict_ = dict()
		if filt != None:
			return self._select(filt)
		else:
			self._idx_ = None
			self._name = str()
			self._comment = str()
			if set_default:
				self.set_default()
	
	def set_default(self):
		"""Reset restrictions to default values."""
		sql = "select name, bool_aspect from Planets;"
		res = db.execute(sql)
		self._set_dict(res)
	
	def reset(self):
		"""Reset filter when database is updated.
		
		Filter may have been deleted, then load the default one.
		
		"""
		try:
			self._select_by_idx(self._idx_)
		except ValueError: # filter deleted
			sql = '''select asprestr from Filters
				where _idx = (select dft_filter from Config);'''
			idx = int(db.execute(sql).fetchone()[0])
			self._select_by_idx(idx)
	
	def _select(self, filt):
		"""Select aspects restrictions in database.
		
		:raise TypeError: invalid filter
		"""
		if isinstance(filt, int):
			return self._select_by_idx(filt)
		elif isinstance(filt, basestring): # str in py3
			return self._select_by_name(filt)
		raise TypeError('Invalid filter %s.' % filt)
	
	def _select_by_idx(self, idx):
		"""Select aspects restrictions in database, by idx.
		
		:raise ValueError: not found
		"""
		sql = "select * from AspectsRestrictions where _idx = ?;"
		res = db.execute(sql, (idx,)).fetchall()
		if len(res) == 0:
			raise ValueError('Invalid idx %s.' % idx)
		self.set(*res[0])
		self._select_dict()
	
	def _select_by_name(self, filt):
		"""Select aspects restrictions filter in database, by name.
		
		:raise ValueError: not found
		"""
		sql = "select * from AspectsRestrictions where name = ?;"
		res = db.execute(sql, (filt,)).fetchall()
		if len(res) == 0:
			raise ValueError('Invalid filter %s.' % filt)
		self.set(*res[0])
		self._select_dict()
	
	def _select_dict(self):
		"""Select filter dict in database, with filter idx."""
		sql = """select A.name, B.bool_asp from Planets as A,
		_AspectsRestrictions as B where B.filter_idx = ? and A._idx =
		B.planet_idx;"""
		res = db.execute(sql, (self._idx_,)).fetchall()
		self._set_dict(res)
	
	def save(self):
		"""Save aspects restrictions in database."""
		if self._idx_ == None:
			self._insert()
		else:
			self._update()
	
	def _insert(self):
		"""Insert aspects restrictions in database.
		
		:raise ValueError: duplicate
		"""
		sql1 = "insert into AspectsRestrictions (name, comment) values (?, ?);"
		sql2 = "select _idx from AspectsRestrictions where name = ?;"
		try:
			db.execute(sql1, (self._name, self._comment))
		except: # sqlite3.IntegrityError
			raise ValueError('Duplicate filter %s.' % self._name)
		self._idx = db.execute(sql2, (self._name,)).fetchone()[0]
		self._save_dict()
	
	def _update(self):
		"""Update aspects restrictions filter in database.
		
		:raise ValueError: duplicate
		"""
		sql = """update AspectsRestrictions set name = ?, comment = ?
			where _idx = ?;"""
		try:
			db.execute(sql, (self._name, self._comment, self._idx_))
		except: # integrity error
			raise ValueError('Duplicate filter %s.' % self._name)
		self._save_dict()
	
	def delete(self):
		"""Delete aspects restrictions in database.
		
		:raise TypeError: invalid index
		:raise ValueError: integrity error
		"""
		if self._idx_ == None:
			raise TypeError('Missing idx.')
		sql = "delete from AspectsRestrictions where _idx = ?;"
		try:
			db.execute(sql, (self._idx_,))
		except: # integrity error
			raise ValueError('Cannot delete default filter')
		self._idx_ = None
	
	def _save_dict(self):
		"""Save aspects restrictions dict in database (with filter idx)."""
		self._delete_dict()
		sql = """insert into _AspectsRestrictions select ?, _idx, ? from
			Planets where name = ?;"""
		for plt, val in self.items():
			db.execute(sql, (self._idx_, int(val), plt))
	
	def _delete_dict(self):
		"""Delete aspects restrictions dict in database."""
		sql = "delete from _AspectsRestrictions where filter_idx = ?;"
		db.execute(sql, (self._idx_,))
	
	def __len__(self):
		"""Return number of planets in aspects restrictions.
		
		:rtype: int
		"""
		return len(self._dict_)
	
	def __getitem__(self, key):
		"""Return boolean (aspected) identified by planet name.
		
		:type key: str
		:rtype: bool
		"""
		return self._dict_[key]
	
	def __setitem__(self, key, value=False):
		"""Set planet aspected, identified by planet name.
		
		:type key: str
		:type value: bool
		:raise KeyError: not found
		"""
		for plt in self._dict_:
			if plt == key:
				if value in (True, 1, 'True', '1', 'true'):
					value = True
				else:
					value = False
				self._dict_[plt] = value
				return
		raise KeyError(key)
	
	def __contains__(self, key):
		"""Return True if planet name is in aspects restrictions.
		
		:rtype: bool
		"""
		return self._dict_.__contains__(key)
	
	def __iter__(self):
		"""Return iterator over aspects restrictions keys.
		
		:rtype: iterator
		"""
		return self._dict_.__iter__()
	
	def keys(self):
		"""Return a list of aspects restrictions keys.
		
		:rtype: list
		"""
		return self._dict_.keys()
	
	def values(self):
		"""Return a list of aspects restrictions values."""
		return self._dict_.values()
	
	def items(self):
		"""Return a list of restrictions key, value tuples.
		
		:rtype: list
		"""
		return self._dict_.items()
	
	def get(self, key, default=None):
		"""Return boolean (aspected), identified by key (planet name).
		
		Return default (None) if aspect not found.
		
		:type key: str
		:type default: any
		:rtype: bool or default
		"""
		got = self.__getitem__(key)
		if got == None:
			return default
		return got
	
	def __str__(self):
		"""Return aspects restrictions as string.
		
		:rtype: str
		"""
		return str(tuple(x for x in (self._idx_, self._name, self._comment,
			self._dict_)))
	
	def __repr__(self):
		if self._idx_ == None:
			return repr(tuple(repr(x) for x in self))
		return "AspectsRestrictions('''%s''')" % self._name
	
	def __getstate__(self):
		return {'_idx': None,
			'name': self._name,
			'comment': self._comment,
			'_dict': self._dict_}
	
	def _to_xml(self, with_idx=False):
		"""Return a xmlutils.Element('AspectsRestrictions').
		
		:type with_idx: bool
		:rtype: xmlutils.Element
		"""
		if with_idx:
			el = xmlutils.Element('PlanetsAspectsFilter', {'_idx': self._idx_},
				'\n\t', '\n')
		else:
			el = xmlutils.Element('PlanetsAspectsFilter', {'_idx': None},
				'\n\t', '\n')
		el.append('name', {}, self._name, '\n\t')
		el.append('comment', {}, self._comment, '\n\t')
		el2 = xmlutils.Element('Planets', {}, '\n\t\t', '\n')
		for x, y in self.items():
			el2.append('Planet', {'name': x, 'value': y}, '', '\n\t\t')
		el.append(el2)
		return el
	
	def _from_xml(self, elem, with_idx=False):
		"""Set restrictions from a xmlutils.Element('AspectsRestrictions').
		
		:type elem: xmlutils.Element
		:type with_idx: bool
		"""
		if with_idx:
			_idx = elem.get_attr('_idx')
			if _idx == 'None':
				self._idx_ = None
			else:
				self._idx = _idx
		self.set(name=elem.get_child_text(
				tag='name').replace('&lt;', '<').replace('&gt;', '>'),
			comment=elem.get_child_text(
				tag='comment').replace('&lt;', '<').replace('&gt;', '>'))
		el2 = elem.get_child('Planets')
		for e in el2.get_iterator(tag='Planet'):
			self[e.get_attr('name')] = e.get_attr('value')
	
	def __eq__(self, other):
		"""Return True if other is the same filter in database.
		
		:rtype: bool
		"""
		if other == None:
			return False
		if not isinstance(other, AspectsRestrictions):
			return False
		if other._idx_ == self._idx_:
			return True
		return False
	
	def __ne__(self, other):
		"""Return True if other is not the same filter in database.
		
		:rtype: bool
		"""
		if other == None:
			return True
		if not isinstance(other, AspectsRestrictions):
			return True
		if other._idx_ != self._idx_:
			return True
		return False


class AspectsRestrictionsList(list):
	"""Aspects restrictions list object."""
	
	def __getitem__(self, item):
		if isinstance(item, int):
			return list.__getitem__(self, item)
		for ar in self:
			if ar._name == item:
				return ar
		raise KeyError(item)
	
	def __contains__(self, item):
		for ar in self:
			if ar._name == item:
				return True
		return False
	
	def get_idx(self, idx):
		for ar in self:
			if ar._idx_ == idx:
				return ar
		raise KeyError(idx)


def all_aspects_restrictions():
	"""Get list of all aspects restrictions objects.
	
	:rtype: AspectsRestrictionsList
	"""
	ret = AspectsRestrictionsList()
	sql = "select * from AspectsRestrictions order by name;"
	res = db.execute(sql).fetchall()
	for row in res:
		ret.append(AspectsRestrictions(set_default=False))
		ret[-1].set(*row)
		ret[-1]._select_dict()
	return ret


def all_aspects_restrictions_names():
	"""Return a list of all aspects restrictions names.
	
	:rtype: list
	"""
	ret = list()
	sql = 'select name from AspectsRestrictions order by name;'
	res = db.execute(sql).fetchall()
	for row in res:
		ret.append(row[0])
	return ret


def xml_export_aspects_restrictions():
	"""Return a xmlutils.Element('AllAspectsRestrictions').
	
	:rtype: xmlutils.Element
	"""
	all = all_aspects_restrictions()
	el = xmlutils.Element('AllAspectsRestrictions', {}, '\n', '\n')
	for a in all:
		el.append(a._to_xml())
	return el


def xml_import_aspects_restrictions(elem, with_idx=False):
	"""Return a list of aspects restr. from a xmlutils.Element('AllAspectsRestrictions').
	
	:type elem: xmlutils.Element
	:type with_idx: bool
	:rtype: AspectsRestrictionsList
	"""
	ret = AspectsRestrictionsList()
	for a in elem.get_iterator('AspectsRestrictions'):
		ret.append(AspectsRestrictions(set_default=False))
		ret[-1]._from_xml(a, with_idx=with_idx)
	return ret



def _test():
	import doctest
	doctest.testmod()


if __name__ == "__main__":
	_test()

# End.
