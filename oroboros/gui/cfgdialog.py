#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Edit general settings window.

"""

import sys
import os.path

import pytz
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from oroboros.core import cfg
from oroboros.core import timezone
from oroboros.core.filters import Filter, all_filters_names

from oroboros.gui import translations
from oroboros.gui.coordswidget import LatitudeEdit, LongitudeEdit, AltitudeEdit
from oroboros.gui.filterdialog import FilterDialog
from oroboros.gui.geonames import GeoNamesQueryDialog


__all__ = ['CfgDialog']


_baseDir = os.path.dirname(os.path.abspath(__file__))


class CfgDialog(QDialog):
	
	def __init__(self, parent=None):
		QDialog.__init__(self, parent)
		self._parent = parent
		tr = self.tr
		# set window title
		self.setWindowTitle(tr('Edit settings'))
		# width/height
		self.setMinimumWidth(280)
		self.setMaximumWidth(400)
		self.setSizeGripEnabled(True)
		# layout
		grid = QGridLayout(self)
		self.setLayout(grid)
		# tab widget
		tabs = QTabWidget(self)
		grid.addWidget(tabs, 0, 0)
		
		# ### main settings ###
		mainWidget = QWidget()
		tabs.addTab(mainWidget, tr('Main', 'Main settings'))
		mainGrid = QGridLayout()
		mainWidget.setLayout(mainGrid)
		# user name
		mainGrid.addWidget(QLabel(tr('User name')), 0, 0)
		self.usernameEdit = QLineEdit(self)
		mainGrid.addWidget(self.usernameEdit, 0, 1)
		# user mail
		mainGrid.addWidget(QLabel(tr('User email')), 1, 0)
		self.usermailEdit = QLineEdit(self)
		mainGrid.addWidget(self.usermailEdit, 1, 1)
		# language
		mainGrid.addWidget(QLabel(tr('Language')), 2, 0)
		self.languageEdit = QComboBox(self)
		alllng = translations.languages
		alllng.insert(0, '')
		self.languageEdit.addItems(alllng)
		self.languageEdit.setEditable(False)
		mainGrid.addWidget(self.languageEdit, 2, 1)
		# charts directory
		mainGrid.addWidget(QLabel(tr('Charts dir')), 3, 0)
		layout = QHBoxLayout()
		self.chartsdirEdit = QLineEdit(self)
		self.chartsdirEdit.setReadOnly(True)
		layout.addWidget(self.chartsdirEdit)
		chtdirButton = QToolButton(self)
		chtdirButton.setIcon(QIcon(os.path.join(_baseDir,
			'icons', 'gtk-directory.png')))
		chtdirButton.setToolTip(tr('Select charts directory'))
		self.connect(chtdirButton, SIGNAL('clicked()'), self.chartsDirSelect)
		layout.addWidget(chtdirButton)
		mainGrid.addLayout(layout, 3, 1)
		# use docutils
		self.useDocutilsBox = QCheckBox(tr('Use docutils'), self)
		mainGrid.addWidget(self.useDocutilsBox, 4, 0, 1, 2)
		
		# ### default chart ###
		dftChartWidget = QWidget()
		tabs.addTab(dftChartWidget, tr('Default Chart'))
		dftChartGrid = QGridLayout()
		dftChartWidget.setLayout(dftChartGrid)
		# default location
		lbl = QLabel(tr('<a href="http://www.astro.com/atlas">Location</a>'))
		lbl.setOpenExternalLinks(True)
		dftChartGrid.addWidget(lbl, 0, 0)
		self.locationEdit = QLineEdit(self)
		dftChartGrid.addWidget(self.locationEdit, 0, 1)
		# default country
		dftChartGrid.addWidget(QLabel(tr('Country')), 1, 0)
		self.countryEdit = QLineEdit(self)
		dftChartGrid.addWidget(self.countryEdit, 1, 1)
		# default zoneinfo
		lbl = QLabel(tr('<a href="http://en.wikipedia.org/wiki/List_of_zoneinfo_timezones">Zoneinfo</a>'))
		lbl.setToolTip(tr('Posix timezone file (for charts after 1900)'))
		lbl.setOpenExternalLinks(True)
		dftChartGrid.addWidget(lbl, 2, 0)
		self.zoneinfoEdit = QComboBox(self)
		alltz = pytz.all_timezones[:]
		alltz.insert(0, '')
		self.zoneinfoEdit.addItems(alltz)
		self.zoneinfoEdit.setEditable(False)
		dftChartGrid.addWidget(self.zoneinfoEdit, 2, 1)
		# default timezone
		lbl = QLabel(tr('<a href="http://upload.wikimedia.org/wikipedia/en/e/e7/Timezones2008.png">Timezone</a>'))
		lbl.setToolTip(tr('Standard timezone (for local mean time)'))
		lbl.setOpenExternalLinks(True)
		dftChartGrid.addWidget(lbl, 3, 0)
		self.timezoneEdit = QComboBox(self)
		alltz = [str(x) for x in timezone.all_timezones]
		alltz.insert(0, '')
		self.timezoneEdit.addItems(alltz)
		self.timezoneEdit.setEditable(False)
		dftChartGrid.addWidget(self.timezoneEdit, 3, 1)
		# latitude
		dftChartGrid.addWidget(QLabel(tr('Latitude')), 4, 0)
		self.latitudeEdit = LatitudeEdit(cfg.dft_latitude, self)
		dftChartGrid.addLayout(self.latitudeEdit, 4, 1)
		# longitude
		dftChartGrid.addWidget(QLabel(tr('Longitude')), 5, 0)
		self.longitudeEdit = LongitudeEdit(cfg.dft_longitude, self)
		dftChartGrid.addLayout(self.longitudeEdit, 5, 1)
		# altitude
		dftChartGrid.addWidget(QLabel(tr('Altitude')), 6, 0)
		geoLayout = QHBoxLayout() # geo layout
		dftChartGrid.addLayout(geoLayout, 6, 1)
		self.altitudeEdit = AltitudeEdit(cfg.dft_altitude, self)
		geoLayout.addWidget(self.altitudeEdit)
		# geonames query
		geoButton = QToolButton(self)
		geoButton.setIcon(QIcon(os.path.join(_baseDir, 'icons',
			'earth-icon.png')))
		geoButton.setToolTip(tr('Query GeoNames.org'))
		self.connect(geoButton, SIGNAL('clicked()'), self.queryGeoNames)
		geoLayout.addWidget(geoButton)
		# filter
		dftChartGrid.addWidget(QLabel(tr('Filter')), 7, 0)
		filtLayout = QHBoxLayout()
		self.filterEdit = QComboBox(self)
		self.filterEdit.addItems(all_filters_names())
		self.filterEdit.setEditable(False)
		filtLayout.addWidget(self.filterEdit)
		filtButton = QToolButton(self)
		filtButton.setIcon(QIcon(os.path.join(_baseDir, 'icons',
			'gtk-execute.png')))
		filtButton.setToolTip(tr('Edit filter'))
		self.connect(filtButton, SIGNAL('clicked()'), self.editFilter)
		filtLayout.addWidget(filtButton)
		dftChartGrid.addLayout(filtLayout, 7, 1)
		
		# ### mercurial settings ###
		hgWidget = QWidget()
		tabs.addTab(hgWidget, tr('Mercurial'))
		hgGrid = QGridLayout()
		hgWidget.setLayout(hgGrid)
		# use hg
		self.useHgBox = QCheckBox(tr('Use Mercurial'), self)
		self.useHgBox.setToolTip(
			tr('Pull changes on startup and push changes on shutdown'))
		hgGrid.addWidget(self.useHgBox, 0, 0, 1, 2)
		# hg repo
		lbl = QLabel(tr('Hg repo'))
		lbl.setToolTip(tr('Distant repository address'))
		hgGrid.addWidget(lbl, 1, 0)
		self.hgRepoEdit = QLineEdit(self)
		hgGrid.addWidget(self.hgRepoEdit, 1, 1)
		# hg user
		hgGrid.addWidget(QLabel(tr('Username')), 2, 0)
		self.hgUserEdit = QLineEdit(self)
		hgGrid.addWidget(self.hgUserEdit, 2, 1)
		# hg pswd
		hgGrid.addWidget(QLabel(tr('Password')), 3, 0)
		self.hgPswdEdit = QLineEdit(self)
		self.hgPswdEdit.setEchoMode(QLineEdit.Password)
		hgGrid.addWidget(self.hgPswdEdit, 3, 1)
		
		# ### buttons ###
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
		grid.addLayout(buttonsLayout, 1, 0)
		# fill entries
		self.reset()
	
	def chartsDirSelect(self):
		"""Select charts directory."""
		path = unicode(QFileDialog.getExistingDirectory(self,
			self.tr('Set charts directory'),
			os.path.expanduser('~')))
		if path != '':
			self.chartsdirEdit.setText(path)
	
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
	
	def editFilter(self):
		"""Open filter editor."""
		filt = Filter(all_filters_names()[self.filterEdit.currentIndex()])
		edit = FilterDialog(self, filt)
		ok = edit.exec_()
		if ok: # reload filter box
			# cfg is already updated by filter dialog
			self.resetFilters()
	
	def resetFilters(self):
		"""Reset filter box."""
		self.filterEdit.clear()
		all = all_filters_names()
		self.filterEdit.addItems(all)
		self.filterEdit.setCurrentIndex(all.index(cfg.dft_filter._name))
	
	def reset(self):
		"""Set entries with original values."""
		# ### main ###
		# user name
		self.usernameEdit.setText(cfg.username)
		# user email
		self.usermailEdit.setText(cfg.usermail)
		# language
		if cfg.language != '':
			self.languageEdit.setCurrentIndex(
				translations.languages.index(cfg.language))
		else:
			self.languageEdit.setCurrentIndex(0)
		# charts dir
		self.chartsdirEdit.setText(os.path.expanduser(cfg.charts_dir))
		# use docutils
		self.useDocutilsBox.setChecked(cfg.use_docutils)
		# ### default chart ###
		# default location
		self.locationEdit.setText(cfg.dft_location)
		# default country
		self.countryEdit.setText(cfg.dft_country)
		# zoneinfo
		if cfg.dft_zoneinfo in ('', None):
			self.zoneinfoEdit.setCurrentIndex(0)
		else:
			self.zoneinfoEdit.setCurrentIndex(
				pytz.all_timezones.index(cfg.dft_zoneinfo) + 1)
		# timezone
		if cfg.dft_timezone == None:
			self.timezoneEdit.setCurrentIndex(0)
		else:
			self.timezoneEdit.setCurrentIndex(
				timezone.all_timezones.index(cfg.dft_timezone) + 1)
		# latitude
		self.latitudeEdit.setLatitude(cfg.dft_latitude)
		# longitude
		self.longitudeEdit.setLongitude(cfg.dft_longitude)
		# altitude
		self.altitudeEdit.setAltitude(cfg.dft_altitude)
		# filter
		self.resetFilters()
		# ### mercurial ###
		# use hg
		self.useHgBox.setChecked(cfg.use_hg)
		# hg repo
		self.hgRepoEdit.setText(cfg.hg_repo)
		# hg user
		self.hgUserEdit.setText(cfg.hg_user)
		# hg pswd
		self.hgPswdEdit.setText(cfg.hg_pswd)
	
	def accept(self):
		# ### main ###
		# username
		cfg.username = unicode(self.usernameEdit.text())
		# usermail
		cfg.usermail = unicode(self.usermailEdit.text())
		# language
		lng = self.languageEdit.currentIndex()
		if lng == 0:
			lng = ''
		else:
			lng = translations.languages[lng-1]
		cfg.language = lng
		# charts dir
		cfg.charts_dir = unicode(self.chartsdirEdit.text())
		# use docutils
		cfg.use_docutils = self.useDocutilsBox.isChecked()
		# ### default chart ###
		# location
		cfg.dft_location = unicode(self.locationEdit.text())
		# country
		cfg.dft_country = unicode(self.countryEdit.text())
		# zoneinfo
		tz = self.zoneinfoEdit.currentIndex()
		if tz == 0:
			cfg.dft_zoneinfo == ''
		else:
			cfg.dft_zoneinfo = pytz.all_timezones[tz - 1]
		# timezone
		tzone = self.timezoneEdit.currentIndex()
		if tzone == 0:
			cfg.dft_timezone = ''
		else:
			cfg.dft_timezone = timezone.all_timezones[tzone - 1]
		# latitude
		cfg.dft_latitude = self.latitudeEdit.latitude()
		# longitude
		cfg.dft_longitude = self.longitudeEdit.longitude()
		# altitude
		cfg.dft_altitude = self.altitudeEdit.altitude()
		# filter
		filt = self.filterEdit.currentIndex()
		cfg.dft_filter = Filter(all_filters_names()[filt])
		# ### mercurial ###
		# use hg
		cfg.use_hg = self.useHgBox.isChecked()
		# hg repo
		cfg.hg_repo = unicode(self.hgRepoEdit.text())
		# hg user
		cfg.hg_user = unicode(self.hgUserEdit.text())
		# hg pswd
		cfg.hg_pswd = unicode(self.hgPswdEdit.text())
		
		# save settings
		cfg.save()
		# done
		self.done(QDialog.Accepted)



def main():
	app = QApplication(sys.argv)
	main = CfgDialog()
	main.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()

# End.
