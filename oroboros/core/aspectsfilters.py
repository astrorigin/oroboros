#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Aspects filters (list of all aspects with an associated boolean value).

Create a new aspects filter.

	>>> af = AspectsFilter()
	>>> af.name = 'Main aspects'

Filters details.

	>>> af['Conjunction'] # usage set to conjunction
	True
	>>> af['Undecile']
	False
	>>> 'Square' in af # square aspect does exist ?
	True
	>>> 'Quintunovariadecile' in af
	False
	>>> af['Trine'] = False

Insert, update, delete aspects filter.

	>>> af.save()
	>>> af
	AspectsFilter('''Main aspects''')
	>>> af['Opposition'] = False
	>>> af.save()
	>>> af.delete()

Search functions.

	>>> all_aspects_filters
	[AspectsFilter('''<Aspects Filter 1>''')]

Load filter.

	>>> af = AspectsFilter('<Aspects Filter 1>')
	>>> print(af)
	[1, u'<Aspects Filter 1>', u'Example Aspects Filter.', {u'SemiQuintile': False, u'BiQuintile': False, u'Septile': False, u'Trine': True, u'BiNovile': False, u'Conjunction': True, u'SquiSextile': True, u'Opposition': True, u'SquiSquare': True, u'Quincunx': True, u'SemiNovile': False, u'SemiSquare': True, u'QuinUndecile': False, u'TriSeptile': False, u'Undecile': False, u'Quintile': False, u'SesquiSquare': True, u'QuadUndecile': False, u'Novile': False, u'Square': True, u'QuatroNovile': False, u'BiUndecile': False, u'SemiSextile': True, u'Sextile': True, u'BiSeptile': False, u'TriUndecile': False}, None]

"""

from oroboros.core import db
from oroboros.core import xmlutils


__all__ = ['AspectsFilter', 'AspectsFiltersList',
	'all_aspects_filters', 'all_aspects_filters_names',
	'xml_export_aspects_filters', 'xml_import_aspects_filters']


class AspectsFilter(db.Object):
	"""Aspects filter type."""
	
	__slots__ = ('_idx_', '_name', '_comment', '_dict_')
	
	def _get_name(self):
		"""Get aspects filter name."""
		return self._name
	
	def _set_name(self, name):
		"""Set aspects filter name."""
		self._name = name
	
	def _get_comment(self):
		"""Get aspects filter comment."""
		return self._comment
	
	def _set_comment(self, comment):
		"""Set aspects filter comment."""
		self._comment = comment
	
	def _get_dict(self):
		"""Get internal dict of aspects."""
		return self._dict_
	
	def _set_dict(self, res):
		"""Set internal dict of aspects (with db result rows)."""
		self._dict_.clear()
		for x, y in res:
			if y in (True, '1', 1, 'True', 'true', 'yes'):
				y = True
			else:
				y = False
			self._dict_[x] = y
	
	_idx = property(db.Object._get_idx, db.Object._set_idx,
		doc="Aspects filter db index value.")
	name = property(_get_name, _set_name,
		doc="Aspects filter name.")
	comment = property(_get_comment, _set_comment,
		doc="Aspects filter comment.")
	_dict = property(_get_dict, _set_dict,
		doc="Aspects filter internal dict.")
	
	def set(self, _idx=None, name=None, comment=None):
		"""Set aspects filter properties.
		
		:type name: str
		:type comment: str
		"""
		if _idx != None:
			self._idx = _idx
		if name != None:
			self.name = name
		if comment != None:
			self.comment = comment
	
	def __init__(self, filt=None, set_default=True):
		"""Aspects filter initialization."""
		self._dict_ = dict()
		if filt != None:
			return self._select(filt)
		else:
			self._idx_ = None
			self._name = ''
			self._comment = ''
			if set_default:
				self.set_default()
	
	def set_default(self):
		"""Reset aspects filter to default values."""
		sql = "select name, bool_use from Aspects;"
		res = db.execute(sql)
		self._set_dict(res)
	
	def reset(self):
		"""Reset filter when database is updated.
		
		The filter may have been deleted, then load the default one.
		
		"""
		try:
			self._select_by_idx(self._idx_)
		except ValueError: # filter deleted
			sql = '''select aspects from Filters
				where _idx = (select dft_filter from Config);'''
			idx = int(db.execute(sql).fetchone()[0])
			self._select_by_idx(idx)
	
	def _select(self, filt):
		"""Select aspects filter in database.
		
		:raise TypeError: invalid filter
		"""
		if isinstance(filt, int):
			return self._select_by_idx(filt)
		elif isinstance(filt, basestring):
			return self._select_by_name(filt)
		raise TypeError('Invalid filter %s.' % filt)
	
	def _select_by_idx(self, idx):
		"""Select aspects filter in database, by idx.
		
		:raise ValueError: not found
		"""
		sql = "select * from AspectsFilters where _idx = ?;"
		res = db.execute(sql, (idx,)).fetchall()
		if len(res) == 0:
			raise ValueError('Invalid idx %s.' % idx)
		self.set(*res[0])
		self._select_dict()
	
	def _select_by_name(self, filt):
		"""Select aspects filter in database, by name.
		
		:raise ValueError: not found
		"""
		sql = "select * from AspectsFilters where name = ?;"
		res = db.execute(sql, (filt,)).fetchall()
		if len(res) == 0:
			raise ValueError('Invalid filter %s.' % filt)
		self.set(*res[0])
		self._select_dict()
	
	def _select_dict(self):
		"""Select aspects filters dict in database, with filter idx."""
		sql = """select A.name, B.bool_use from Aspects as A, _AspectsFilters
			as B where B.filter_idx = ? and A._idx = B.aspect_idx;"""
		res = db.execute(sql, (self._idx_,)).fetchall()
		self._set_dict(res)
	
	def save(self):
		"""Save aspects filter in database."""
		if self._idx_ == None:
			self._insert()
		else:
			self._update()
	
	def _insert(self):
		"""Insert aspects filter in database.
		
		:raise ValueError: duplicate
		"""
		sql1 = "insert into AspectsFilters (name, comment) values (?, ?);"
		sql2 = "select _idx from AspectsFilters where name = ?;"
		try:
			db.execute(sql1, (self._name, self._comment))
		except: # sqlite3.IntegrityError
			raise ValueError('Duplicate filter %s.' % self._name)
		self._idx = db.execute(sql2,(self._name,)).fetchone()[0]
		self._save_dict()
	
	def _update(self):
		"""Update aspects filter in database."""
		sql = "update AspectsFilters set name = ?, comment = ? where _idx = ?;"
		db.execute(sql, (self._name, self._comment, self._idx_))
		self._save_dict()
	
	def _save_dict(self):
		"""Save aspects filter dict in database (with filter idx)."""
		self._delete_dict()
		sql = """insert into _AspectsFilters select ?, _idx, ? from Aspects
			where name = ?;"""
		for asp, val in self._dict_.items():
			db.execute(sql, (self._idx_, int(val), asp))
	
	def delete(self):
		"""Delete aspects filter in database.
		
		:raise TypeError: invalid index
		:raise ValueError: integrity error
		"""
		if self._idx_ == None:
			raise TypeError('Missing idx.')
		sql = "delete from AspectsFilters where _idx = ?;"
		try:
			db.execute(sql, (self._idx_,))
		except: # integrity error
			raise ValueError('Cannot delete default filter.')
		self._idx_ = None
	
	def _delete_dict(self):
		"""Delete aspects filter dict in database."""
		sql = "delete from _AspectsFilters where filter_idx = ?;"
		db.execute(sql, (self._idx_,))
	
	def __len__(self):
		"""Return number of elements in aspects filter.
		
		:rtype: int
		"""
		return len(self._dict_)
	
	def __getitem__(self, key):
		"""Return boolean (aspect usage) identified by aspect name.
		
		:raise KeyError: not found
		:rtype: bool
		"""
		return self._dict_[key]
	
	def __setitem__(self, key, value=False):
		"""Set aspect usage (boolean), identified by aspect name.
		
		:raise KeyError: not found
		"""
		for asp in self._dict_:
			if asp == key:
				if value in (True, 1, 'True', '1', 'true'):
					value = True
				else:
					value = False
				self._dict_[asp] = value
				return
		raise KeyError(key)
	
	def __contains__(self, key):
		"""Return True if aspect name is in aspects filter.
		
		:rtype: bool
		"""
		return self._dict_.__contains__(key)
	
	def __iter__(self):
		"""Return iterator over aspects filter keys.
		
		:rtype: iterator
		"""
		return self._dict_.__iter__()
	
	def keys(self):
		"""Return a list of aspects filter keys.
		
		:rtype: list
		"""
		return self._dict_.keys()
	
	def values(self):
		"""Return a list of aspects filter values.
		
		:rtype: list
		"""
		return self._dict_.values()
	
	def items(self):
		"""Return a list of aspects filter key, value tuples.
		
		:rtype: list
		"""
		return self._dict_.items()
	
	def get(self, key, default=None):
		"""Return boolean (aspect usage), identified by key (aspect name).
		
		Return default (None) if aspect not found.
		
		:rtype: bool
		"""
		got = self.__getitem__(key)
		if got == None:
			return default
		return got
	
	def __str__(self):
		"""Show aspects filter internals.
		
		:rtype: str
		"""
		return str(tuple(x for x in (self._idx_, self._name, self._comment,
			self._dict_)))
	
	def __repr__(self):
		if self._idx_ == None:
			return repr(tuple(repr(x) for x in self))
		return "AspectsFilter('''%s''')" % self._name
	
	def __getstate__(self):
		return {'_idx': None,
			'name': self._name,
			'comment': self._comment,
			'_dict': self._dict_}
	
	def _to_xml(self, with_idx=False):
		"""Return a xmlutils.Element('AspecstFilter').
		
		:type with_idx: bool
		:rtype: xmlutils.Element
		"""
		if with_idx:
			el = xmlutils.Element('AspectsFilter', {'_idx': self._idx_},
				'\n\t', '\n')
		else:
			el = xmlutils.Element('AspectsFilter', {'_id': None}, '\n\t', '\n')
		el.append('name', {}, self._name, '\n\t')
		el.append('comment', {}, self._comment, '\n\t')
		el2 = xmlutils.Element('Aspects', {}, '\n\t\t', '\n')
		for x, y in self.items():
			el2.append('Aspect', {'name': x, 'value': y}, '', '\n\t\t')
		el.append(el2)
		return el
	
	def _from_xml(self, elem, with_idx=False):
		"""Set aspects filter from a xmlutils.Element('AspectsFilter').
		
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
		"""Return True if other is the same aspects filter in database.
		
		:rtype: bool
		"""
		if other == None:
			return False
		if not isinstance(other, AspectsFilter):
			return False
		if other._idx_ == self._idx_:
			return True
		return False
	
	def __ne__(self, other):
		"""Return True if other is not the same aspects filter in database.
		
		:rtype: bool
		"""
		if other == None:
			return True
		if not isinstance(other, AspectsFilter):
			return True
		if other._idx_ != self._idx_:
			return True
		return False


class AspectsFiltersList(list):
	"""Aspects filters list object."""
	
	def __getitem__(self, item):
		if isinstance(item, int):
			return list.__getitem__(self, item)
		for af in self:
			if af._name == item:
				return af
		raise KeyError(item)
	
	def __contains__(self, item):
		for af in self:
			if af._name == item:
				return True
		return False
	
	def get_idx(self, idx):
		for af in self:
			if af._idx_ == idx:
				return af
		raise KeyError(idx)


def all_aspects_filters():
	"""Return a list of all aspects filters.
	
	:rtype: AspectsFiltersList
	"""
	ret = AspectsFiltersList()
	sql = "select * from AspectsFilters order by name;"
	res = db.execute(sql).fetchall()
	for row in res:
		ret.append(AspectsFilter(set_default=False))
		ret[-1].set(*row)
		ret[-1]._select_dict()
	return ret


def all_aspects_filters_names():
	"""Return a list of all aspects filters names.
	
	:rtype: list
	"""
	ret = list()
	sql = 'select name from AspectsFilters order by name;'
	res = db.execute(sql).fetchall()
	for row in res:
		ret.append(row[0])
	return ret


def xml_export_aspects_filters():
	"""Return a xmlutils.Element('AspectsFilters') with all aspects filters.
	
	:rtype: xmlutils.Element
	"""
	all = all_aspects_filters()
	el = xmlutils.Element('AspectsFilters', {}, '\n', '\n')
	for a in all:
		el.append(a._to_xml())
	return el


def xml_import_aspects_filters(elem, with_idx=False):
	"""Return a list of aspects filters from a xmlutils.Element('AspectsFilters').
	
	:type elem: xmlutils.Element
	:type with_idx: bool
	:rtype: AspectsFiltersList
	"""
	ret = AspectsFiltersList()
	for a in elem.get_iterator('AspectsFilter'):
		ret.append(AspectsFilter(set_default=False))
		ret[-1]._from_xml(a, with_idx=with_idx)
	return ret



def _test():
	import doctest
	doctest.testmod()


if __name__ == "__main__":
	_test()

# End.
