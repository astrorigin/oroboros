#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Chart information dialog (new, edit).

"""

import sys
import os.path

import pytz
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from oroboros.core import timezone
from oroboros.core.charts import Chart

from oroboros.gui import app
from oroboros.gui.coordswidget import LatitudeEdit, LongitudeEdit, AltitudeEdit
from oroboros.gui.geonames import GeoNamesQueryDialog


__all__ = ['ChartInfoDialog']


_baseDir = os.path.join(os.path.abspath(os.path.dirname(__file__)))


class ChartInfoDialog(QDialog):
	"""New/edit chart window."""
	
	def __init__(self, idx=-1, num=0, parent=None):
		QDialog.__init__(self, parent)
		self._parent = parent
		tr = self.tr
		idx = int(idx)
		if idx == -1:
			chart = Chart(do_calc=False)
			title = tr('New Chart')
		else:
			try:
				chart = app.desktop.charts[idx][num]
				title = unicode(tr('Edit Chart \xab %(chart)s \xbb')) % {
					'chart': chart._name}
			except IndexError:
				chart = Chart(do_calc=False)
				title = unicode(tr('New SubChart'))
		self._chart = chart
		self._idx = idx
		self._num = num
		self.setWindowTitle(title)
		# set width/height
		self.setMinimumWidth(280)
		self.setMinimumHeight(400)
		self.setSizeGripEnabled(True)
		# layout
		grid = QGridLayout(self)
		self.setLayout(grid)
		# name
		grid.addWidget(QLabel(tr('Name')), 0, 0)
		self.nameEdit = QLineEdit(self)
		grid.addWidget(self.nameEdit, 0, 1)
		# datetime
		lbl = QLabel(tr('DateTime'))
		lbl.setToolTip(tr('Local date & time'))
		grid.addWidget(lbl, 1, 0)
		self.datetimeEdit = QDateTimeEdit(self)
		self.datetimeEdit.setDisplayFormat(tr('yyyy-MM-dd hh:mm:ss',
			'Datetime format'))
		self.datetimeEdit.setButtonSymbols(QAbstractSpinBox.PlusMinus)
		self.datetimeEdit.setCalendarPopup(True)
		self.datetimeEdit.setMinimumDateTime(QDateTime(-5400, 1, 1, 0, 0))
		self.datetimeEdit.setMaximumDateTime(QDateTime(5400, 1, 1, 0, 0))
		grid.addWidget(self.datetimeEdit, 1, 1)
		# calendar
		grid.addWidget(QLabel(tr('Calendar')), 2, 0)
		self.calendarEdit = QComboBox(self)
		self.calendarEdit.addItems([tr('Gregorian'), tr('Julian')])
		self.calendarEdit.setEditable(False)
		grid.addWidget(self.calendarEdit, 2, 1)
		# location
		lbl = QLabel(tr('<a href="http://www.astro.com/atlas">Location</a>'))
		lbl.setOpenExternalLinks(True)
		grid.addWidget(lbl, 3, 0)
		self.locationEdit = QLineEdit(self)
		grid.addWidget(self.locationEdit, 3, 1)
		# country
		grid.addWidget(QLabel(tr('Country')), 4, 0)
		self.countryEdit = QLineEdit(self)
		grid.addWidget(self.countryEdit, 4, 1)
		# latitude
		grid.addWidget(QLabel(tr('Latitude')), 5, 0)
		self.latitudeEdit = LatitudeEdit(chart._latitude, self)
		grid.addLayout(self.latitudeEdit, 5, 1)
		# longitude
		grid.addWidget(QLabel(tr('Longitude')), 6, 0)
		self.longitudeEdit = LongitudeEdit(chart._longitude, self)
		grid.addLayout(self.longitudeEdit, 6, 1)
		# altitude
		grid.addWidget(QLabel(tr('Altitude')), 7, 0)
		geoLayout = QHBoxLayout() ## geolayout
		grid.addLayout(geoLayout, 7, 1)
		self.altitudeEdit = AltitudeEdit(chart._altitude, self)
		geoLayout.addWidget(self.altitudeEdit)
		# query geonames
		geoButton = QToolButton(self)
		geoButton.setIcon(QIcon(os.path.join(_baseDir, 'icons',
			'earth-icon.png')))
		geoButton.setToolTip(tr('Query GeoNames.org'))
		self.connect(geoButton, SIGNAL('clicked()'), self.queryGeoNames)
		geoLayout.addWidget(geoButton)
		# zoneinfo
		lbl = QLabel(tr('<a href="http://en.wikipedia.org/wiki/List_of_zoneinfo_timezones">Zoneinfo</a>'))
		lbl.setToolTip(tr('Posix timezone file (for charts after 1900)'))
		lbl.setOpenExternalLinks(True)
		grid.addWidget(lbl, 8, 0)
		self.zoneinfoEdit = QComboBox(self)
		alltz = pytz.all_timezones[:]
		alltz.insert(0, '')
		self.zoneinfoEdit.addItems(alltz)
		self.zoneinfoEdit.setEditable(False)
		grid.addWidget(self.zoneinfoEdit, 8, 1)
		# dst
		lbl = QLabel(tr('Dst'))
		lbl.setToolTip(tr('Daylight saving time (for ambiguous dates only)'))
		grid.addWidget(lbl, 9, 0)
		self.dstEdit = QComboBox(self)
		self.dstEdit.addItems([tr('Not needed'), tr('Yes'), tr('No')])
		grid.addWidget(self.dstEdit, 9, 1)
		# timezone
		lbl = QLabel(tr('<a href="http://upload.wikimedia.org/wikipedia/en/e/e7/Timezones2008.png">Timezone</a>'))
		lbl.setToolTip(tr('Standard timezone (for local mean time)'))
		lbl.setOpenExternalLinks(True)
		grid.addWidget(lbl, 10, 0)
		self.timezoneEdit = QComboBox(self)
		alltz = [str(x) for x in timezone.all_timezones]
		alltz.insert(0, '')
		self.timezoneEdit.addItems(alltz)
		self.timezoneEdit.setEditable(False)
		grid.addWidget(self.timezoneEdit, 10, 1)
		# utc offset
		lbl = QLabel(tr('Utc offset'))
		lbl.setToolTip(
			tr('Coordinated universal time offset (for charts before 1900)'))
		grid.addWidget(lbl, 11, 0)
		self.utcoffsetEdit = QDoubleSpinBox(self)
		self.utcoffsetEdit.setDecimals(2)
		self.utcoffsetEdit.setMinimum(-25)
		self.utcoffsetEdit.setMaximum(24)
		self.utcoffsetEdit.setSuffix(tr(' h.'))
		self.utcoffsetEdit.setSpecialValueText(tr('Not needed'))
		self.utcoffsetEdit.setButtonSymbols(QAbstractSpinBox.PlusMinus)
		grid.addWidget(self.utcoffsetEdit, 11, 1)
		# comment
		lbl = QLabel(tr('Comment'))
		lbl.setToolTip(tr('Accepts reStructured Text'))
		grid.addWidget(lbl, 12, 0, Qt.AlignTop)
		self.commentEdit = QTextEdit('', self)
		grid.addWidget(self.commentEdit, 12, 1)
		# keywords
		lbl = QLabel(tr('Keywords'))
		lbl.setToolTip(tr('Line-separated "key: word" pairs'))
		grid.addWidget(lbl, 13, 0, Qt.AlignTop)
		self.keywordsEdit = QTextEdit('', self)
		grid.addWidget(self.keywordsEdit, 13, 1)
		# buttons
		buttonsLayout = QHBoxLayout()
		resetButton = QPushButton(tr('Reset'), self)
		self.connect(resetButton, SIGNAL('clicked()'), self.reset)
		buttonsLayout.addWidget(resetButton)
		cancelButton = QPushButton(tr('Cancel'), self)
		self.connect(cancelButton, SIGNAL('clicked()'), self.reject)
		buttonsLayout.addWidget(cancelButton)
		okButton = QPushButton(tr('Ok'), self)
		okButton.setDefault(True)
		self.connect(okButton, SIGNAL('clicked()'), self.accept)
		buttonsLayout.addWidget(okButton)
		grid.addLayout(buttonsLayout, 14, 0, 1, 2)
		# fill entries
		self.reset()
	
	def queryGeoNames(self):
		"""Query GeoNames.org database."""
		ok, res = GeoNamesQueryDialog(self).exec_()
		if ok:
			self.locationEdit.setText(res[0])
			self.countryEdit.setText(res[1])
			self.latitudeEdit.setLatitude(res[2])
			self.longitudeEdit.setLongitude(res[3])
			self.altitudeEdit.setAltitude(res[4])
			self.zoneinfoEdit.setCurrentIndex(
				pytz.all_timezones.index(res[5]) + 1)
	
	def reset(self):
		"""Set entries with original values."""
		# name
		self.nameEdit.setText(self._chart._name)
		# datetime
		dt = self._chart._datetime
		dt = QDateTime(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
		self.datetimeEdit.setDateTime(dt)
		# calendar
		if self._chart._calendar == 'gregorian':
			self.calendarEdit.setCurrentIndex(0)
		else:
			self.calendarEdit.setCurrentIndex(1)
		# location
		self.locationEdit.setText(self._chart._location)
		# country
		self.countryEdit.setText(self._chart._country)
		# latitude
		self.latitudeEdit.setLatitude(self._chart._latitude)
		# longitude
		self.longitudeEdit.setLongitude(self._chart._longitude)
		# altitude
		self.altitudeEdit.setAltitude(self._chart._altitude)
		# zoneinfo
		if self._chart._zoneinfo not in (None, ''):
			self.zoneinfoEdit.setCurrentIndex(
				pytz.all_timezones.index(self._chart._zoneinfo) + 1)
		else:
			self.zoneinfoEdit.setCurrentIndex(0)
		# dst
		if self._chart._dst == None:
			self.dstEdit.setCurrentIndex(0)
		elif self._chart._dst == True:
			self.dstEdit.setCurrentIndex(1)
		else:
			self.dstEdit.setCurrentIndex(2)
		# timezone
		if self._chart._timezone not in (None, ''):
			self.timezoneEdit.setCurrentIndex(
				timezone.all_timezones.index(
					timezone.get(self._chart._timezone.utc)) + 1)
		else:
			self.timezoneEdit.setCurrentIndex(0)
		# utc offset
		if self._chart._utcoffset != None:
			self.utcoffsetEdit.setValue(self._chart._utcoffset)
		else:
			self.utcoffsetEdit.setValue(-25)
		# comment
		self.commentEdit.setText(self._chart._comment)
		# keywords
		kw = str(self._chart._keywords).replace(';', '\n')
		self.keywordsEdit.setText(kw)
	
	def accept(self):
		tr = self.tr
		# name
		name = unicode(self.nameEdit.text())
		if name == '':
			QMessageBox.critical(self, tr('Missing Name'),
				tr('Please set chart name.'))
			self.nameEdit.setFocus()
			return
		# datetime
		dt = self.datetimeEdit.dateTime().toPyDateTime()
		# calendar
		if self.calendarEdit.currentIndex() == 0:
			cal = 'gregorian'
		else:
			cal = 'julian'
		# location
		loc = unicode(self.locationEdit.text())
		# country
		cty = unicode(self.countryEdit.text())
		# latitude
		lat = self.latitudeEdit.latitude()
		# longitude
		lon = self.longitudeEdit.longitude()
		# altitude
		alt = self.altitudeEdit.altitude()
		# zoneinfo
		tz = self.zoneinfoEdit.currentIndex()
		if tz == 0:
			tz = ''
		else:
			tz = pytz.all_timezones[tz - 1]
		# dst
		dst = self.dstEdit.currentIndex()
		if dst == 0: ## not needed
			dst = ''
		elif dst == 1:
			dst = True
		else:
			dst = False
		# timezone
		tzone = self.timezoneEdit.currentIndex()
		if tzone == 0:
			tzone = ''
		else:
			tzone = timezone.all_timezones[tzone - 1]
		# utcoffset
		utcof = self.utcoffsetEdit.value()
		if utcof == -25: ## not needed
			utcof = ''
		# comment
		cmt = unicode(self.commentEdit.toPlainText())
		# keywords
		kw = unicode(self.keywordsEdit.toPlainText()).replace('\n', ';')
		# set chart
		self._chart.set(name=name, datetime=dt, calendar=cal, location=loc,
			country=cty, latitude=lat, longitude=lon, altitude=alt, zoneinfo=tz,
			dst=dst, utcoffset=utcof, timezone=tzone, comment=cmt, keywords=kw)
		# check ambiguous datetime
		try:
			self._chart.local_datetime
		except TypeError: ## unable to get local time
			QMessageBox.critical(self, tr('Ambiguous datetime!'),
				tr('Please set DST.'))
			self.dstEdit.setFocus()
			return
		# recalc and close
		self._chart.calc()
		if __name__ != '__main__': ## update app
			if self._idx == -1:
				app.appendMultiChart(self._chart)
			else:
				app.replaceChart(self._idx, self._num, self._chart)
		# done
		self.done(QDialog.Accepted)



def main():
	app = QApplication(sys.argv)
	main = ChartInfoDialog()
	main.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()

# End.
