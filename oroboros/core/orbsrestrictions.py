#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Orbs restrictions (list of all planets associated with an orb-modifier).

	Create a new orbs restrictions filter:
	
		>>> pof = OrbsRestrictions()
		>>> pof.set(name='foobar')
		>>> pof.save()
	
	Filter details.
	
		>>> pof['Sun']
		oroboros.orbs.OrbModifier("0")
		>>> pof['Pholus']
		oroboros.orbs.OrbModifier("0")
		>>> 'Lilith' in pof
		False
	
	Save, update, delete filter.
	
		>>> pof.save()
		>>> pof
		oroboros.orbsrestrictions.OrbsRestrictions('''foobar''')
		>>> pof['Moon'] = 2
		>>> pof.save()
		>>> pof.delete()
	
	Search functions.
	
		>>> all_orbs_restrictions
		[oroboros.orbsrestrictions.OrbsRestrictions('''<Orbs Restrictions 1>''')]

"""

from oroboros.core import db
from oroboros.core import xmlutils
from oroboros.core.orbs import OrbModifier


__all__ = ['OrbsRestrictions', 'OrbsRestrictionsList',
	'all_orbs_restrictions', 'all_orbs_restrictions_names',
	'xml_export_orbs_restrictions', 'xml_import_orbs_restrictions']


class OrbsRestrictions(db.Object):
	"""Orbs restrictions type."""
	
	__slots__ = ('_idx_', '_name', '_comment', '_dict_')
	
	def _get_name(self):
		"""Return filter name."""
		return self._name
	
	def _set_name(self, name):
		"""Set filter name."""
		self._name = name
	
	def _get_comment(self):
		"""Return filter comment."""
		return self._comment
	
	def _set_comment(self, comment):
		"""Set filter comment."""
		self._comment = comment
	
	def _get_dict(self):
		"""Return internal dict of planets."""
		return self._dict_
	
	def _set_dict(self, res):
		"""Set internal dict of planets (with db result rows)."""
		self._dict_.clear()
		for x, y in res:
			self._dict_[x] = OrbModifier(y)
	
	_idx = property(db.Object._get_idx, db.Object._set_idx,
		doc="Orbs restrictions filter db index value.")
	name = property(_get_name, _set_name,
		doc="Orbs restrictions filter name.")
	comment = property(_get_comment, _set_comment,
		doc="Orbs restrictions filter comment.")
	_dict = property(_get_dict, _set_dict,
		doc="Orbs restrictions filter internal dict.")
	
	def set(self, _idx=None, name=None, comment=None):
		"""Set orbs restrictions properties.
		
		Args: 'name', 'comment'
		
		"""
		if _idx != None:
			self._idx = _idx
		if name != None:
			self.name = name
		if comment != None:
			self.comment = comment
	
	def __init__(self, filt=None, set_default=True):
		"""Orbs restrictions initialization."""
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
		"""Reset Orbs restrictions to default values."""
		sql = "select name, orb_mod from Planets;"
		res = db.execute(sql)
		self._set_dict(res)
	
	def reset(self):
		"""Reset filter when database is updated.
		
		Filter may have been deleted, then load the default one.
		
		"""
		try:
			self._select_by_idx(self._idx_)
		except ValueError: ## filter deleted
			sql = '''select orbrestr from Filters
				where _idx = (select dft_filter from Config);'''
			idx = int(db.execute(sql).fetchone()[0])
			self._select_by_idx(idx)
	
	def _select(self, filt):
		"""Select orbs restrictions filter in database.
		
		Raise TypeError if invalid filter.
		
		"""
		if isinstance(filt, int):
			return self._select_by_idx(filt)
		elif isinstance(filt, basestring): # str in py3
			return self._select_by_name(filt)
		raise TypeError('Invalid filter %s.' % filt)
	
	def _select_by_idx(self, idx):
		"""Select Orbs restrictions filter by idx.
		
		Raise ValueError if not found.
		
		"""
		sql = "select * from OrbsRestrictions where _idx = ?;"
		res = db.execute(sql, (idx,)).fetchall()
		if len(res) == 0:
			raise ValueError('Invalid idx %s.' % idx)
		self.set(*res[0])
		self._select_dict()
	
	def _select_by_name(self, filt):
		"""Select orbs restrictions filter by name.
		
		Raise ValueError if not found.
		
		"""
		sql = "select * from OrbsRestrictions where name = ?;"
		res = db.execute(sql, (filt,)).fetchall()
		if len(res) == 0:
			raise ValueError('Invalid filter %s.' % filt)
		self.set(*res[0])
		self._select_dict()
	
	def _select_dict(self):
		"""Select orbs restrictions dict in database."""
		sql = """select A.name, B.orb_mod from Planets as A, _OrbsRestrictions
			as B where B.filter_idx = ? and A._idx = B.planet_idx;"""
		res = db.execute(sql, (self._idx_,)).fetchall()
		self._set_dict(res)
	
	def save(self):
		"""Save orbs restrictions filter in database."""
		if self._idx_ == None:
			self._insert()
		else:
			self._update()
	
	def _insert(self):
		"""Insert orbs restrictions filter in database.
		
		Raise ValueError if duplicate.
		
		"""
		sql1 = "insert into OrbsRestrictions (name, comment) values (?, ?);"
		sql2 = "select _idx from OrbsRestrictions where name = ?;"
		try:
			db.execute(sql1, (self._name, self._comment))
		except: # sqlite3.IntegrityError?
			raise ValueError('Duplicate filter %s' % self._name)
		self._idx = db.execute(sql2, (self._name,)).fetchone()[0]
		self._save_dict()
	
	def _update(self):
		"""Update orbs restrictions filter in database.
		
		Raise ValueError if duplicate.
		
		"""
		sql = """update OrbsRestrictions set name = ?, comment = ?
			where _idx = ?;"""
		try:
			db.execute(sql, (self._name, self._comment, self._idx_))
		except: ## integrity error
			raise ValueError('Duplicate filter %s.' % self._name)
		self._save_dict()
	
	def delete(self):
		"""Delete orbs restrictions in database (by idx).
		
		Raise TypeError if idx is None.
		Raise ValueError if filter is required by default filter.
		
		"""
		if self._idx_ == None:
			raise TypeError('Missing idx.')
		sql = "delete from OrbsRestrictions where _idx = ?;"
		try:
			db.execute(sql, (self._idx_,))
		except:
			raise ValueError('Cannot delete default filter.')
		self._idx_ = None
	
	def _save_dict(self):
		"""Save orbs restrictions dict in database (with idx)."""
		self._delete_dict()
		sql = """insert into _OrbsRestrictions select ?, _idx, ? from
			Planets where name = ?;"""
		for plt, val in self.items():
			db.execute(sql, (self._idx_, val, plt))
	
	def _delete_dict(self):
		"""Delete orbs restrictions filter dict in database."""
		sql = "delete from _OrbsRestrictions where filter_idx = ?;"
		db.execute(sql, (self._idx_,))
	
	def __len__(self):
		"""Return number of planets in orbs restrictions."""
		return len(self._dict_)
	
	def __getitem__(self, key):
		"""Return orb modifier identified by planet name.
		
		Raise KeyError if planet not found.
		
		"""
		return self._dict_[key]
	
	def __setitem__(self, key, value=False):
		"""Set planet orb modifier, identified by planet name.
		
		Raise KeyError if planet not found.
		
		"""
		for plt in self._dict_:
			if plt == key:
				self._dict_[plt] = OrbModifier(value)
				return
		raise KeyError(key)
	
	def __contains__(self, key):
		"""Return True if planet name is in orbs restrictions."""
		return self._dict_.__contains__(key)
	
	def __iter__(self):
		"""Return iterator over orbs restrictions keys."""
		return self._dict_.__iter__()
	
	def keys(self):
		"""Return a list of Orbs restrictions keys."""
		return self._dict_.keys()
	
	def values(self):
		"""Return a list of Orbs restrictions values."""
		return self._dict_.values()
	
	def items(self):
		"""Return a list of Orbs restrictions key, value tuples."""
		return self._dict_.items()
	
	def get(self, key, default=None):
		"""Return orb modifier, identified by key (planet name).
		
		Return default (None) if aspect not found.
		
		"""
		got = self.__getitem__(key)
		if got == None:
			return default
		return got
	
	def __str__(self):
		"""Return orbs restrictions filter as string."""
		return str([x for x in (self._idx_, self._name, self._comment,
			self._dict_)])
	
	def __repr__(self):
		if self._idx_ == None:
			return repr(str(self))
		return """oroboros.orbsrestrictions.OrbsRestrictions('''%s''')""" % self._name
	
	def __getstate__(self):
		return {'_idx': None,
			'name': self._name,
			'comment': self._comment,
			'_dict': self._dict_}
	
	def _to_xml(self, with_idx=False):
		"""Return a xmlutils.Element('OrbsRestrictions')."""
		if with_idx:
			el = xmlutils.Element('OrbsRestrictions', {'_idx': self._idx_},
				'\n\t', '\n')
		else:
			el = xmlutils.Element('OrbsRestrictions', {'_idx': None},
				'\n\t', '\n')
		el.append('name', {}, self._name, '\n\t')
		el.append('comment', {}, self._comment, '\n\t')
		el2 = xmlutils.Element('Planets', {}, '\n\t', '\n')
		for x, y in self.items():
			el2.append('Planet', {'name': x, 'value': y}, '', '\n\t\t')
		el.append(el2)
		return el
	
	def _from_xml(self, elem, with_idx=False):
		"""Set aspects filter from a xmlutils.Element('OrbsRestrictions')."""
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
		"""Return True if other is the same filter in database."""
		if other == None:
			return False
		if not isinstance(other, OrbsRestrictions):
			return False
		if other._idx_ == self._idx_:
			return True
		return False
	
	def __ne__(self, other):
		"""Return True if other is not the same filter in database."""
		if other == None:
			return True
		if not isinstance(other, OrbsRestrictions):
			return True
		if other._idx_ != self._idx_:
			return True
		return False


class OrbsRestrictionsList(list):
	"""Orbs restrictions list object."""
	
	def __getitem__(self, item):
		if isinstance(item, int):
			return list.__getitem__(self, item)
		for o in self:
			if o._name == item:
				return o
		raise KeyError(item)
	
	def __contains__(self, item):
		for o in self:
			if o._name == item:
				return True
		return False
	
	def get_idx(self, idx):
		for o in self:
			if o._idx_ == idx:
				return o
		raise KeyError(idx)


def all_orbs_restrictions():
	"""Get list of all orbs filters objects."""
	ret = OrbsRestrictionsList()
	sql = "select * from OrbsRestrictions order by name;"
	res = db.execute(sql).fetchall()
	for row in res:
		ret.append(OrbsRestrictions(set_default=False))
		ret[-1].set(*row)
		ret[-1]._select_dict()
	return ret


def all_orbs_restrictions_names():
	"""Return a list of all orbs restrictions names."""
	ret = list()
	sql = 'select name from OrbsRestrictions order by name;'
	res = db.execute(sql).fetchall()
	for row in res:
		ret.append(row[0])
	return ret


def xml_export_orbs_restrictions():
	"""Return a xmlutils.Element('AllOrbsRestrictions')."""
	all = all_orbs_restrictions()
	el = xmlutils.Element('AllOrbsRestrictions', {}, '\n', '\n')
	for a in all:
		el.append(a._to_xml())
	return el


def xml_import_orbs_restrictions(elem, with_idx=False):
	"""Return a list of orbs restrictions from a xmlutils.Element('AllOrbsRestrictions')."""
	ret = list()
	for a in elem.get_iterator('OrbsRestrictions'):
		ret.append(OrbsRestrictions(set_default=False))
		ret[-1]._from_xml(a, with_idx=with_idx)
	return ret



def _test():
	import doctest
	doctest.testmod()


if __name__ == "__main__":
	_test()

# End.
