#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Import Skif charts.

"""

import os.path

from oroboros.core.charts import Chart
from oroboros.core import xmlutils


__all__ = ['load']


def load(path):
	"""Load skif and return chart object (not calculated).
	
	:type path: str
	:rtype: Chart
	"""
	path = os.path.abspath(os.path.expanduser(path))
	f = xmlutils.parse(path)
	data = f.get_child(tag='DATASET')
	# name
	name = data.get_child_text(tag='NAME')
	# datetime
	year = int(data.get_child_attr('Year', tag='DATE'))
	month = int(data.get_child_attr('Month', tag='DATE'))
	day = int(data.get_child_attr('Day', tag='DATE'))
	hm = data.get_child_attr('Hm', tag='DATE')
	hour, minute = [int(x) for x in hm.split(':')]
	datetime = (year, month, day, hour, minute, 0)
	# location
	location = data.get_child_text(tag='PLACE')
	# country
	country = data.get_child_text(tag='COUNTRY')
	# zoneinfo, utcoffset, dst
	zoneinfo = data.get_child_attr('ZoneInfoFile', tag='COUNTRY')
	if zoneinfo == '': # need utcoffset
		utcoff = data.get_child_attr('Timezone', tag='DATE')
		h, m = [int(x) for x in utcoff.split(':')]
		utcoffset = -(h + (m / 60.0))
	else:
		utcoffset = ''
	if data.get_child_attr('Daylight', tag='DATE') != '0:00':
		dst = True
	else:
		dst = False
	# adjust utc offset
	if utcoffset != '':
		if dst == True:
			utcoffset -= 1
	# geocoords
	lat = data.get_child_attr('Latitude', tag='PLACE')
	latdg, latmn = lat[:-1].split(':')
	latdr = lat[-1]
	latitude = (int(latdg), latdr, int(latmn), 0)
	lon = data.get_child_attr('Longitude', tag='PLACE')
	londg, lonmn = lon[:-1].split(':')
	londr = lon[-1]
	longitude = (int(londg), londr, int(lonmn), 0)
	# comments
	comment = 'Imported from Skylendar.\n'
	comment += 'Chart type: %s\n' % data.get_child_text(tag='TYPE')
	comment += 'Gender: %s\n' % data.get_child_attr('Gender', tag='TYPE')
	comment += 'Keywords: %s\n' % data.get_child_text(tag='KEYWORDS')
	comment += 'Comment: %s' % data.get_child_text(tag='COMMENT')
	# ...
	cht = Chart(set_default=False, do_calc=False)
	cht.set(name=name, datetime=datetime, location=location, country=country,
		zoneinfo=zoneinfo, dst=dst, utcoffset=utcoffset, latitude=latitude,
		longitude=longitude, altitude=0, comment=comment)
	return cht


# End.
