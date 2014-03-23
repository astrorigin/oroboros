#!/usr/bin/env pythno
# -*- coding: utf-8 -*-

"""
GeoNames.org search system.

"""

import urllib

from oroboros.core import xmlutils
from oroboros.core import geocoords


__all__ = ['search']


def query(url):
	"""Query GeoNames.org webservice.
	
	:type url: str
	:rtype: file-like
	:raise ValueError: query failed
	"""
	try:
		f = urllib.urlopen(url)
	except:
		#raise
		raise ValueError('Unable to query geonames %s.' % url)
	return f


def search(name):
	"""Query GeoNames.org.
	
	Return a list of tuples (name, country, lat, lon, elev, timezone)
	
	:type name: str
	:rtype: list
	"""
	url = 'http://ws.geonames.org/search?q=%s&featureClass=P&style=FULL'
	f = query(url % urllib.quote(name))
	xml = xmlutils.parse(f)
	try:
		f.close()
	except:
		pass
	ret = list()
	all = xml.get_iterator('geoname')
	for a in all:
		lat = geocoords.Latitude()
		lon = geocoords.Longitude()
		dlat = float(a.get_child_text(tag='lat'))
		dlon = float(a.get_child_text(tag='lng'))
		lat.from_decimal(dlat)
		lon.from_decimal(dlon)
		elev = get_elevation(dlat, dlon)
		ret.append((a.get_child_text(tag='name'),
			a.get_child_text(tag='countryName'),
			lat, lon, elev,
			a.get_child_text(tag='timezone')))
	return ret


def get_elevation(lat, lon):
	"""Get elevation (altitude) for a place.
	
	:type lat: numeric
	:type lon: numeric
	:rtype: Altitude
	"""
	if lat > 60 or lat < -66: # use gtopo30
		url = 'http://ws.geonames.org/gtopo30?lat=%s&lng=%s'
	else: # use srtm3
		url = 'http://ws.geonames.org/srtm3?lat=%s&lng=%s'
	f = query(url % (lat, lon))
	elev = int(f.read().strip())
	try:
		f.close()
	except:
		pass
	if elev < 0:
		elev = 0
	return geocoords.Altitude(elev)



def _test():
	import doctest
	doctest.testmod()


if __name__ == '__main__':
	_test()

# End.
