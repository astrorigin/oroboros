#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Chart file objects (minimal chart objects).

Use this if you dont need calculations but file parsing only.
Basicly, all information written in xml format is handled here.

    >>> cht = ChartFile()
    >>> cht.name = 'Tom Cruise'
    >>> cht.datetime = '1962-07-03 12:05:0'
    >>> cht.zoneinfo = 'America/New_York'
    >>> cht.location = 'Syracuse (NY)'
    >>> cht.latitude = '43:N:2:53'
    >>> cht.longitude = '76:W:8:50'
    >>> cht.altitude = 129
    >>> cht.country = 'USA'
    >>> cht.timezone = 'UTC-5'
    >>> cht.set_keyword('Gender', 'M')
    >>> cht.set_keyword('Type', 'Natal')
    >>> cht.path = './Tom Cruise.xml'
    >>> cht.write()
    True
    >>> cht2 = ChartFile('./Tom Cruise.xml')
    >>> print(cht2.name)
    Tom Cruise
    >>> cht2.comment = 'copy me!'
    >>> cht.dup(cht2)
    >>> cht.path is None
    True
    >>> print(cht.comment)
    copy me!
    >>> cht2.remove()

"""

import os.path
from datetime import datetime

import pytz

from oroboros.core import cfg
from oroboros.core import geocoords
from oroboros.core import timezone
from oroboros.core import xmlutils
from oroboros.core.kwdict import KeywordsDict


__all__ = ['ChartFile']


class ChartFile(object):
    """Chart file object.

    Properties:

      - path -> file path (str)
      - name -> chart name (str)
      - datetime -> naive datetime object (civilian info)
      - calendar -> calendar type ('gregorian'|'julian')
      - location -> location/city (str)
      - latitude -> Latitude object
      - longitude -> Longitude object
      - altitude -> Altitude object
      - country -> country name (str)
      - zoneinfo -> posix time zone file (see pytz module)
      - timezone -> standard utc timezone (see timezone module)
      - comment -> user's comments (str)
      - keywords -> user's keywords (kwdict.KeywordsDict object)

    Optional properties:

      - dst -> daylight savings time flag (None|True|False),
        for ambiguous datetime only
      - utcoffset -> offset with Universal Coord. Time (incl. dst)
        for dates before 1900 only

    """

    __slots__ = ['_path', '_name', '_datetime', '_calendar', '_location',
        '_latitude', '_longitude', '_altitude', '_country', '_zoneinfo',
        '_timezone', '_comment', '_keywords', '_dst', '_utcoffset']


    def _get_path(self):
        """Get chart file path (None -> no file).

        :rtype: str or None
        """
        return self._path

    def _set_path(self, path=None):
        """Set chart file path (None, empty str -> no file).

        :type path: str or None
        """
        if path not in (None, ''):
            self._path = os.path.abspath(os.path.expanduser(path))
        else:
            self._path = None

    def _get_name(self):
        """Get chart name.

        :rtype: str
        """
        return self._name

    def _set_name(self, name=''):
        """Set chart name.

        :type name: str
        """
        if not isinstance(name, unicode):
            self._name = name.decode('utf-8')
        else:
            self._name = name

    def _get_datetime(self):
        """Get chart date and time.

        :rtype: datetime
        """
        return self._datetime

    def _set_datetime(self, dt):
        """Set chart date and time.

        Accepts datetime objects,
        or a tuple with year/month/day/hour/min/sec,
        or a string in a format like '2001-12-31 12:0:0'.

        This is a naive datetime object, without timezone or daylight savings
        time information.

        :see: zoneinfo property

        :param dt: date and time information
        :type dt: datetime or sequence or str
        :raise TypeError: dt has an invalid type
        """
        if isinstance(dt, datetime):
            self._datetime = dt
        elif isinstance(dt, (tuple, list)):
            self._datetime = datetime(*dt)
        elif isinstance(dt, str):
            self._datetime = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
        else:
            raise TypeError('Invalid datetime %s.' % dt)

    def _get_calendar(self):
        """Get chart calendar type.

        :return: calendar type, 'gregorian' or 'julian'
        :rtype: str
        """
        return self._calendar

    def _set_calendar(self, cal):
        """Set chart calendar type.

        Gregorian calendar -> 'gregorian'
        Julian calendar -> 'julian'

        :param cal: calendar type
        :type cal: str
        :raise TypeError: calendar is invalid
        """
        if cal in ('gregorian', 'julian'):
            self._calendar = cal
        else:
            raise TypeError('Invalid calendar %s.' % cal)

    def _get_location(self):
        """Get chart location/city (without country).

        :rtype: str
        """
        return self._location

    def _set_location(self, location):
        """Set chart location/city (without country).

        :type location: str
        """
        if not isinstance(location, unicode):
            self._location = location.decode('utf8')
        else:
            self._location = location

    def _get_latitude(self):
        """Get chart latitude.

        :rtype: oroboros.geocoords.Latitude
        """
        return self._latitude

    def _set_latitude(self, lat):
        """Set chart latitude.

        Accepts Latitude objects,
        or tuple with degrees/direction/minutes/seconds,
        or string with ':'-separated values, like '46:N:32:0'.

        :param lat: latitude
        :type lat: geocoords.Latitude or sequence or str
        :raise TypeError: latitude is invalid
        """
        if isinstance(lat, geocoords.Latitude):
            self._latitude = lat
        elif isinstance(lat, (tuple, list)):
            self._latitude = geocoords.Latitude(*lat)
        elif isinstance(lat, str):
            self._latitude = geocoords.Latitude(*lat.split(':'))
        else:
            raise TypeError('Invalid latitude %s.' % lat)

    def _get_longitude(self):
        """Get chart longitude.

        :rtype: geocoords.Longitude
        """
        return self._longitude

    def _set_longitude(self, lon):
        """Set chart longitude.

        Accepts Longitude objects,
        or tuple with degrees/direction/minutes/seconds,
        or string with ':'-separated values, like '6:E:55:0'.

        :param lon: longitude
        :type lon: geocoords.Longitude or list or str
        :raise TypeError: longitude is invalid
        """
        if isinstance(lon, geocoords.Longitude):
            self._longitude = lon
        elif isinstance(lon, (tuple, list)):
            self._longitude = geocoords.Longitude(*lon)
        elif isinstance(lon, str):
            self._longitude = geocoords.Longitude(*lon.split(':'))
        else:
            raise TypeError('Invalid longitude %s.' % lon)

    def _get_altitude(self):
        """Get chart altitude.

        :rtype: geocoords.Altitude
        """
        return self._altitude

    def _set_altitude(self, alt):
        """Set chart altitude.

        :type alt: geocoords.Altitude or numeric value >= 0
        """
        if isinstance(alt, geocoords.Altitude):
            self._altitude = alt
        else:
            self._altitude = geocoords.Altitude(alt)

    def _get_country(self):
        """Get chart country.

        :rtype: str
        """
        return self._country

    def _set_country(self, country):
        """Set chart country.

        :type country: str
        """
        if not isinstance(country, unicode):
            self._country = country.decode('utf8')
        else:
            self._country = country

    def _get_zoneinfo(self):
        """Get chart zoneinfo file.

        :rtype: str or None
        """
        return self._zoneinfo

    def _set_zoneinfo(self, tz):
        """Set chart zoneinfo file.

        Accepts a pytz timezone file,
        or None/empty str/'None' (which default to UTC).

        :see: pytz module

        :type tz: str or None
        :raise TypeError: zoneinfo is invalid
        """
        if tz not in (None, 'None', '') and tz not in pytz.all_timezones:
            raise TypeError('Invalid zoneinfo %s.' % tz)
        self._zoneinfo = tz if tz not in ('None', None, '') else None

    def _get_timezone(self):
        """Get chart timezone object.

        :rtype: timezone.TimeZone or None (unknown)
        """
        return self._timezone

    def _set_timezone(self, tz):
        """Set chart timezone object.

        Accepts utc names or TimeZone objects,
        or None if unknown.

        This is used to calculate local mean time and sidereal time.
        If not set, local mean time and sidereal time may not be computed.

        :see: oroboros.timezone module

        :type tz: str or timezone.TimeZone or None
        :raise ValueError: TimeZone is not accepted
        """
        if tz in ('None', None, ''):
            self._timezone = None
        else:
            if not isinstance(tz, timezone.TimeZone):
                tz = timezone.get(tz)
            elif tz not in timezone.all_timezones:
                raise ValueError('Invalid timezone %s.' % tz)
            self._timezone = tz

    def _get_comment(self):
        """Get chart comment.

        :rtype: str
        """
        return self._comment

    def _set_comment(self, comment):
        """Set chart comment.

        :type comment: str
        """
        if not isinstance(comment, unicode):
            self._comment = comment.decode('utf-8')
        else:
            self._comment = comment

    def _get_keywords(self):
        """Get chart keywords.

        :rtype: kwdict.KeywordsDict
        """
        return self._keywords

    def _set_keywords(self, kwstr=''):
        """Set chart keywords dict with a string.

        Input string is like "key:value;key:value"

        :type kwstr: str
        """
        self._keywords = KeywordsDict(kwstr)

    def _get_dst(self):
        """get chart daylight savings time flag.

        None -> not needed, True -> dst on, False -> dst off.

        :rtype: None or bool
        """
        return self._dst

    def _set_dst(self, dst=None):
        """Set chart daylight savings time flag.

        For non-ambiguous dates, just let it be None.

        :see: pytz module, zoneinfo property

        :param dst: daylight savings time flag
        :type dst: None or bool (or boolean equivalent)
        """
        if dst in (True, '1', 1, 'True', 'true', 'yes'):
            self._dst = True
        elif dst in (False, '0', 0, 'False', 'false', 'no'):
            self._dst = False
        elif dst in (None, ''):
            self._dst = None
        else:
            raise TypeError('Invalid DST %s.' % dst)

    def _get_utcoffset(self):
        """Get UTC offset (hours to add to Utc to get local time).

        :rtype: float or None (not needed)
        """
        return self._utcoffset

    def _set_utcoffset(self, hours=None):
        """Set UTC offset (hours to add to Utc to get local time).

        :type hours: numeric or None (not needed)
        """
        if hours in (None, ''):
            self._utcoffset = None
        else:
            self._utcoffset = float(hours)

    path = property(_get_path, _set_path,
        doc='Chart file path.')
    name = property(_get_name, _set_name,
        doc='Chart name.')
    datetime = property(_get_datetime, _set_datetime,
        doc='Chart date & time.')
    calendar = property(_get_calendar, _set_calendar,
        doc="Chart calendar ('gregorian'|'julian').")
    location = property(_get_location, _set_location,
        doc='Chart location.')
    latitude = property(_get_latitude, _set_latitude,
        doc='Chart latitude.')
    longitude = property(_get_longitude, _set_longitude,
        doc='Chart longitude.')
    altitude = property(_get_altitude, _set_altitude,
        doc='Chart altitude.')
    country = property(_get_country, _set_country,
        doc='Chart country.')
    zoneinfo = property(_get_zoneinfo, _set_zoneinfo,
        doc='Chart posix zoneinfo.')
    timezone = property(_get_timezone, _set_timezone,
        doc='Chart standard Utc timezone.')
    comment = property(_get_comment, _set_comment,
        doc='Chart comment.')
    keywords = property(_get_keywords, _set_keywords,
        doc='Chart keywords.')
    dst = property(_get_dst, _set_dst,
        doc='Chart DST (None|True|False), for ambiguous datetime.')
    utcoffset = property(_get_utcoffset, _set_utcoffset,
        doc='Chart UTC offset, in hours, for dates < 1900.')

    def set(self, path=None, name=None, datetime=None, calendar=None,
        location=None, latitude=None, longitude=None, altitude=None,
        country=None, zoneinfo=None, timezone=None, comment=None,
        keywords=None, dst=None, utcoffset=None):
        """Set chart properties.

        For arguments needing to be set to None, pass empty string ('').

        """
        if path != None:
            self.path = path
        if name != None:
            self.name = name
        if datetime != None:
            self.datetime = datetime
        if calendar != None:
            self.calendar = calendar
        if location != None:
            self.location = location
        if latitude != None:
            self.latitude = latitude
        if longitude != None:
            self.longitude = longitude
        if altitude != None:
            self.altitude = altitude
        if country != None:
            self.country = country
        if zoneinfo != None:
            self.zoneinfo = zoneinfo
        if timezone != None:
            self.timezone = timezone
        if comment != None:
            self.comment = comment
        if keywords != None:
            self.keywords = keywords
        if dst != None:
            self.dst = dst
        if utcoffset != None:
            self.utcoffset = utcoffset

    def __init__(self, path=None, set_default=True):
        """Load or create a (default) chart.

        :type path: str or None
        :type set_default: bool
        """
        if path != None:
            self.parse(path)
        elif set_default:
            self.set_default()
        else:
            self._path = None
            self._name = '<?>'
            self._datetime = datetime.utcnow().replace(microsecond=0)
            self._calendar = 'gregorian'
            self._location = '<?>'
            self._latitude = geocoords.Latitude()
            self._longitude = geocoords.Longitude()
            self._altitude = geocoords.Altitude()
            self._country = '<?>'
            self._zoneinfo = None
            self._timezone = None
            self._comment = ''
            self._keywords = KeywordsDict()
            self._dst = None
            self._utcoffset = None

    def set_default(self):
        """Set chart to defaults according to configuration.

        :see: oroboros.core.cfg module
        """
        self._path = None
        self._name = cfg.dft_name
        self._datetime = datetime.utcnow().replace(microsecond=0)
        self._calendar = 'gregorian'
        self._location = cfg.dft_location
        self._latitude = cfg.dft_latitude
        self._longitude = cfg.dft_longitude
        self._altitude = cfg.dft_altitude
        self._country = cfg.dft_country
        self._zoneinfo = cfg.dft_zoneinfo
        self._timezone = cfg.dft_timezone
        self._comment = cfg.dft_comment
        self._keywords = KeywordsDict()
        self._dst = None
        self._utcoffset = None
        # set datetime to local time
        if self._zoneinfo not in ('UTC', 'utc'):
            dt = pytz.utc.localize(self._datetime)
            tz = pytz.timezone(self._zoneinfo)
            self._datetime = dt.astimezone(tz)
            self._datetime = datetime(*self._datetime.timetuple()[:6])

    def parse(self, path):
        """Load a chart from xml file.

        :type path: str
        """
        path = os.path.abspath(os.path.expanduser(path))
        el = xmlutils.parse(path)
        self._from_xml(el)
        self._path = path

    def dup(self, other):
        """Copy another chart properties (but file path).

        :type other: any chart type
        """
        self._path = None
        self._name = other._name
        self._datetime = other._datetime
        self._calendar = other._calendar
        self._location = other._location
        self._latitude = other._latitude
        self._longitude = other._longitude
        self._altitude = other._altitude
        self._country = other._country
        self._zoneinfo = other._zoneinfo
        self._timezone = other.timezone
        self._comment = other._comment
        self._keywords = other._keywords
        self._dst = other._dst
        self._utcoffset = other._utcoffset

    def write(self, overwrite=True):
        """Write (save) chart in xml file.

        :type overwrite: bool
        :rtype: bool
        :raise TypeError: path is None
        """
        if self._path == None:
            raise TypeError('Missing path.')
        if not overwrite and os.path.exists(self._path):
            return False
        xml = self._to_xml()
        xml.write(self._path)
        return True

    def remove(self):
        """Remove (delete) xml file."""
        os.remove(self._path) # may raise OSError
        self._path = None

    def get_keyword(self, key):
        """Get chart keyword value.

        :type key: str
        :rtype: str
        """
        return self._keywords[key]

    def set_keyword(self, key, word):
        """Set a chart keyword.

        :type key: str
        :type word: str
        """
        self._keywords[key] = word

    def del_keyword(self, key):
        """Delete a chart keyword.

        :type key: str
        """
        del(self._keywords[key])

    def _to_xml(self):
        """Return chart as an xmlutils element.

        :rtype: xmlutils.Element
        """
        el = xmlutils.Element('ASTROLOGY', {'software': 'Oroboros'},
            text='\n', tail='\n')
        # comments
        cmt = xmlutils.comment(
            'Generated by Oroboros, %s UTC' % datetime.utcnow().replace(microsecond=0))
        cmt.tail = '\n'
        el.append(_etree_elem=cmt)
        cmt = xmlutils.comment('For user: %s %s' % (cfg.username, cfg.usermail))
        cmt.tail = '\n\t'
        el.append(_etree_elem=cmt)
        # data
        el.append('NAME', text=self.name, tail='\n\t')
        el.append('DATETIME',
            {'calendar': self._calendar if self._calendar != None else '',
                'utcoffset': self._utcoffset if self._utcoffset != None else '',
                'dst': self._dst if self._dst != None else ''},
            self.datetime,
            '\n\t')
        el.append('LOCATION',
            {'latitude': str(self._latitude),
                'longitude': str(self._longitude),
                'altitude': self._altitude},
            self._location,
            '\n\t')
        el.append('COUNTRY',
            {'zoneinfo': self._zoneinfo,
                'timezone': self._timezone.utc if self._timezone != None else ''},
            self._country,
            '\n\t')
        el.append('COMMENT', text=self._comment, tail='\n\t')
        el.append('KEYWORDS', self._keywords, tail='\n')
        return el

    def _from_xml(self, elem):
        """Load properties from xmlutils element.

        :type elem: xmlutils.Element
        """
        self.name = elem.get_child_text(tag='NAME').replace('&lt;',
            '<').replace('&gt;', '>')
        dt = elem.get_child(tag='DATETIME')
        self.datetime = dt.text
        self.calendar = dt.get_attr('calendar')
        self.utcoffset = dt.get_attr('utcoffset')
        self.dst = dt.get_attr('dst')
        loc = elem.get_child(tag='LOCATION')
        self.location = loc.text
        self.altitude = loc.get_attr('altitude')
        self.latitude = loc.get_attr('latitude')
        self.longitude = loc.get_attr('longitude')
        cty = elem.get_child(tag='COUNTRY')
        self.country = cty.text
        self.zoneinfo = cty.get_attr('zoneinfo')
        self.timezone = cty.get_attr('timezone')
        self.comment = elem.get_child_text(tag='COMMENT').replace('&lt;',
            '<').replace('&gt;', '>')
        kw = KeywordsDict()
        for k, v in elem.get_child(tag='KEYWORDS').attributes.items():
            kw[k] = v
        self._keywords = kw

    def __iter__(self):
        """Iterate over chart properties.

        :rtype: iterator
        """
        return (x for x in (self._path, self._name, self._datetime,
            self._calendar, self._location, self._latitude, self._longitude,
            self._altitude, self._country, self._zoneinfo, self._timezone,
            self._comment, self._keywords, self._dst, self._utcoffset))

    def __str__(self):
        return str(tuple(self))

    def __repr__(self):
        if self._path != None:
            return "ChartFile('''%s''')" % self._path
        else:
            return repr(tuple(repr(x) for x in self))



def _test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    _test()

# End.
