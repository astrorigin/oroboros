#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Planets filters (list of all planets with associated boolean value).

	Create a new planets filter.
	
		>>> pf = PlanetsFilter()
		>>> pf.name = 'Sun and main asteroids'
	
	Set filter details.
	
		>>> pf['Sun'] = True
		>>> pf['Moon'] = False
		>>> pf['Pallas'] = True
		>>> pf['Juno'] = True
		>>> pf['Juno'] = True
		>>> pf['Vesta'] = True
	
	Save filter.
	
		>>> pf.save()
	
	Delete filter.
	
		>>> pf.delete()
	
	Get all planets filters.
	
		>>> all_planets_filters
		[PlanetsFilter('''<Planets Filter 1>''')]
	
	Load planets filter.
	
		>>> pf = PlanetsFilter('<Planets Filter 1>')
		>>> print(pf)
		[1, u'<Planets Filter 1>', u'Example Planets Filter.', {u'Mercury': True, u'Rahu (True)': False, u'Admetos': False, u'Cupido': False, u'Sun': True, u'House Cusp 12': False, u'Moon': True, u'House Cusp 11': False, u'House Cusp 10': False, u'Waldemath': False, u'Mars': True, u'Ketu (Mean)': False, u'Armc': False, u'Apollon': False, u'White Moon': False, u'Lilith (Mean)': False, u'Pallas': False, u'Juno': False, u'Chiron': False, u'Zeus': False, u'Vertex': False, u'Pluto': True, u'Vulcan': False, u'Kronos': False, u'Polar Ascendant': False, u'Ketu (True)': False, u'Lilith (True)': False, u'Pluto (Pickering)': False, u'Saturn': True, u'Co-Ascendant (Munkasey)': False, u'Poseidon': False, u'Isis': False, u'Priapus (Mean)': False, u'Neptune (Adams)': False, u'Neptune': True, u'Pholus': False, u'House Cusp 06': False, u'House Cusp 07': False, u'House Cusp 04': False, u'House Cusp 05': False, u'House Cusp 02': False, u'House Cusp 03': False, u'Vesta': False, u'House Cusp 01': False, u'Harrington': False, u'Venus': True, u'Priapus (True)': False, u'Co-Ascendant (Koch)': False, u'Proserpina': False, u'House Cusp 08': False, u'House Cusp 09': False, u'Neptune (Leverrier)': False, u'Ceres': False, u'Part of Fortune': False, u'Nemesis 128': False, u'Pluto (Lowell)': False, u'Nibiru': False, u'Hades': False, u'Rahu (Mean)': False, u'Equatorial Ascendant': False, u'Jupiter': True, u'Uranus': True, u'Vulkanus': False}, None]

"""

from oroboros.core import db
from oroboros.core import xmlutils


__all__ = ['PlanetsFilter', 'PlanetsFiltersList',
	'all_planets_filters', 'all_planets_filters_names',
	'xml_export_planets_filters', 'xml_import_planets_filters']


class PlanetsFilter(db.Object):
	"""Planets filter type."""
	
	__slots__ = ('_idx_', '_name', '_comment', '_dict_')
	
	def _get_name(self):
		"""Get planets filter name.
		
		:rtype: str
		"""
		return self._name
	
	def _set_name(self, name):
		"""Set planets filter name.
		
		:type name: str
		"""
		self._name = name
	
	def _get_comment(self):
		"""Get planets filter comment.
		
		:rtype: str
		"""
		return self._comment
	
	def _set_comment(self, comment):
		"""Set planets filter comment.
		
		:type comment: str
		"""
		self._comment = comment
	
	def _get_dict(self):
		"""Get internal dict.
		
		:rtype: dict
		"""
		return self._dict_
	
	def _set_dict(self, res):
		"""Set internal dict of planets (with db result rows).
		
		:type res: list
		"""
		self._dict_.clear()
		for x, y in res:
			if y in (True, '1', 1, 'True', 'true'):
				y = True
			else:
				y = False
			self._dict_[x] = y
	
	_idx = property(db.Object._get_idx, db.Object._set_idx,
		doc="Planets filter db index value.")
	name = property(_get_name, _set_name,
		doc="Planets filter name.")
	comment = property(_get_comment, _set_comment,
		doc="Planets filter comment.")
	_dict = property(_get_dict, _set_dict,
		doc="Planets filter internal dict.")
	
	def set(self, _idx=None, name=None, comment=None):
		"""Set planets filter properties.
		
		Args: 'name', 'comment'
		
		"""
		if _idx != None:
			self._idx = _idx
		if name != None:
			self.name = name
		if comment != None:
			self.comment = comment
	
	def __init__(self, filt=None, set_default=True):
		"""Planets filter initialization.
		
		:type filt: str or int or None
		:type set_default: bool
		"""
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
		"""Reset planets filter to default values."""
		sql = "select name, bool_use from Planets;"
		res = db.execute(sql)
		self._set_dict(res)
	
	def reset(self):
		"""Reset filter when database is updated.
		
		Filter may have been deleted, then load the default one.
		
		"""
		try:
			self._select_by_idx(self._idx_)
		except ValueError: # filter deleted
			sql = '''select planets from Filters
				where _idx = (select dft_filter from Config);'''
			idx = int(db.execute(sql).fetchone()[0])
			self._select_by_idx(idx)
	
	def _select(self, filt):
		"""Select planets filter in database.
		
		:raise TypeError: invalid filter
		"""
		if isinstance(filt, int):
			return self._select_by_idx(filt)
		elif isinstance(filt, basestring):
			return self._select_by_name(filt)
		raise TypeError('Invalid filter %s.' % filt)
	
	def _select_by_idx(self, idx):
		"""Select planets filter in database, by idx.
		
		:type idx: int
		:raise ValueError: not found
		"""
		sql = "select * from PlanetsFilters where _idx = ?;"
		res = db.execute(sql, (idx,)).fetchall()
		if len(res) == 0:
			raise ValueError('Invalid filter %s.' % idx)
		self.set(*res[0])
		self._select_dict()
	
	def _select_by_name(self, filt):
		"""Select planets filter in database, by name.
		
		:type filt: str
		:raise ValueError: not found
		"""
		sql = "select * from PlanetsFilters where name = ?;"
		res = db.execute(sql, (filt,)).fetchall()
		if len(res) == 0:
			raise ValueError('Invalid filter %s.' % filt)
		self.set(*res[0])
		self._select_dict()
	
	def _select_dict(self):
		"""Select planets filters dict in database, with aspects filter idx."""
		sql = """select A.name, B.bool_use from Planets as A, _PlanetsFilters
			as B where B.filter_idx = ? and A._idx = B.planet_idx;"""
		res = db.execute(sql, (self._idx_,)).fetchall()
		self._set_dict(res)
	
	def save(self):
		"""Save planets filter in database."""
		if self._idx_ == None:
			self._insert()
		else:
			self._update()
	
	def _insert(self):
		"""Insert planets filter in database.
		
		:raise ValueError: duplicate
		"""
		sql1 = "insert into PlanetsFilters (name, comment) values (?, ?);"
		sql2 = "select _idx from PlanetsFilters where name = ?;"
		try:
			db.execute(sql1, (self._name, self._comment))
		except: # sqlite3.IntegrityError
			raise ValueError('Duplicate filter %s.' % self._name)
		self._idx = db.execute(sql2, (self.name,)).fetchone()[0]
		self._save_dict()
	
	def _update(self):
		"""Update planets filter in database.
		
		:raise ValueError: duplicate
		"""
		sql = "update PlanetsFilters set name = ?, comment = ? where _idx = ?;"
		try:
			db.execute(sql, (self._name, self._comment, self._idx_))
		except: # integrity error
			raise ValueError('Duplicate filter %s.' % self._name)
		self._save_dict()
	
	def delete(self):
		"""Delete planets filter in database.
		
		:raise TypeError: invalid index
		:raise ValueError: integrity error
		"""
		if self._idx_ == None:
			raise TypeError('Missing idx.')
		sql = "delete from PlanetsFilters where _idx = ?;"
		try:
			db.execute(sql, (self._idx_,))
		except: # integrity error
			raise ValueError('Cannot delete default filter.')
		self._idx_ = None
	
	def _save_dict(self):
		"""Save planets filter dict in database (with filter idx)."""
		self._delete_dict()
		sql = """insert into _PlanetsFilters select ?, _idx, ? from Planets
			where name = ?;"""
		for plnt, val in self._dict_.items():
			db.execute(sql, (self._idx_, int(val), plnt))
	
	def _delete_dict(self):
		"""Delete planets filter dict in database."""
		sql = "delete from _PlanetsFilters where filter_idx = ?;"
		db.execute(sql, (self._idx_,))
	
	def __len__(self):
		"""Return number of elements in planets filter.
		
		:rtype: int
		"""
		return len(self._dict_)
	
	def __getitem__(self, key):
		"""Return boolean (planet usage), identified by planet name.
		
		:type key: str
		:rtype: bool
		:raise KeyError: not found
		"""
		return self._dict_[key]
	
	def __setitem__(self, key, value=False):
		"""Set planet usage, identified by planet name.
		
		:type key: str
		:type value: bool
		:raise KeyError: not found
		"""
		for plt in self._dict_.keys():
			if plt == key:
				if value in (True, 1, 'True', '1', 'true'):
					value = True
				else:
					value = False
				self._dict_[plt] = value
				return
		raise KeyError(key)
	
	def __contains__(self, key):
		"""Return True if planet name is in planets filter.
		
		:type key: str
		:rtype: bool
		"""
		return self._dict_.__contains__(key)
	
	def __iter__(self):
		"""Return iterator over planets filter keys.
		
		:rtype: iterator
		"""
		return self._dict_.__iter__()
	
	def keys(self):
		"""Return a list of planets filter keys.
		
		:rtype: list
		"""
		return self._dict_.keys()
	
	def values(self):
		"""Return a list of planets filter values.
		
		:rtype: list
		"""
		return self._dict_.values()
	
	def items(self):
		"""Return a list of planets filter key, value tuples.
		
		:rtype: list
		"""
		return self._dict_.items()
	
	def get(self, key, default=None):
		"""Return boolean (planet usage), identified by key (planet name).
		
		Return default (None) if planet not found.
		
		:type key: str
		:type default: any
		:rtype: bool or default
		"""
		got = self._dict_.__getitem__(key)
		if got == None:
			return default
		return got
	
	def __str__(self):
		"""Show planets filter internals.
		
		:rtype: str
		"""
		return str([x for x in (self._idx_, self._name, self._comment,
			self._dict_)])
	
	def __repr__(self):
		if self._idx_ == None:
			return repr(tuple(repr(x) for x in self))
		return "PlanetsFilter('''%s''')" % self._name
	
	def __getstate__(self):
		return {'_idx': None,
			'name': self._name,
			'comment': self._comment,
			'_dict': self._dict_}
	
	def _to_xml(self, with_idx=False):
		"""Return a xmlutils.Element('PlanetstFilter').
		
		:type with_idx: bool
		:rtype: xmlutils.Element
		"""
		if with_idx:
			el = xmlutils.Element('PlanetsFilter', {'_idx': self._idx_},
				'\n\t', '\n')
		else:
			el = xmlutils.Element('PlanetsFilter', {'_idx': None}, '\n\t', '\n')
		el.append('name', {}, self._name, '\n\t')
		el.append('comment', {}, self._comment, '\n\t')
		el2 = xmlutils.Element('Planets', {}, '\n\t\t', '\n')
		for x, y in self.items():
			el2.append('Planet', {'name': x, 'value': y}, '', '\n\t\t')
		el.append(el2)
		return el
	
	def _from_xml(self, elem, with_idx=False):
		"""Set aspects filter from a xmlutils.Element('PlanetsFilter').
		
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
		"""Return True if other is the same planets filter in database.
		
		:rtype: bool
		"""
		if other == None:
			return False
		if not isinstance(other, PlanetsFilter):
			return False
		if other._idx_ == self._idx_:
			return True
		return False
	
	def __ne__(self, other):
		"""Return True if other is not the same planets filter in database.
		
		:rtype: bool
		"""
		if other == None:
			return True
		if not isinstance(other, PlanetsFilter):
			return True
		if other._idx_ != self._idx_:
			return True
		return False


class PlanetsFiltersList(list):
	"""Planets filters list object."""
	
	def __getitem__(self, item):
		if isinstance(item, int):
			return list.__getitem__(self, item)
		for pf in self:
			if pf._name == item:
				return pf
		raise KeyError(item)
	
	def __contains__(self, item):
		for pf in self:
			if pf._name == item:
				return True
		return False
	
	def get_idx(self, idx):
		for pf in self:
			if pf._idx_ == idx:
				return pf
		raise KeyError(idx)


def all_planets_filters():
	"""Return all planets filters objects.
	
	:rtype: PlanetsFiltersList
	"""
	ret = PlanetsFiltersList()
	sql = "select * from PlanetsFilters order by name;"
	res = db.execute(sql)
	for row in res:
		ret.append(PlanetsFilter(set_default=False))
		ret[-1].set(*row)
		ret[-1]._select_dict()
	return ret


def all_planets_filters_names():
	"""Return a list of all planets filters names.
	
	:rtype: list
	"""
	ret = list()
	sql = 'select name from PlanetsFilters order by name;'
	res = db.execute(sql).fetchall()
	for row in res:
		ret.append(row[0])
	return ret


def xml_export_planets_filters():
	"""Return a xmlutils.Element('PlanetsFilters') containing all planets filters.
	
	:rtype: xmlutils.Element
	"""
	all = all_planets_filters()
	el = xmlutils.Element('PlanetsFilters', {}, '\n', '\n')
	for a in all:
		el.append(a._to_xml())
	return el


def xml_import_planets_filters(elem):
	"""Return a list of planets filters from a xmlutils.Element('PlanetsFilters').
	
	:type elem: xmlutils.Element
	:rtype: PlanetsFiltersList
	"""
	ret = PlanetsFiltersList()
	for a in elem.get_iterator('PlanetsFilter'):
		ret.append(PlanetsFilter(set_default=False))
		ret[-1]._from_xml(a)
	return ret



def _test():
	import doctest
	doctest.testmod()


if __name__ == "__main__":
	_test()

# End.
