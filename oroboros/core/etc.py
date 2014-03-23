#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Configuration file.

Users have a configuration file loaded on startup, containing the
minimal information:

  - path to sqlite3 database

The original configuration file (``etc.txt``) should be checked and
modified by the administrator, with correct values. The default values
inside ``etc.py`` must also be checked accordingly.

This file is copied to user's home by default in a dedicated directory
(``~/.oroboros``) on the first startup, but only if there is no config in the
system-wide configuration path (``/etc/oroboros.conf`` under linux) or in the
current working directory (``./oroboros.conf``). All these names can easily be
changed inside the source code.

Importation of the module does read (and create) the config file.

Copy original config file to home:

	>>> create() # config already installed: should return False
	False

Read your config and set module globals (done on explicit import):

	>>> read()
	True

Get your config values:

	>>> sqlite['path']
	'~/.oroboros/oroboros.db'

"""

import os.path
import shutil
import stat
import ConfigParser


__all__ = ['read', 'exists', 'create', 'sqlite']


# -- CONFIGURATION -- default values:
# Dont forget to modify etc.txt.
# These values are used only if there is no config file to read anywhere.

#: Sqlite config section.
#: :type sqlite: dict
sqlite = {
	'path': '~/.oroboros/oroboros.db'
	}


# Paths:
# There should be no reason to change them unless you know what you are doing.

#: Configuration file name.
#: :type _cfgname: str
_cfgname = 'oroboros.conf'

#: User's configuration directory.
#: If empty str or None, don't create this directory.
#: :type _dir: str
_dir = '~/.oroboros'

#: User's default config file path.
#: :type _path: str
_path = os.path.join(_dir, _cfgname)

#: System-wide configuration.
#: :type _sysconf: str
_sysconf = os.path.join('/etc', _cfgname)

# current working dir path
_baseconf = os.path.join('./', _cfgname)


# -- END CONFIGURATION -- Don't modify below!


#: Configuration file exist flag.
#: :type exists: bool
exists = False

#: Original configuration file.
#: :type original_file: str
original_file = 'etc.txt'


def read(path=_path, force=False):
	"""Read configuration and set globals.
	
	If user has no personal config, try to read system's config,
	or current directory config.
	Return True if something has been read; or False if nothing.
	Set force=True if you want to re-read config file.
	
	:type path: str
	:type force: bool
	:rtype: bool
	"""
	# dont re-read config unless forcing
	global exists
	if not force:
		if exists == True:
			return True
	# try to read user's config
	ini = ConfigParser.SafeConfigParser()
	c = ini.read(os.path.expanduser(path))
	if len(c) != 0:
		return _set_globals(ini)
	# try to read system config
	global _sysconf
	ini = ConfigParser.SafeConfigParser()
	c = ini.read(_sysconf)
	if len(c) != 0:
		return _set_globals(ini)
	# try to read current dir config
	global _baseconf
	ini = ConfigParser.SafeConfigParser()
	c = ini.read(_baseconf)
	if len(c) != 0:
		return _set_globals(ini)
	# using default values...
	return False


def _set_globals(parser):
	"""Set configuration globals using a config parser.
	
	By the way, sets the ``exists`` flag to True.
	
	:type parser: ConfigParser
	:rtype: bool
	"""
	global exists, sqlite
	if parser.has_option('sqlite', 'path'):
		sqlite['path'] = parser.get('sqlite', 'path')
	exists = True
	return True


def create(path=_path, create_dir=_dir):
	"""Copy original config file to user's home.
	
	If needed, try to create a dedicated directory.
	Return True; or False if something already exists.
	
	:type path: str
	:type create_dir: str
	:rtype: bool
	"""
	path = os.path.expanduser(path)
	# check if file already exists
	if (os.path.exists(path)):
		return False
	# check if dir exists
	if create_dir not in (None, ''):
		if not _create_dir(create_dir):
			return False
	# copy file
	src = os.path.join(os.path.abspath(os.path.dirname(__file__)),
		original_file)
	shutil.copyfile(src, path)
	## chown and chmod file
	os.chown(path, os.getuid(), os.getgid())
	os.chmod(path, stat.S_IRUSR|stat.S_IWUSR)
	return True


def _create_dir(path=_dir):
	"""Create the personal oroboros directory (``~/.oroboros``).
	
	Return True; or False if something else than a directory already exists.
	
	:rtype: bool
	"""
	path = os.path.expanduser(path)
	if (os.path.exists(path)):
		if not (os.path.isdir(path)):
			return False
		else:
			return True
	else:
		os.mkdir(path)
		os.chmod(path, stat.S_IRUSR|stat.S_IWUSR|stat.S_IXUSR)
	return True


def _test():
	import doctest
	doctest.testmod()


if __name__ == "__main__":
	_test()
else: # read config file on module import, or try to create it
	if not read():
		create()
		read(force=True)

# End.
