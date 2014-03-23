#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Mid-points filters.

"""

from oroboros.core import db
from oroboros.core.planetsfilters import PlanetsFilter
from oroboros.core.aspectsfilters import AspectsFilter
from oroboros.core.orbsfilters import OrbsFilter
from oroboros.core.aspectsrestrictions import AspectsRestrictions
from oroboros.core.orbsrestrictions import OrbsRestrictions


__all__ = ['MidPointsFilter', 'MidPointsFiltersList',
	'all_midpoints_filters', 'all_midpoints_filters_names',
	'xml_export_midpoints_filters', 'xml_import_midpoints_filters']


class MidPointsFilter(db.Object):
	"""Mid-points settings."""
	
	__slots__ = ('_idx_', '_name', '_planets', '_aspects', '_orbs', '_asprestr',
		'_orbrestr', '_comment')
	
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
	
	# sub filters
	
	def _get_planets(self):
		"""Get planets filter.
		
		:rtype: PlanetsFilter
		"""
		return self._planets
	
	def _set_planets(self, filt):
		"""Set planets filter.
		
		:type filt: PlanetsFilter, str or int
		"""
		if not isinstance(filt, PlanetsFilter):
			self._planets = PlanetsFilter(filt)
		else:
			self._planets = filt
	
	def _get_aspects(self):
		"""Get aspects filter.
		
		:rtype: AspectsFilter
		"""
		return self._aspects
	
	def _set_aspects(self, filt):
		"""Set aspects filter.
		
		:type filt: AspectsFilter, str or int
		"""
		if not isinstance(filt, AspectsFilter):
			self._aspects = AspectsFilter(filt)
		else:
			self._aspects = filt
	
	def _get_orbs(self):
		"""Get orbs filter.
		
		:rtype: OrbsFilter
		"""
		return self._orbs
	
	def _set_orbs(self, filt):
		"""Set orbs filter.
		
		:type filt: OrbsFilter, str or int
		"""
		if not isinstance(filt, OrbsFilter):
			self._orbs = OrbsFilter(filt)
		else:
			self._orbs = filt
	
	def _get_asprestr(self):
		"""Get aspects restrictions.
		
		:rtype: AspectsRestrictions
		"""
		return self._asprestr
	
	def _set_asprestr(self, filt):
		"""Set aspects restrictions.
		
		:type filt: AspectsRestrictions
		"""
		if not isinstance(filt, AspectsRestrictions):
			self._asprestr = AspectsRestrictions(filt)
		else:
			self._asprestr = filt
	
	def _get_orbrestr(self):
		"""Get orbs restrictions.
		
		:rtype: OrbsRestrictions
		"""
		return self._orbrestr
	
	def _set_orbrestr(self, filt):
		"""Set orbs restrictions.
		
		:type filt: OrbsRestrictions, str or int
		"""
		if not isinstance(filt, OrbsRestrictions):
			self._orbrestr = OrbsRestrictions(filt)
		else:
			self._orbrestr = filt
	
	_idx = property(db.Object._get_idx, db.Object._set_idx,
		doc='Filter db index value.')
	name = property(_get_name, _set_name,
		doc='Filter name.')
	planets = property(_get_planets, _set_planets,
		doc='Planets filter.')
	aspects = property(_get_aspects, _set_aspects,
		doc='Aspects filter.')
	orbs = property(_get_orbs, _set_orbs,
		doc='Orbs filter.')
	asprestr = property(_get_asprestr, _set_asprestr,
		doc='Aspects restrictions.')
	orbrestr = property(_get_orbrestr, _set_orbrestr,
		doc='Orbs restrictions.')
	comment = property(_get_comment, _set_comment,
		doc='Filter comment.')
	
	def set(self, _idx=None, name=None, planets=None, aspects=None, orbs=None,
		asprestr=None, orbrestr=None, comment=None):
		"""Set filter properties."""
		if _idx != None:
			self._idx = _idx
		if name != None:
			self.name = name
		if planets != None:
			self.planets = planets
		if aspects != None:
			self.aspects = aspects
		if orbs != None:
			self.orbs = orbs
		if asprestr != None:
			self.asprestr = asprestr
		if orbrestr != None:
			self.orbrestr = orbrestr
		if comment != None:
			self.comment = comment
	
	def __init__(self, filt=None, set_default=True):
		"""Init midpoints filters.
		
		:type filt: str or int or None
		:type set_default: bool
		"""
		if filt != None:
			return self._select(filt)
		elif set_default:
			self.set_default()
	
	def set_default(self):
		"""Set filter to default values."""
		sql = '''select midpoints from Filters
			where _idx = (select dft_filter from Config);'''
		idx = int(db.execute(sql).fetchone()[0])
		self._select_by_idx(idx)
	
	def reset(self):
		"""Reset filter when database is updated.
		
		Filter may have been deleted, then load the default one.
		
		"""
		try:
			self._select_by_idx(self._idx_)
		except ValueError: # filter deleted
			self.set_default()
	
	def _select(self, filt):
		"""Select filter in database.
		
		:type filt: str or int
		:raise TypeError: invalid filter
		"""
		if isinstance(filt, int):
			return self._select_by_idx(filt)
		elif isinstance(filt, basestring): ## not py3
			return self._select_by_name(filt)
		raise TypeError('Invalid filter %s.' % filt)
	
	def _select_by_idx(self, idx):
		"""Select filter in database, by idx.
		
		:type idx: int
		:raise ValueError: not found
		"""
		sql = "select * from MidPointsFilters where _idx = ?;"
		res = db.execute(sql, (idx,)).fetchall()
		if len(res) == 0:
			raise ValueError('Invalid idx %s.' % idx)
		self.set(*res[0])
	
	def _select_by_name(self, filt):
		"""Select filter in database, by name.
		
		:type filt: name
		:raise ValueError: not found
		"""
		sql = "select * from MidPointsFilters where name = ?;"
		res = db.execute(sql, (filt,)).fetchall()
		if len(res) == 0:
			raise ValueError('Invalid filter %s.' % filt)
		self.set(*res[0])
	
	def save(self, recursive=False):
		"""Save filter in database.
		
		If recursive is True, save all sub-filters.
		Else raise TypeError if a sub-filter is not saved.
		
		:type recursive: bool
		"""
		if self._idx_ == None:
			self._insert(recursive)
		else:
			self._update(recursive)
	
	def _insert(self, recursive=False):
		"""Insert filter in database.
		
		:type recursive: bool
		:raise ValueError: duplicate
		"""
		self._save_filters(recursive)
		sql1 = """insert into MidPointsFilters (name, planets,
			aspects, orbs, asprestr, orbrestr, comment) values (?, ?, ?, ?, ?,
			?, ?);"""
		var = (self._name, self._planets._idx_, self._aspects._idx_,
			self._orbs._idx_, self._asprestr._idx_, self._orbrestr._idx_,
			self._comment)
		sql2 = "select _idx from MidPointsFilters where name = ?;"
		try:
			db.execute(sql1, var)
		except: # sqlite3.IntegrityError
			raise ValueError('Duplicate filter %s.' % self._name)
		self._idx = db.execute(sql2,(self._name,)).fetchone()[0]
	
	def _update(self, recursive=False):
		"""Update filter in database.
		
		:type recursive: bool
		:raise ValueError: duplicate
		"""
		self._save_filters(recursive)
		sql = """update MidPointsFilters set name = ?, planets = ?, aspects = ?,
			orbs = ?, asprestr = ?, orbrestr = ?, comment = ? where _idx = ?;"""
		var = (self._name, self._planets._idx_, self._aspects._idx_,
			self._orbs._idx_, self._asprestr._idx_, self._orbrestr._idx_,
			self._comment, self._idx_)
		try:
			db.execute(sql, var)
		except: # integrity error
			raise ValueError('Duplicate filter %s.' % self._name)
	
	def _save_filters(self, recursive):
		"""Save sub-filters if recursive is True, else check they are saved.
		
		Raise TypeError if recursive is False and sub-filter is not saved.
		
		:type recursive: bool
		"""
		for f in (self._planets, self._aspects, self._orbs, self.asprestr,
			self._orbrestr):
			if recursive:
				f.save()
			else:
				if f._idx_ == None:
					raise TypeError('Sub filter %s is not saved.' % f._name)
	
	def delete(self):
		"""Delete filter in database.
		
		:raise TypeError: invalid index
		:raise ValueError: integrity error
		"""
		if self._idx_ == None:
			raise TypeError('Missing idx')
		sql = "delete from MidPointsFilters where _idx = ?;"
		try:
			db.execute(sql, (self._idx_,))
		except: # sqlite3 integrity error 
			raise ValueError('Cannot delete default filter.')
		self._idx_ = None
	
	def __iter__(self):
		"""Return iterator over filter's internals.
		
		:rtype: iterator
		"""
		return (x for x in (self._idx_, self._name,
			self._planets, self._aspects, self._orbs, self._asprestr,
			self._orbrestr, self._comment))
	
	def __str__(self):
		"""Show filter internals.
		
		:rtype: str
		"""
		return str(tuple(self))
	
	def __repr__(self):
		if self._idx_ == None:
			return repr(tuple(repr(x) for x in self))
		return "MidPointsFilter('''%s''')" % self._name
	
	def __getstate__(self):
		"""TODO."""
		pass
	
	def _to_xml(self, with_idx=False):
		"""TODO."""
		pass
	
	def _from_xml(self, elem, with_idx=False):
		"""TODO."""
		pass
	
	def __eq__(self, other):
		"""Return True if other is the same filter in database.
		
		:rtype: bool
		"""
		if other == None:
			return False
		if not isinstance(other, MidPointsFilter):
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
		if not isinstance(other, MidPointsFilter):
			return True
		if other._idx_ != self._idx_:
			return True
		return False


class MidPointsFiltersList(list):
	"""Midpoints filters list object."""
	
	def __getitem__(self, item):
		if isinstance(item, int):
			return list.__getitem__(self, item)
		for mp in self:
			if mp._name == item:
				return mp
		raise KeyError(item)
	
	def __contains__(self, item):
		for mp in self:
			if mp._name == item:
				return True
		raise KeyError(item)
	
	def get_idx(self, idx):
		for mp in self:
			if mp._idx_ == idx:
				return mp
		raise KeyError(idx)


def all_midpoints_filters():
	"""Return a list of all mid-points filters in database.
	
	:rtype: MidPointsFiltersList
	"""
	ret = MidPointsFiltersList()
	sql = "select * from MidPointsFilters order by name;"
	res = db.execute(sql).fetchall()
	for row in res:
		ret.append(MidPointsFilter(set_default=False))
		ret[-1].set(*row)
	return ret


def all_midpoints_filters_names():
	"""Return a list of all midpoints filters names.
	
	:rtype: list
	"""
	ret = list()
	sql = 'select name from MidPointsFilters order by name;'
	res = db.execute(sql).fetchall()
	for row in res:
		ret.append(row[0])
	return ret


def xml_export_midpoints_filters():
	""":todo:"""
	pass


def xml_import_midpoints_filters(elem, with_idx=False):
	""":todo:"""
	pass


def _test():
	import doctest
	doctest.testmod()


if __name__ == '__main__':
	_test()

# End.
