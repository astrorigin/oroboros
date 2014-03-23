#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Import astrolog32 files.

"""

import os.path

from oroboros.core.charts import Chart


__all__ = ['load']



def load(path):
	"""Load an astrolog32 file. Return chart (no positions calculated).
	
	:rtype: Chart
	"""
	path = os.path.abspath(os.path.expanduser(path))
	f = file(path)
	lines = f.read().split('\n')
	f.close()
	for line in [x.strip() for x in lines]:
		if not line.startswith('/'):
			continue
		if line.startswith('/qb'):
			line = line[4:]
			# get date and time, latitude, longitude
			prts = line.split(' ')
			parts = list()
			for i, p in enumerate(prts):
				if p != '':
					parts.append(p)
			# datetime
			mth, d, y, time, stdt, offset, lon, lat = parts
			h, m, s = time.split(':')
			dt = [int(x) for x in (y, mth, d, h, m, s)]
			# longitude
			try:
				londg, rest = lon.split(':')
				lonmn, rest = rest.split("'")
				lonsc, londr = rest[:2], rest[-1]
			except ValueError:
				londg, lonmn, lonsc = lon.split(':')
				lonsc, londr = lonsc[:1], lonsc[-1]
			longitude = (londg, londr, lonmn, lonsc)
			# latitude
			try:
				latdg, rest = lat.split(':')
				latmn, rest = rest.split("'")
				latsc, latdr = rest[:2], rest[-1]
			except ValueError:
				latdg, latmn, latsc = lat.split(':')
				latsc, latdr = latsc[:1], latsc[-1]
			latitude = (latdg, latdr, latmn, latsc)
			# get utc offset
			hoffset, moffset = offset.split(':')
			soffset, hoffset = hoffset[0], int(hoffset[1:])
			moffset = int(moffset) / 60.0
			hoffset += moffset
			if soffset == '+': # a32 inverts utc offsets
				hoffset = -hoffset
			if stdt == 'DT':
				hoffset += 1
				dst = True
			else:
				dst = False
		if line.startswith('/zi'):
			line = line[4:]
			name, location = line[1:-1].split('" "')
	try:
		cht = Chart(set_default=False, do_calc=False)
		cht.name = name
		cht.location = location
		cht.country = '?'
		cht.datetime = dt
		cht.longitude = longitude
		cht.latitude = latitude
		cht.utcoffset = hoffset
		cht.dst = dst
		cht.comment = 'Imported from Astrolog32'
	except:
		raise
	return cht


# End.
