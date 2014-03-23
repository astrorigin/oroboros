#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Chart calculations.

"""

from decimal import Decimal

import swisseph as swe

from oroboros.core import cfg
from oroboros.core import db
from oroboros.core.chartdate import ChartDate
from oroboros.core.filters import Filter
from oroboros.core.planets import all_planets
from oroboros.core.aspects import all_aspects
from oroboros.core.results import HousesDataList, PlanetDataList, MidPointDataList
from oroboros.core.aspectsresults import AspectDataList, MidPointAspectDataList


__all__ = ['ChartCalc']


class ChartCalc(ChartDate):
    """Chart with planets, houses, midpoints, aspects calculation methods."""

    __slots__ = ChartDate.__slots__ + ['_ecl_nut', '_planets', '_houses',
        '_aspects', '_midpoints', '_midp_aspects', '_filter']

    def _set_datetime(self, dt):
        ChartDate._set_datetime(self, dt)
        self.reset_positions()

    def _set_calendar(self, cal):
        ChartDate._set_calendar(self, cal)
        self.reset_positions()

    def _set_location(self, location):
        ChartDate._set_location(self, location)
        self.reset_positions()

    def _set_latitude(self, lat):
        ChartDate._set_latitude(self, lat)
        self.reset_positions()

    def _set_longitude(self, lon):
        ChartDate._set_longitude(self, lon)
        self.reset_positions()

    def _set_altitude(self, alt):
        ChartDate._set_altitude(self, alt)
        self.reset_positions()

    def _set_zoneinfo(self, tz):
        ChartDate._set_zoneinfo(self, tz)
        self.reset_positions()

    def _set_timezone(self, tz):
        ChartDate._set_timezone(self, tz)
        self.reset_positions()

    def _set_dst(self, dst):
        ChartDate._set_dst(self, dst)
        self.reset_positions()

    def _set_utcoffset(self, utcoffset):
        ChartDate._set_utcoffset(self, utcoffset)
        self.reset_positions()

    def _get_filter(self):
        """Get chart filter.

        :rtype: filters.Filter
        """
        return self._filter

    def _set_filter(self, filt):
        """Set chart filter.

        Accepts Filter objects, filter names or index.

        :type filt: filters.Filter or str or int
        """
        if not isinstance(filt, Filter):
            self._filter = Filter(filt)
        else:
            self.filter = filt
        self.reset_positions()

    def _get_ecl_nut(self):
        """Get results for obliquity, nutation, etc.

        :rtype: tuple
        """
        if self._ecl_nut == None:
            self._calc_ecl_nut()
        return self._ecl_nut

    def _get_planets(self):
        """Get chart planets.

        :rtype: results.PlanetDataList
        """
        if self._planets == None:
            self._calc_planets()
        return self._planets

    def _get_houses(self):
        """Get houses cusps.

        :rtype: results.HousesDataList
        """
        if self._houses == None:
            self._calc_houses()
        return self._houses

    def _get_aspects(self):
        """Get aspects list.

        :rtype: aspectsresults.AspectDataList
        """
        if self._aspects == None:
            self._calc_aspects()
        return self._aspects

    def _get_midpoints(self):
        """Get midpoints results.

        :rtype: results.MidPointDataList
        """
        if self._midpoints == None:
            self._calc_midpoints()
        return self._midpoints

    def _get_midp_aspects(self):
        """Get midpoints aspects.

        :rtype: aspectsresults.MidPointAspectDataList
        """
        if self._midp_aspects == None:
            self._calc_midp_aspects()
        return self._midp_aspects

    # from ChartFile
    path = property(ChartDate._get_path, ChartDate._set_path,
        doc='Chart file path.')
    name = property(ChartDate._get_name, ChartDate._set_name,
        doc='Chart name.')
    datetime = property(ChartDate._get_datetime, _set_datetime,
        doc='Chart date & time.')
    calendar = property(ChartDate._get_calendar, _set_calendar,
        doc="Chart calendar ('gregorian'|'julian').")
    location = property(ChartDate._get_location, ChartDate._set_location,
        doc='Chart location.')
    latitude = property(ChartDate._get_latitude, _set_latitude,
        doc='Chart latitude.')
    longitude = property(ChartDate._get_longitude, _set_longitude,
        doc='Chart longitude.')
    altitude = property(ChartDate._get_altitude, _set_altitude,
        doc='Chart altitude.')
    country = property(ChartDate._get_country, ChartDate._set_country,
        doc='Chart country.')
    zoneinfo = property(ChartDate._get_zoneinfo, _set_zoneinfo,
        doc='Chart posix zoneinfo.')
    timezone = property(ChartDate._get_timezone, _set_timezone,
        doc='Chart standard Utc timezone.')
    comment = property(ChartDate._get_comment, ChartDate._set_comment,
        doc='Chart comment.')
    keywords = property(ChartDate._get_keywords, ChartDate._set_keywords,
        doc='Chart keywords.')
    dst = property(ChartDate._get_dst, _set_dst,
        doc='Chart DST (None|True|False), for ambiguous datetime.')
    utcoffset = property(ChartDate._get_utcoffset, _set_utcoffset,
        doc='Chart UTC offset, in hours, for dates < 1900.')
    # from ChartDate
    julday = property(ChartDate._get_julday,
        doc='Chart Julian day.')
    local_datetime = property(ChartDate._get_local_datetime,
        doc='Chart local datetime.')
    utc_datetime = property(ChartDate._get_utc_datetime,
        doc='Chart Utc datetime.')
    local_mean_datetime = property(ChartDate._get_local_mean_datetime,
        doc='Chart local mean datetime.')
    sidtime = property(ChartDate._get_sidtime,
        doc='Chart Gmt sidereal time')
    local_sidtime = property(ChartDate._get_local_sidtime,
        doc='Chart local sidereal time.')
    # Additional properties
    filter = property(_get_filter, _set_filter,
        doc='Chart filter.')
    ecl_nut = property(_get_ecl_nut,
        doc='Obliquity and nutation values.')
    planets = property(_get_planets,
        doc='Planets positions.')
    houses = property(_get_houses,
        doc='Houses cusps.')
    aspects = property(_get_aspects,
        doc='Aspects.')
    midpoints = property(_get_midpoints,
        doc='Midpoints results.')
    midp_aspects = property(_get_midp_aspects,
        doc='Midpoints aspects.')

    def reset_positions(self):
        """Trigger recalculation of positions and aspects results."""
        self._ecl_nut = None
        self._planets = None
        self._aspects = None
        self._midpoints = None
        self._midp_aspects = None

    def _setup_swisseph(self):
        """Prepare swisseph for calculations."""
        f = self._filter
        # ephemeris type
        if f._ephe_type == 'swiss':
            swe.set_ephe_path(f._ephe_path)
        elif f._ephe_type == 'jpl':
            swe.set_jpl_file(f._ephe_path)
        # sidereal mode
        if f._sid_mode > -1:
            swe.set_sid_mode(f._sid_mode, f._sid_t0, f._sid_ayan_t0)
        # situation
        if f._xcentric == 'topo':
            swe.set_topo(float(self._longitude), float(self._latitude),
                self._altitude)

    def _calc_ecl_nut(self):
        """Calculate obliquity and nutation.

        Result is an unmodified swe.calc_ut tuple.

        """
        ##self._setup_swisseph()
        ##print self.julday
        self._ecl_nut = swe.calc_ut(self.julday, swe.ECL_NUT)

    def _calc_houses(self):
        """Calculate houses cusps."""
        self._setup_swisseph()
        cusps, ascmc = swe.houses_ex(self.julday, float(self._latitude),
            float(self._longitude), self._filter._hsys,
            self._filter.get_calcflag())
        self._houses = HousesDataList(cusps, ascmc, self._filter._hsys)

    def _calc_planets(self):
        """Calculate planets positions (but houses).

        Houses must be calculated first (for parts).

        """
        res = PlanetDataList() # results
        filt = self._filter._planets
        jd = self.julday
        flag = self._filter.get_calcflag()
        self._setup_swisseph()
        all_pl = all_planets()
        # get planets
        db.close() # fixstars_ut will overflow on sqlite buffers: close db.
        for k, v in filt.items():
            if v == False: # not this object
                continue
            p = all_pl[k]
            if p._family == 4: # houses, dont calc
                continue
            else:
                res.feed(p, p.calc_ut(jd, flag, self))
        db.connect() # fixstars_ut bug: reopen db
        # add cusps needed
        for h in self._houses:
            if filt[h._planet._name]:
                res.append(self._houses.get_data(h._planet._name))
        self._planets = res

    def _calc_aspects(self):
        """Calculate aspects.

        Planets must be calculated first.

        """
        res = AspectDataList() # results
        f = self._filter
        all = self._planets
        all_asp = all_aspects() #;print 'moo' # TODO: fixed stars bug here!?
        # begin calc
        for i, pos1 in enumerate(all.sort_by_ranking()):
            p1, lon1, lonsp1 = pos1._planet, pos1._longitude, pos1._lonspeed
            for pos2 in all[i+1:]:
                p2, lon2, lonsp2 = pos2._planet, pos2._longitude, pos2._lonspeed
                for asp, doasp in f._aspects.items():
                    if not doasp: # dont use this aspect
                        continue
                    if not f._asprestr[p1._name] or not f._asprestr[p2._name]:
                        continue # not this planet
                    asp = all_asp[asp]
                    # modify orb
                    orb = f._orbs[asp._name]
                    orbmod1 = f._orbrestr[p1._name].get_absolute(orb)
                    orbmod2 = f._orbrestr[p2._name].get_absolute(orb)
                    orb += (orbmod1 + orbmod2) / Decimal('2')
                    if orb < 0: # we'll never get such a precision
                        continue
                    # check aspect match
                    diff, apply, factor = swe._match_aspect2(
                        lon1, lonsp1, lon2, lonsp2,
                        float(asp._angle), float(orb))
                    if diff != None:
                        res.feed(pos1, pos2, asp, diff, apply, factor)
        self._aspects = res

    def _calc_midpoints(self):
        """Calculate midpoints.

        :todo: fetch houses results?
        """
        res = MidPointDataList() # results
        filt = self._filter._midpoints._planets
        jd = self.julday
        flag = self._filter.get_calcflag()
        self._setup_swisseph()
        all_pl = all_planets()
        # get all concerned planets, if not already calculated
        plres = PlanetDataList()
        for pl in [x for x in filt if filt[x]]:
            try:
                plres.append(self._planets.get_data(pl))
            except KeyError:
                p = all_pl[pl]
                plres.feed(p, p.calc_ut(jd, flag, self))
        # get midpoints
        plres.sort_by_ranking()
        for i, pos1 in enumerate(plres[:-1]):
            for pos2 in plres[i+1:]:
                if pos1._planet == pos2._planet:
                    continue
                res.feed(pos1, pos2,
                    (swe.deg_midp(pos1._longitude, pos2._longitude), # midp long
                        (pos1._latitude + pos2._latitude) / 2, # midp lat
                        (pos1._distance + pos2._distance) / 2, # midp dist
                        (pos1._lonspeed + pos2._lonspeed) / 2, # midp long speed
                        (pos1._latspeed + pos2._latspeed) / 2, # midp lat speed
                        (pos1._distspeed + pos2._distspeed) / 2) # midp dist speed
                    )
        self._midpoints = res

    def _calc_midp_aspects(self):
        """Calculate midpoints aspects."""
        res = MidPointAspectDataList() # results
        midpres = self._midpoints
        jd = self.julday
        flag = self._filter.get_calcflag()
        self._setup_swisseph()
        f = self._filter._midpoints
        all_pl = all_planets()
        all_asp = all_aspects()
        # get all concerned planets, if not already calculated
        plres = PlanetDataList()
        for pl in [x for x in f._planets if f._planets[x] and f._asprestr[x]]:
            try:
                plres.append(self._planets.get_data(pl))
            except KeyError:
                p = all_pl[pl]
                plres.feed(p, p.calc_ut(jd, flag, self))
        # get midp aspects
        plres.sort_by_ranking()
        for i, midp in enumerate(midpres):
            ##p1, p2 = midp._planet, midp._planet2
            lon1, lonsp1 = midp._longitude, midp._lonspeed
            for pos in plres:
                pl, lon2, lonsp2 = pos._planet, pos._longitude, pos._lonspeed
                for asp, doasp in f._aspects.items():
                    if not doasp: # dont use this aspect
                        continue
                    asp = all_asp[asp]
                    # modify orb
                    orb = f._orbs[asp._name]
                    #orbmod1 = plorbfilt[p1._name].get_absolute(orb)
                    orbmod1 = 0 # todo?: midp obrestr
                    orbmod2 = f._orbrestr[pl._name].get_absolute(orb)
                    orb += (orbmod1 + orbmod2) / Decimal('2')
                    if orb < 0: # we'll never get such a precision
                        continue
                    # check aspect match
                    diff, apply, factor = swe._match_aspect2(
                        lon1, lonsp1, lon2, lonsp2,
                        float(asp._angle), float(orb))
                    if diff != None:
                        res.feed(midp, pos, asp, diff, apply, factor)
        self._midp_aspects = res

    def calc(self):
        """Calculate all positions and aspects.

        Do midpoints if filter allows it.

        """
        self._calc_ecl_nut()
        self._calc_houses()
        self._calc_planets()
        self._calc_aspects()
        if self._filter._calc_midp:
            self._calc_midpoints()
            self._calc_midp_aspects()

    # transformations

    def multiply_pos(self, value):
        """Multiply planets positions (harmonics).

        Chart positions must be computed before.

        :see: calc()

        :type value: numeric
        """
        pl = PlanetDataList()
        value = float(value)
        for pos in self._planets:
            ##if pos._planet._family == 4: # houses
                ##continue
            pos._longitude = swe.degnorm(pos._longitude * value)
            pl.append(pos)
        self._planets = pl
        # recalc
        self._calc_aspects()
        if self._filter._calc_midp:
            self._calc_midpoints()
            self._calc_midp_aspects()

    def add_pos(self, value):
        """Add degrees to positions.

        Chart positions must be computed before.

        :see: calc()

        :type value: numeric
        """
        pl = PlanetDataList()
        value = float(value)
        for pos in self._planets:
            ##if pos._planet._family == 4: # houses
                ##continue
            pos._longitude = swe.degnorm(pos._longitude + value)
            pl.append(pos)
        self._planets = pl
        # recalc
        self._calc_aspects()
        if self._filter._calc_midp:
            self._calc_midpoints()
            self._calc_midp_aspects()

    # comparisons (transform planets positions relatively to another julian day)

    def progression_of(self, jd):
        """Make itself a progressed chart for some Julian day.

        :type jd: numeric
        """
        jd += swe._years_diff(jd, self.julday) # years as days
        flag = swe.GREG_CAL if self._calendar == 'gregorian' else swe.JUL_CAL
        y, mth, d, h, m, s = swe._revjul(jd, flag)
        old = self.datetime
        self.datetime = (y, mth, d, h, m, s)
        self.calc()
        # reset datetime
        self._reset_datetime()
        self._datetime = old

    def direction_of(self, jd):
        """Make itself a primary direction chart for some Julian day.

        :todo: to do...

        :type jd: numeric
        """
        pass

    def profection_of(self, op, value, unit, jd):
        """Transform positions to get profection for some Julian day.

            - Operator: 'add' -> addition, 'mul' -> multiplication
            - Units: 'year', 'day', 'hour'

        :todo: make it handle negative julian days

        :type op: str
        :type value: numeric
        :type unit: str
        :type jd: numeric
        :raise ValueError: invalid operator or unit
        """
        if unit == 'year':
            diff = swe._years_diff(jd, self.julday)
        elif unit == 1: # unit days - will fail if negatives
            diff = self.julday - jd
        elif unit == 2: # unit hours - will fail if negatives
            diff = (self.julday - jd) * 24.0
        else:
            raise ValueError('Invalid profection unit %s.' % unit)
        if op == 'add':
            self.add_pos(value * diff)
        elif op == 'mul':
            self.multiply_pos(value * diff)
        else:
            raise ValueError('Invalid profection operator %s.' % op)

    def __init__(self, path=None, set_default=True, do_calc=True):
        """Init chart object (and do calculations).

        :see: chartdate.ChartDate, chartfile.ChartFile

        :type path: str
        :type set_default: bool
        :type do_calc: bool
        """
        ChartDate.__init__(self, path, set_default)
        if set_default:
            self._filter = cfg.dft_filter
        else:
            self._filter = Filter()
        self.reset_positions()
        if do_calc:
            self.calc()

    def set(self, *args, **kwargs):
        """Set chart properties (incl. filter)."""
        if 'filter' in kwargs:
            self.filter = kwargs['filter']
            del(kwargs['filter'])
        ChartDate.set(self, *args, **kwargs)

    def dup(self, other):
        ChartDate.dup(self, other)
        self.reset_positions()

    def __iter__(self):
        """Iterate over chart properties.

        :rtype: iterator
        """
        return (x for x in (self._path, self._name, self._datetime,
            self._calendar, self._location, self._latitude, self._longitude,
            self._altitude, self._country, self._zoneinfo, self._timezone,
            self._comment, self._keywords, self._dst, self._utcoffset,
            self._julday, self._local_datetime, self._utc_datetime,
            self._local_mean_datetime, self._sidtime, self._local_sidtime,
            self._filter, self._ecl_nut, self._houses, self._planets,
            self._aspects, self._midpoints, self._midp_aspects))

    def __repr__(self):
        if self._path != None:
            return "ChartCalc('''%s''')" % self._path
        else:
            return repr(tuple(repr(x) for x in self))



def _test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()

# End.
