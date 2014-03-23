#!/sur/bin/env python
# -*- coding: utf-8 -*-

"""
Chart with date and time methods.

"""

from datetime import datetime, timedelta, time
from decimal import Decimal

import pytz
import swisseph as swe

from oroboros.core.chartfile import ChartFile


__all__ = ['ChartDate']


class ChartDate(ChartFile):
    """Chart with date and time methods.

    :see: chartfile.ChartFile

    Additional properties:

        - julday -> Julian day (float)
        - local_datetime -> aware datetime object, if zoneinfo is set
        - utc_datetime -> aware utc datetime object
        - local_mean_time -> naive local mean datetime object
        - sidtime -> gmt sidereal time (float)
        - local_sidtime -> local sidereal time, if mean time can be computed (time)

    In most situations, there is no need to set the 'dst' property.
    The zoneinfo system will try to guess if dst is active or not
    at that moment.
    But there is a rare case where it is up to the user to choose
    between dst (True) or standard time (False), usually when the
    savings time switches from dst to sdt. You can check this with
    the local_datetime property.

    The pytz module does not have time zone information for
    dates below 1900. In such case you must set the 'utcoffset'
    property with the correct value, the number of hours to add or
    to substract to get Universal Coordinated Time. There is no
    need to set 'dst', nor 'zoneinfo', because utcoffset takes
    precedance over them.

    """

    __slots__ = ChartFile.__slots__ + ['_julday', '_local_datetime',
        '_utc_datetime', '_local_mean_datetime', '_sidtime', '_local_sidtime']

    def _set_datetime(self, dt):
        ChartFile._set_datetime(self, dt)
        self._reset_datetime()

    def _set_calendar(self, cal):
        ChartFile._set_calendar(self, cal)
        self._reset_datetime()

    def _set_latitude(self, lat):
        ChartFile._set_latitude(self, lat)
        self._reset_datetime()

    def _set_longitude(self, lon):
        ChartFile._set_longitude(self, lon)
        self._reset_datetime()

    def _set_zoneinfo(self, tz):
        ChartFile._set_zoneinfo(self, tz)
        self._reset_datetime()

    def _set_timezone(self, tz):
        ChartFile._set_timezone(self, tz)
        self._reset_datetime()

    def _set_dst(self, dst):
        ChartFile._set_dst(self, dst)
        self._reset_datetime()

    def _set_utcoffset(self, hours):
        ChartFile._set_utcoffset(self, hours)
        self._reset_datetime()

    def _get_dst(self):
        """Get daylight savings time flag.

        Return True if daylight savings time is on, False if off.

        :rtype: bool
        :raise ValueError: date is ambiguous and user did not set DST info
        """
        if self._dst == None: # try to guess
            dst = self.local_datetime.dst()
            if dst == None: # utcoffset has taken precedance
                return False
            elif dst.seconds == 0:
                return False
            else:
                return True
        else: # user-defined DST
            return self._dst

    def _get_utcoffset(self):
        """Get UTC offset (hours to add to Utc to get local time).

        If utcoffset is not set, try to guess based on zoneinfo.
        Return offset in hours.
        Raise ValueError if zoneinfo is missing to get utcoffset.

        :rtype: float
        :raise ValueError: missing zoneinfo
        """
        if self._utcoffset != None:
            return self._utcoffset
        else: # guess
            if self._zoneinfo in (None, ''):
                raise ValueError('Missing zoneinfo.')
            tz = pytz.timezone(self._zoneinfo)
            dt = tz.localize(self._datetime)
            delta = (dt.utcoffset().seconds) / 3600.0
            return delta

    # Additional properties

    def _get_julday(self):
        """Get Julian day.

        :rtype: float
        """
        if self._julday == None:
            self._julday = self._calc_julday()
        return self._julday

    def _get_local_datetime(self):
        """Get local datetime (tz aware).

        :rtype: datetime
        """
        if self._local_datetime == None:
            self._local_datetime = self._calc_local_datetime()
        return self._local_datetime

    def _get_utc_datetime(self):
        """Get utc datetime (tz aware).

        :rtype: datetime
        """
        if self._utc_datetime == None:
            self._utc_datetime = self._calc_utc_datetime()
        return self._utc_datetime

    def _get_local_mean_datetime(self):
        """Get local mean time (tz naive).

        :rtype: datetime
        """
        if self._local_mean_datetime == None:
            self._local_mean_datetime = self._calc_local_mean_datetime()
        return self._local_mean_datetime

    def _get_sidtime(self):
        """Get gmt sidereal time.

        :rtype: float
        """
        if self._sidtime == None:
            self._sidtime = self._calc_sidtime()
        return self._sidtime

    def _get_local_sidtime(self):
        """Get local sidereal time.

        :rtype: time
        """
        if self._local_sidtime == None:
            self._local_sidtime = self._calc_local_sidtime()
        return self._local_sidtime

    path = property(ChartFile._get_path, ChartFile._set_path,
        doc='Chart file path.')
    name = property(ChartFile._get_name, ChartFile._set_name,
        doc='Chart name.')
    datetime = property(ChartFile._get_datetime, _set_datetime,
        doc='Chart date & time.')
    calendar = property(ChartFile._get_calendar, _set_calendar,
        doc="Chart calendar ('gregorian'|'julian').")
    location = property(ChartFile._get_location, ChartFile._set_location,
        doc='Chart location.')
    latitude = property(ChartFile._get_latitude, ChartFile._set_latitude,
        doc='Chart latitude.')
    longitude = property(ChartFile._get_longitude, _set_longitude,
        doc='Chart longitude.')
    altitude = property(ChartFile._get_altitude, ChartFile._set_altitude,
        doc='Chart altitude.')
    country = property(ChartFile._get_country, ChartFile._set_country,
        doc='Chart country.')
    zoneinfo = property(ChartFile._get_zoneinfo, _set_zoneinfo,
        doc='Chart posix zoneinfo.')
    timezone = property(ChartFile._get_timezone, _set_timezone,
        doc='Chart standard Utc timezone.')
    comment = property(ChartFile._get_comment, ChartFile._set_comment,
        doc='Chart comment.')
    keywords = property(ChartFile._get_keywords, ChartFile._set_keywords,
        doc='Chart keywords.')
    dst = property(_get_dst, _set_dst,
        doc='Chart DST (None|True|False), for ambiguous datetime.')
    utcoffset = property(_get_utcoffset, _set_utcoffset,
        doc='Chart UTC offset, in hours, for dates < 1900.')
    # Additional (read-only)
    julday = property(_get_julday,
        doc='Chart Julian day.')
    local_datetime = property(_get_local_datetime,
        doc='Chart local datetime.')
    utc_datetime = property(_get_utc_datetime,
        doc='Chart Utc datetime.')
    local_mean_datetime = property(_get_local_mean_datetime,
        doc='Chart local mean datetime.')
    sidtime = property(_get_sidtime,
        doc='Chart Gmt sidereal time')
    local_sidtime = property(_get_local_sidtime,
        doc='Chart local sidereal time.')

    def _reset_datetime(self):
        """Trigger recalculation of date and time dependant info."""
        self._julday = None
        self._local_datetime = None
        self._utc_datetime = None
        self._local_mean_datetime = None
        self._sidtime = None
        self._local_sidtime = None

    def _calc_julday(self):
        """Get chart Julian day number, based on local datetime and zoneinfo.

        For ambiguous dates, set the 'dst' property.
        For dates below 1900, set the 'utcoffset' property only.

        :rtype: float
        """
        utc_dt = self.utc_datetime
        hour = utc_dt.hour + (utc_dt.minute / 60.0) + (utc_dt.second / 3600.0)
        if self.calendar in ('gregorian', None):
            jd = swe.date_conversion(utc_dt.year, utc_dt.month, utc_dt.day, hour)
        elif calendar == 'julian':
            jd = swe.date_conversion(utc_dt.year, utc_dt.month, utc_dt.day, hour, 'j')
        self._julday = jd[1] # further reading
        return self._julday

    def _calc_utc_datetime(self):
        """Get UTC datetime, based on local datetime.

        Return datetime object with UTC zoneinfo.
        For ambiguous dates, set the 'dst' property.
        For dates below 1900, set the 'utcoffset' property only.

        :rtype: datetime
        """
        if self._utcoffset != None: # user-defined, below 1900
            tdelta = timedelta(hours=abs(self._utcoffset))
            if self._utcoffset >= 0:
                utc_dt = self._datetime - tdelta
            else:
                utc_dt = self._datetime + tdelta
            utc_dt = pytz.utc.localize(utc_dt)
        else: # use zoneinfo and local datetime
            utc_dt = self.local_datetime.astimezone(pytz.utc)
        self._utc_datetime = utc_dt # further reading
        return utc_dt

    def _calc_local_datetime(self):
        """Get local datetime, with timezone info.

        Return datetime object, with given zoneinfo.
        If no zoneinfo is set, consider it is UTC.
        For ambiguous dates, set the 'dst' property.
        For dates below 1900, set the 'utcoffset' property only.
        In this case the datetime contains no zone information.

        :rtype: datetime
        :raise ValueError: datetime is ambiguous
        """
        if self._utcoffset != None: # user-defined, below 1900
            loc_dt = self._datetime
        else: # use zoneinfo and datetime
            if self._zoneinfo == None: # assume it is utc
                loc_dt = pytz.utc.localize(self._datetime)
            else: # zoneinfo is set
                tz = pytz.timezone(self._zoneinfo)
                if self._dst != None: # user-defined, ambiguous
                    loc_dt = tz.localize(dt, is_dst=self._dst)
                else: # check for ambiguous datetime
                    loc_dt = tz.localize(self._datetime)
                    loc_dt_dst = tz.localize(self._datetime, is_dst=True)
                    if loc_dt != loc_dt_dst:
                        raise ValueError('Ambiguous datetime. Please set DST.')
        self._local_datetime = loc_dt # further reading
        return loc_dt

    def _calc_local_mean_datetime(self):
        """Get local mean datetime.

        If timezone is not set, we're unable to compute local mean time.
        Longitude must of course be correct.

        :rtype: datetime
        :raise ValueError: missing timezone
        """
        if self._timezone == None:
            raise ValueError('Missing timezone.')
        # get longitude correction
        diff = Decimal(str(self._timezone.longitude)) - (
            self._longitude.to_decimal()) # degree arc difference
        diff = diff * Decimal('240.0') # diff in time (seconds)
        delta = timedelta(seconds=float(diff))
        # get dst correction
        loc_dt = self.local_datetime
        dst = timedelta(seconds=loc_dt.tzinfo.dst(loc_dt).seconds)
        loc_mtime = loc_dt - (delta + dst)
        loc_mtime = datetime(*loc_mtime.timetuple()[:6])
        self._local_mean_datetime = loc_mtime # further reading
        return loc_mtime

    def _calc_sidtime(self):
        """Get sidereal time at gmt.

        :rtype: float
        """
        sidt = swe.sidtime(self.julday)
        self._sidtime = sidt # further reading
        return sidt

    def _calc_local_sidtime(self):
        """Get local sidereal time.

        :todo: wipe bugs

        :rtype: time
        """
        # midnight gmt sidtime
        y, mth, d, h, m, s = self.local_mean_datetime.timetuple()[:6]
        jd = swe._julday(y, mth, d)
        midn = swe.sidtime(jd)
        midn = swe.split_deg(midn, 0)
        midn = datetime(2000, 1, 1, hour=midn[0], minute=midn[1], second=midn[2],
            microsecond=int(1.0000000000000001e-05 * midn[3]))
        # time with acceleration correction
        tm = timedelta(hours=1.002737909 * (h + m/60.0 + s/3600.0))
        # with tz correction
        corrtz = timedelta(seconds=10.0 * (self._timezone.longitude/15.0))
        loc_sidt = midn + (tm - corrtz)
        # southern -- commented
        ##if self._latitude._direction == 'S':
        ##  loc_sidt += timedelta(hours=12)
        loc_sidt = time(hour=loc_sidt.hour, minute=loc_sidt.minute,
            second=loc_sidt.second)
        self._local_sidtime = loc_sidt # further reading
        return loc_sidt

    def __init__(self, path=None, set_default=True):
        ChartFile.__init__(self, path, set_default)
        self._reset_datetime()

    def dup(self, other):
        ChartFile.dup(self, other)
        self._reset_datetime()

    def _from_xml(self, elem):
        ChartFile._from_xml(self, elem)
        self._reset_datetime()

    def __iter__(self):
        """Iterate over chart properties.

        :rtype: iterator
        """
        return (x for x in (self._path, self._name, self._datetime,
            self._calendar, self._location, self._latitude, self._longitude,
            self._altitude, self._country, self._zoneinfo, self._timezone,
            self._comment, self._keywords, self._dst, self._utcoffset,
            self._julday, self._local_datetime, self._utc_datetime,
            self._local_mean_datetime, self._sidtime, self._local_sidtime))

    def __repr__(self):
        if self._path != None:
            return "ChartDate('''%s''')" % self._path
        else:
            return repr(tuple(repr(x) for x in self))



def _test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    _test()

# End.
