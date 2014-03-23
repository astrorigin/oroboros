#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Orbs filters (list of all aspects associated with orbs values).
	
	Create a new orbs filter.
	
		>>> of = OrbsFilter()
		>>> of.set(name='Tight orbs')
		>>> of['Trine']
		Orb("8.0")
		>>> 'some aspect' in of
		False
	
	Insert, update, delete orbs filter.
	
		>>> of.save()
		>>> of
		OrbsFilter('''Tight orbs''')
		>>> of['Conjunction'] = 5
		>>> of['Conjunction']
		Orb("5.0")
		>>> of.save()
		>>> of.delete()
	
	Search functions.
	
		>>> all_orbs_filters
		[OrbsFilter('''<Orbs Filter 1>''')]
	
	Load filter.
	
		>>> of = OrbsFilter('<Orbs Filter 1>')
		>>> print(of)
		[1, u'<Orbs Filter 1>', u'Example Orbs Filter.', {u'SemiQuintile': oroboros.orbs.Orb("1.0"), u'BiQuintile': oroboros.orbs.Orb("1.0"), u'Septile': oroboros.orbs.Orb("1.0"), u'Trine': oroboros.orbs.Orb("8.0"), u'BiNovile': oroboros.orbs.Orb("1.0"), u'Conjunction': oroboros.orbs.Orb("10.0"), u'SquiSextile': oroboros.orbs.Orb("1.0"), u'Opposition': oroboros.orbs.Orb("10.0"), u'SquiSquare': oroboros.orbs.Orb("1.0"), u'Quincunx': oroboros.orbs.Orb("4.0"), u'SemiNovile': oroboros.orbs.Orb("1.0"), u'SemiSquare': oroboros.orbs.Orb("2.0"), u'QuinUndecile': oroboros.orbs.Orb("1.0"), u'TriSeptile': oroboros.orbs.Orb("1.0"), u'Undecile': oroboros.orbs.Orb("1.0"), u'Quintile': oroboros.orbs.Orb("1.0"), u'SesquiSquare': oroboros.orbs.Orb("2.0"), u'QuadUndecile': oroboros.orbs.Orb("1.0"), u'Novile': oroboros.orbs.Orb("1.0"), u'Square': oroboros.orbs.Orb("8.0"), u'QuatroNovile': oroboros.orbs.Orb("1.0"), u'BiUndecile': oroboros.orbs.Orb("1.0"), u'SemiSextile': oroboros.orbs.Orb("2.0"), u'Sextile': oroboros.orbs.Orb("4.0"), u'BiSeptile': oroboros.orbs.Orb("1.0"), u'TriUndecile': oroboros.orbs.Orb("1.0")}, None]

"""

from oroboros.core import db
from oroboros.core.orbs import Orb
from oroboros.core import xmlutils


__all__ = ['OrbsFilter', 'OrbsFiltersList',
	'all_orbs_filters', 'all_orbs_filters_names',
	'xml_export_orbs_filters', 'xml_import_orbs_filters']


class OrbsFilter(db.Object):
	"""Orbs filter type."""
	
	__slots__ = ('_idx_', '_name', '_comment', '_dict_')
	
	def _get_name(self):
		"""Get orbs filter name.
		
		:rtype: str
		"""
		return self._name
	
	def _set_name(self, name):
		"""Set orbs filter name.
		
		:type name: str
		"""
		self._name = name
	
	def _get_comment(self):
		"""Get orbs filter comment.
		
		:rtype: comment
		"""
		return self._comment
	
	def _set_comment(self, comment):
		"""Set orbs filter comment.
		
		:type comment: str
		"""
		self._comment = comment
	
	def _get_dict(self):
		"""Return internal dict of aspects.
		
		:rtype: dict
		"""
		return self._dict_
	
	def _set_dict(self, res):
		"""Set internal dict of aspects (with db result rows).
		
		:type res: sequence
		"""
		self._dict_.clear()
		for x, y in res:
			self._dict_[x] = Orb(y)
	
	def set(self, _idx=None, name=None, comment=None):
		"""Set orbs filter properties.
		
		Args: 'name', 'comment'
		
		"""
		if _idx != None:
			self._idx = _idx
		if name != None:
			self.name = name
		if comment != None:
			self.comment = comment
	
	_idx = property(db.Object._get_idx, db.Object._set_idx,
		doc="Orbs filter db index value.")
	name = property(_get_name, _set_name,
		doc="Orbs filter name.")
	comment = property(_get_comment, _set_comment,
		doc="Orbs filter comment.")
	_dict = property(_get_dict, _set_dict,
		doc="Orbs filter internal dict.")
	
	def __init__(self, filt=None, set_default=True):
		"""Orbs filter initialization.
		
		:type filt: str or int or None
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
		"""Reset orbs filter to default values."""
		sql = "select name, default_orb from Aspects;"
		res = db.execute(sql)
		self._set_dict(res)
	
	def reset(self):
		"""Reset filter when database is updated.
		
		Filter may have been deleted, then load the default one.
		
		"""
		try:
			self._select_by_idx(self._idx_)
		except ValueError: # filter deleted
			sql = '''select orbs from Filters
				where _idx = (select dft_filter from Config);'''
			idx = int(db.execute(sql).fetchone()[0])
			self._select_by_idx(idx)
	
	def _select(self, filt):
		"""Select orbs filter in database.
		
		:type filt: str or int
		:raise TypeError: invalid filter
		"""
		if isinstance(filt, int):
			return self._select_by_idx(filt)
		elif isinstance(filt, basestring): # str in py3
			return self._select_by_name(filt)
		raise TypeError('Invalid filter %s.' % filt)
	
	def _select_by_idx(self, idx):
		"""Select orbs filter by idx.
		
		:type idx: int
		:raise ValueError: not found
		"""
		sql = "select * from OrbsFilters where _idx = ?;"
		res = db.execute(sql, (idx,)).fetchall()
		if len(res) == 0:
			raise ValueError('Invalid idx %s.' % idx)
		self.set(*res[0])
		self._select_dict()
	
	def _select_by_name(self, filt):
		"""Select orbs filter by name.
		
		:type filt: str
		:raise ValueError: not found
		"""
		sql = "select * from OrbsFilters where name = ?;"
		res = db.execute(sql, (filt,)).fetchall()
		if len(res) == 0:
			raise ValueError('Invalid filter %s.' % filt)
		self.set(*res[0])
		self._select_dict()
	
	def _select_dict(self):
		"""Select orbs filters dict in database, with orbs filter idx."""
		sql = """select A.name, B.orb from Aspects as A, _OrbsFilters as B
			where B.filter_idx = ? and A._idx = B.aspect_idx;"""
		res = db.execute(sql, (self._idx_,)).fetchall()
		self._set_dict(res)
	
	def save(self):
		"""Save orbs filter in database."""
		if self._idx_ == None:
			self._insert()
		else:
			self._update()
	
	def _insert(self):
		"""Insert new orbs filter in database.
		
		:raise ValueError: duplicate
		"""
		sql1 = "insert into OrbsFilters (name, comment) values (?, ?);"
		sql2 = "select _idx from OrbsFilters where name = ?;"
		try:
			db.execute(sql1, (self._name, self._comment))
		except: # sqlite3.IntegrityError
			raise ValueError('Duplicate filter %s.' % self._name)
		self._idx = db.execute(sql2, (self._name,)).fetchone()[0]
		self._save_dict()
	
	def _update(self):
		"""Update orbs filter in database.
		
		:raise ValueError: duplicate
		"""
		sql = "update OrbsFilters set name = ?, comment = ? where _idx = ?;"
		try:
			db.execute(sql, (self._name, self._comment, self._idx_))
		except:
			raise ValueError('Duplicate filter %s.' % self._name)
		self._save_dict()
	
	def delete(self):
		"""Delete orbs filter in database (by idx).
		
		:raise TypeError: invalid index
		:raise ValueError: integrity error
		"""
		if self._idx_ == None:
			raise TypeError('Missing idx.')
		sql = "delete from OrbsFilters where _idx = ?;"
		try:
			db.execute(sql, (self._idx_,))
		except: # integrity error
			raise ValueError('Cannot delete default filter.')
		self._idx_ = None
	
	def _save_dict(self):
		"""Save orbs filter dict in database (with filter idx)."""
		self._delete_dict()
		sql = """insert into _OrbsFilters select ?, _idx, ? from Aspects
			where name = ?;"""
		for asp, val in self.items():
			db.execute(sql, (self._idx_, float(val), asp))
	
	def _delete_dict(self):
		"""Delete orbs filter dict in database."""
		sql = "delete from _OrbsFilters where filter_idx = ?;"
		db.execute(sql, (self._idx_,))
	
	def __len__(self):
		"""Return number of aspects in orbs filter.
		
		:rtype: int
		"""
		return len(self._dict_)
	
	def __getitem__(self, key):
		"""Return orb, identified by aspect name.
		
		:type key: str
		:raise KeyError: not found
		"""
		return self._dict_[key]
	
	def __setitem__(self, key, value):
		"""Set aspect orb, identified by aspect name.
		
		:type key: str
		:type value: numeric
		:raise KeyError: not found
		"""
		for asp in self._dict_.iterkeys():
			if asp == key:
				self._dict_[asp] = Orb(value)
				return
		raise KeyError(key)
	
	def __contains__(self, key):
		"""Return True if aspect name is in orbs filter.
		
		:rtype: bool
		"""
		return self._dict_.__contains__(key)
	
	def __iter__(self):
		"""Return iterator over orbs filter keys.
		
		:rtype: iterator
		"""
		return self._dict_.__iter__()
	
	def keys(self):
		"""Return a list of orbs filter keys.
		
		:rtype: list
		"""
		return self._dict_.keys()
	
	def values(self):
		"""Return a list of orbs filter values.
		
		:rtype: list
		"""
		return self._dict_.values()
	
	def items(self):
		"""Return a list of orbs filter key, value tuples.
		
		:rtype: list
		"""
		return self._dict_.items()
	
	def get(self, key, default=None):
		"""Return Orb, identified by key (aspect name).
		
		Return default (None) if aspect not found.
		
		:type key: str
		:type default: any
		:rtype: Orb
		"""
		got = self.__getitem__(key)
		if got == None:
			return default
		return got
	
	def __str__(self):
		"""Show orbs filter internals."""
		return str(tuple(x for x in (self._idx_, self._name, self._comment,
			self._dict_)))
	
	def __repr__(self):
		if self._idx_ == None:
			return repr(tuple(repr(x) for x in self))
		return "OrbsFilter('''%s''')" % self._name
	
	def __getstate__(self):
		return {'_idx': None,
			'name': self._name,
			'comment': self._comment,
			'_dict': self._dict_}
	
	def _to_xml(self, with_idx=False):
		"""Return a xmlutils.Element('OrbsFilter').
		
		:type with_idx: bool
		:rtype: xmlutils.Element
		"""
		if with_idx:
			el = xmlutils.Element('OrbsFilter', {'_idx': self._idx_},
				'\n\t', '\n')
		else:
			el = xmlutils.Element('OrbsFilter', {'_idx': None},
				'\n\t', '\n')
		el.append('name', {}, self._name, '\n\t')
		el.append('comment', {}, self._comment, '\n\t')
		el2 = xmlutils.Element('Aspects', {}, '\n\t\t', '\n')
		for x, y in self.items():
			el2.append('Aspect', {'name': x, 'value': y}, '', '\n\t\t')
		el.append(el2)
		return el
	
	def _from_xml(self, elem, with_idx=False):
		"""Set orbs filter from a xmlutils.Element('OrbsFilter').
		
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
			comment=elem.get_child_text(tag='comment').replace('&lt;',
				'<').replace('&gt;', '>'))
		el2 = elem.get_child('Aspects')
		for e in el2.get_iterator(tag='Aspect'):
			self[e.get_attr('name')] = e.get_attr('value')
	
	def __eq__(self, other):
		"""Return True if other is the same orbs filter in database.
		
		:rtype: bool
		"""
		if other == None:
			return False
		if not isinstance(other, OrbsFilter):
			return False
		if other._idx_ == self._idx_:
			return True
		return False
	
	def __ne__(self, other):
		"""Return True if other is not the same orbs filter in database.
		
		:rtype: bool
		"""
		if other == None:
			return True
		if not isinstance(other, OrbsFilter):
			return True
		if other._idx_ != self._idx_:
			return True
		return False


class OrbsFiltersList(list):
	"""Orbs filters list object."""
	
	def __getitem__(self, item):
		if isinstance(item, int):
			return list.__getitem__(self, item)
		for of in self:
			if of._name == item:
				return of
		raise KeyError(item)
	
	def __contains__(self, item):
		for of in self:
			if of._name == item:
				return True
		return False
	
	def get_idx(self, idx):
		for of in self:
			if of._idx_ == idx:
				return of
		raise KeyError(idx)


def all_orbs_filters():
	"""Return a list of all orbs filters.
	
	:rtype: OrbsFiltersList
	"""
	ret = OrbsFiltersList()
	sql = "select * from OrbsFilters order by name;"
	res = db.execute(sql).fetchall()
	for row in res:
		ret.append(OrbsFilter(set_default=False))
		ret[-1].set(*row)
		ret[-1]._select_dict()
	return ret


def all_orbs_filters_names():
	"""Return a list of all orbs filters names.
	
	:rtype: list
	"""
	ret = list()
	sql = 'select name from OrbsFilters order by name;'
	res = db.execute(sql).fetchall()
	for row in res:
		ret.append(row[0])
	return ret


def xml_export_orbs_filters():
	"""Return a xmlutils.Element('OrbsFilters') with all orbs filters.
	
	:rtype: xmlutils.Element
	"""
	all = all_orbs_filters()
	el = xmlutils.Element('OrbsFilters', {}, '\n', '\n')
	for a in all:
		el.append(a._to_xml())
	return el


def xml_import_orbs_filters(elem):
	"""Return a list of orbs filters from a xmlutils.Element('OrbsFilters').
	
	:type elem: xmlutils.Element
	:rtype: OrbsFiltersList
	"""
	ret = OrbsFiltersList()
	for a in elem.get_iterator('OrbsFilter'):
		ret.append(OrbsFilter(set_default=False))
		ret[-1]._from_xml(a)
	return ret



def _test():
	import doctest
	doctest.testmod()


if __name__ == "__main__":
	_test()

# End.
