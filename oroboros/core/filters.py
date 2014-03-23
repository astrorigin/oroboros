#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Filters sets.

These filters contain all the information for a chart calculation and
display. This is a fait amount of data. It includes all other filters,
as well as options for the swiss ephemeris, zodiac type, etc.

	Create a new filter.
	
		>>> f = Filter()
		>>> f.name = 'Meta filter'
		>>> f.ephe_type = 'jpl' # use JPL ephemeris
		>>> f.ephe_path = '/usr/share/jpl/deXXX.e'
		>>> f.hsys = 'K' # Koch house system
		>>> f.comment = 'Test'


"""

import swisseph as swe

from oroboros.core import db
from oroboros.core import geocoords
from oroboros.core.planetsfilters import PlanetsFilter
from oroboros.core.aspectsfilters import AspectsFilter
from oroboros.core.orbsfilters import OrbsFilter
from oroboros.core.aspectsrestrictions import AspectsRestrictions
from oroboros.core.orbsrestrictions import OrbsRestrictions
from oroboros.core.midpfilters import MidPointsFilter


__all__ = ['Filter', 'FiltersList',
	'all_filters', 'all_filters_names',
	'xml_export_filters', 'xml_import filters']


class Filter(db.Object):
	"""Filters set and options."""
	
	__slots__ = ('_idx_', '_name', '_bg_color', '_ephe_type', '_ephe_path',
		'_hsys', '_sid_mode', '_sid_t0', '_sid_ayan_t0', '_true_pos',
		'_xcentric', '_calc_midp', '_draw_midp', '_comment',
		# sub-filters:
		'_planets', '_aspects', '_orbs', '_asprestr', '_orbrestr',
		'_midpoints')
	
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
	
	def _get_bg_color(self):
		"""Get background color.
		
		:rtype: str
		"""
		return self._bg_color
	
	def _set_bg_color(self, clr):
		"""Set background color ('black', 'white').
		
		:type clr: str
		:raise ValueError: invalid color
		"""
		if clr not in ('black', 'white'):
			raise ValueError('Invalid background color %s.' % clr)
		self._bg_color = clr
	
	def _get_ephe_type(self):
		"""Get ephemeris type.
		
		:rtype: str
		"""
		return self._ephe_type
	
	def _set_ephe_type(self, ephe='swiss'):
		"""Set ephemeris type ('swiss', 'jpl', 'moshier').
		
		:type ephe: str
		:raise ValueError: invalid ephemeris type
		"""
		if ephe not in ('swiss', 'jpl', 'moshier'):
			raise ValueError('Invalid ephemeris type %s.' % ephe)
		self._ephe_type = ephe
	
	def _get_ephe_path(self):
		"""Get ephemeris files directory (or file for jpl) path.
		
		:rtype: str
		"""
		return self._ephe_path
	
	def _set_ephe_path(self, path):
		"""Set ephemeris directory/file.
		
		:type path: str
		"""
		self._ephe_path = str(path) # str() till pyswisseph accepts unicode!
	
	def _get_hsys(self):
		"""Get house system.
		
		:rtype: str
		"""
		return self._hsys
	
	def _set_hsys(self, hsys='P'):
		"""Set house system.
		
		One in 'PKORCAEVXHTBG'. See swisseph docs.
		
		:type hsys: str
		"""
		if hsys not in 'PKRCBOAEHVXGU':
			raise ValueError('Invalid house system %s.' % hsys)
		self._hsys = str(hsys) ## till pyswisseph accepts unicode
	
	def _get_sid_mode(self):
		return self._sid_mode
	
	def _set_sid_mode(self, sidmode=-1):
		"""Set sidereal mode.
		
			- -1 -> western tropical zodiac
			- 0+ -> sidereal modes
			- 255 -> user-defined sidereal (see sid_t0 and sid_ayan_t0)
		
		:type sidmode: int
		:raise ValueError: invalid sidereal mode
		"""
		if sidmode < -1 or sidmode > 255:
			raise ValueError('Invalid sidereal mode %s.' % sidmode)
		self._sid_mode = sidmode
	
	def _get_sid_t0(self):
		"""Get sidereal time 0.
		
		:rtype: float
		"""
		return self._sid_t0
	
	def _set_sid_t0(self, sidt0):
		"""Set sidereal time 0.
		
		:type sidt0: numeric
		"""
		self._sid_t0 = float(sidt0)
	
	def _get_sid_ayan_t0(self):
		"""Get sidereal ayanamsa at t0.
		
		:rtype: float
		"""
		return self._sid_ayan_t0
	
	def _set_sid_ayan_t0(self, ayan_t0):
		"""Set sidereal ayanamsa at t0.
		
		:type ayan_t0: numeric
		"""
		self._sid_ayan_t0 = float(ayan_t0)
	
	def _get_true_pos(self):
		"""Get true positions flag.
		
		:rtype: bool
		"""
		return self._true_pos
	
	def _set_true_pos(self, boolean=False):
		"""Set true positions flag
		
		:type boolean: bool
		"""
		self._true_pos = bool(boolean)
	
	def _get_xcentric(self):
		"""Get observer mode.
		
		:rtype: str
		"""
		return self._xcentric
	
	def _set_xcentric(self, xcentric='geo'):
		"""Set geo/topo/helio/bary centric mode.
		
		:type xcentric: str
		:raise ValueError: invalid mode
		"""
		if xcentric not in ('geo', 'topo', 'helio', 'bary'):
			raise ValueError('Invalid xcentric mode %s.' % xcentric)
		self._xcentric = xcentric
	
	def _get_calc_midp(self):
		"""Calculate mid-points or not (boolean).
		
		:rtype: bool
		"""
		return self._calc_midp
	
	def _set_calc_midp(self, boolean):
		"""Set midpoints flag.
		
		:type boolean: bool
		"""
		if boolean in (True, 1, 'True', '1', 'yes'):
			self._calc_midp = True
		else:
			self._calc_midp = False
	
	def _get_draw_midp(self):
		"""Draw mid-points aspects or not (boolean).
		
		:rtype: bool
		"""
		return self._draw_midp
	
	def _set_draw_midp(self, boolean):
		"""Set mid-points drawing flag.
		
		:type boolean: bool
		"""
		if boolean in (True, 1, 'True', '1', 'yes'):
			self._draw_midp = True
		else:
			self._draw_midp = False
	
	def _get_comment(self):
		"""Get comment
		
		:rtype: str
		"""
		return self._comment
	
	def _set_comment(self, comment):
		"""Set comment.
		
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
		
		:type filt: AspectsRestrictions, str or int
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
	
	def _get_midpoints(self):
		"""Get midpoints filters.
		
		:rtype: MidPointsFilter
		"""
		return self._midpoints
	
	def _set_midpoints(self, filt):
		"""Set mid-points filters.
		
		:type filt: MidPointsFilter, str or int
		"""
		if not isinstance(filt, MidPointsFilter):
			self._midpoints = MidPointsFilter(filt)
		else:
			self._midpoints = filt
	
	_idx = property(db.Object._get_idx, db.Object._set_idx,
		doc='Filter db index value.')
	name = property(_get_name, _set_name,
		doc='Filter name.')
	bg_color = property(_get_bg_color, _set_bg_color,
		doc='Background color (black|white).')
	ephe_type = property(_get_ephe_type, _set_ephe_type,
		doc='Ephemeris type (swiss|jpl|moshier).')
	ephe_path = property(_get_ephe_path, _set_ephe_path,
		doc='Ephemeris directory/files path.')
	hsys = property(_get_hsys, _set_hsys,
		doc='House system (PKORCAEVXHTBG). See swisseph docs.')
	sid_mode = property(_get_sid_mode, _set_sid_mode,
		doc='Sidereal mode (-1=tropical). See swisseph docs.')
	sid_t0 = property(_get_sid_t0, _set_sid_t0,
		doc='Sidereal mode reference time.')
	sid_ayan_t0 = property(_get_sid_ayan_t0, _set_sid_ayan_t0,
		doc='Sidereal mode ayanmsa.')
	true_pos = property(_get_true_pos, _set_true_pos,
		doc='True positions mode (boolean).')
	xcentric = property(_get_xcentric, _set_xcentric,
		doc='geo/topo/helio/bary centric mode.')
	calc_midp = property(_get_calc_midp, _set_calc_midp,
		doc='Calculate mid-points.')
	draw_midp = property(_get_draw_midp, _set_draw_midp,
		doc='Draw mid-points.')
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
	midpoints = property(_get_midpoints, _set_midpoints,
		doc='Mid-points filter.')
	comment = property(_get_comment, _set_comment,
		doc='Filter comment.')
	
	def set(self, _idx=None, name=None, bg_color=None, ephe_type=None,
		ephe_path=None, hsys=None, sid_mode=None, sid_t0=None,
		sid_ayan_t0=None, true_pos=None, xcentric=None, calc_midp=None,
		draw_midp=None, planets=None, aspects=None, orbs=None, asprestr=None,
		orbrestr=None, midpoints=None, comment=None):
		"""Set filter properties."""
		if _idx != None:
			self._idx = _idx
		if name != None:
			self.name = name
		if bg_color != None:
			self.bg_color = bg_color
		if ephe_type != None:
			self.ephe_type = ephe_type
		if ephe_path != None:
			self.ephe_path = ephe_path
		if hsys != None:
			self.hsys = hsys
		if sid_mode != None:
			self.sid_mode = sid_mode
		if sid_t0 != None:
			self.sid_t0 = sid_t0
		if sid_ayan_t0 != None:
			self.sid_ayan_t0 = sid_ayan_t0
		if true_pos != None:
			self.true_pos = true_pos
		if xcentric != None:
			self.xcentric = xcentric
		if calc_midp != None:
			self.calc_midp = calc_midp
		if draw_midp != None:
			self.draw_midp = draw_midp
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
		if midpoints != None:
			self.midpoints = midpoints
		if comment != None:
			self.comment = comment
	
	def __init__(self, filt=None, set_default=True):
		"""Init filter.
		
		:type filt: str or int
		:type set_default: bool
		"""
		if filt != None:
			return self._select(filt)
		if set_default:
			self.set_default()
	
	def set_default(self):
		"""Set filter to default values."""
		sql = 'select dft_filter from Config;'
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
		sql = "select * from Filters where _idx = ?;"
		res = db.execute(sql, (idx,)).fetchall()
		if len(res) == 0:
			raise ValueError('Invalid idx %s.' % idx)
		self.set(*res[0])
	
	def _select_by_name(self, filt):
		"""Select filter in database, by name.
		
		:type filt: str
		:raise ValueError: not found
		"""
		sql = "select * from Filters where name = ?;"
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
		sql1 = """insert into Filters (name, bg_color, ephe_type, ephe_path,
			hsys, sid_mode, sid_t0, sid_ayan_t0, true_pos, xcentric, calc_midp,
			draw_midp, planets, aspects, orbs, asprestr, orbrestr, midpoints,
			comment) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
			?, ?);"""
		var = (self._name, self._bg_color, self._ephe_type, self._ephe_path,
			self._hsys, self._sid_mode, self._sid_t0, self._sid_ayan_t0,
			self._true_pos, self._xcentric, self._calc_midp, self._draw_midp,
			self._planets._idx_, self._aspects._idx_, self._orbs._idx_,
			self._asprestr._idx_, self._orbrestr._idx_, self._midpoints._idx_,
			self._comment)
		sql2 = "select _idx from Filters where name = ?;"
		try:
			db.execute(sql1, var)
		except: # sqlite3.IntegrityError
			raise ValueError('Duplicate filter %s.' % self._name)
		self._idx = db.execute(sql2,(self._name,)).fetchone()[0]
	
	def _update(self, recursive=False):
		"""Update filter in database.
		
		:raise ValueError: duplicate
		"""
		self._save_filters(recursive)
		sql = """update Filters set name = ?, bg_color = ?, ephe_type = ?,
			ephe_path = ?, hsys = ?, sid_mode = ?, sid_t0 = ?, sid_ayan_t0 = ?,
			true_pos = ?, xcentric = ?, calc_midp = ?, draw_midp = ?,
			planets = ?, aspects = ?, orbs = ?, asprestr = ?, orbrestr = ?,
			midpoints = ?, comment = ? where _idx = ?;"""
		var = (self._name, self._bg_color, self._ephe_type, self._ephe_path,
			self._hsys, self._sid_mode, self._sid_t0, self._sid_ayan_t0,
			self._true_pos, self._xcentric, self._calc_midp, self._draw_midp,
			self._planets._idx_, self._aspects._idx_, self._orbs._idx_,
			self._asprestr._idx_, self._orbrestr._idx_, self._midpoints._idx_,
			self._comment, self._idx_)
		try:
			db.execute(sql, var)
		except: ## integrity error
			raise ValueError('Duplicate filter %s.' % self._name)
	
	def _save_filters(self, recursive):
		"""Save sub-filters if recursive is True, else check they are saved.
		
		Raise TypeError if recursive is False and sub-filter is not saved.
		
		:type recursive: bool
		"""
		for f in (self.planets, self.aspects, self.orbs, self.asprestr,
			self.orbrestr, self.midpoints):
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
		sql = "delete from Filters where _idx = ?;"
		try:
			db.execute(sql, (self._idx_,))
		except: # sqlite3 integrity error
			raise ValueError('Cannot delete default filter.')
		self._idx_ = None
	
	def get_calcflag(self):
		"""Return swisseph calculation flag.
		
		:rtype: int
		"""
		flag = 0
		# speed
		flag += swe.FLG_SPEED
		# ephemeris type
		if self._ephe_type == 'swiss':
			flag += swe.FLG_SWIEPH
		elif self._ephe_type == 'jpl':
			flag += swe.FLG_JPLEPH
		elif self._ephe_type == 'moshier':
			flag += swe.FLG_MOSEPH
		# sidereal mode
		if self._sid_mode > -1:
			flag += swe.FLG_SIDEREAL
		# true positions
		if self._true_pos:
			flag += swe.FLG_TRUEPOS
		# xcentric
		if self._xcentric == 'topo':
			flag += swe.FLG_TOPOCTR
		elif self._xcentric == 'helio':
			flag += swe.FLG_HELCTR
		elif self._xcentric == 'bary':
			flag += swe.FLG_BARYCTR
		return flag
	
	def __iter__(self):
		"""Iterate over filter internals.
		
		:rtype: iterator
		"""
		return (x for x in (self._idx_, self._name, self._bg_color,
			self._ephe_type, self._ephe_path, self._hsys, self._sid_mode,
			self._sid_t0, self._sid_ayan_t0, self._true_pos, self._xcentric,
			self._calc_midp, self._draw_midp, self._planets, self._aspects,
			self._orbs, self._asprestr, self._orbrestr, self._midpoints,
			self._comment))
	
	def __str__(self):
		"""Show filter internals."""
		return str(tuple(self))
	
	def __repr__(self):
		if self._idx_ == None:
			return repr(tuple(repr(x) for x in self))
		return "Filter('''%s''')" % self._name
	
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
		if not isinstance(other, Filter):
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
		if not isinstance(other, Filter):
			return True
		if other._idx_ != self._idx_:
			return True
		return False


class FiltersList(list):
	"""Filters list object."""
	
	def __getitem__(self, item):
		if isinstance(item, int):
			return list.__getitem__(self, item)
		for f in self:
			if f._name == item:
				return f
		raise KeyError(item)
	
	def __contains__(self, item):
		for f in self:
			if f._name == item:
				return True
		return False
	
	def get_idx(self, idx):
		for f in self:
			if f._idx_ == idx:
				return f
		raise KeyError(idx)


def all_filters():
	"""Return a list of all filters in database.
	
	:rtype: FiltersList
	"""
	ret = FiltersList()
	sql = "select * from Filters order by name;"
	res = db.execute(sql).fetchall()
	for row in res:
		ret.append(Filter(set_default=False))
		ret[-1].set(*row)
	return ret


def all_filters_names():
	"""Return a list of all filters names.
	
	:rtype: list
	"""
	ret = list()
	sql = 'select name from Filters order by name;'
	res = db.execute(sql).fetchall()
	for row in res:
		ret.append(row[0])
	return ret


def xml_export_filters():
	""":todo:"""
	pass


def xml_import_filters(elem, with_idx=False):
	""":todo:"""
	pass


def _test():
	import doctest
	doctest.testmod()


if __name__ == '__main__':
	_test()

# End.
