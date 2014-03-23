#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SQLite database system.

Connect to database, mention your db path:

	>>> connect(':memory:')

Connect to database using default path:

	>>> connect()

Now a cursor has been created. You can send queries using it transparently.

	>>> print execute("select 1").fetchall()
	[(1,)]

Close connection:

	>>> close()

"""

import os.path
import re
import stat
import sqlite3 as sqlite

import oroboros
from oroboros.core import etc


__all__ = ['Object',
	'connect', 'execute', 'close', 'autoconnect',
	'install', 'connect_atlas', 'install_atlas']

# default db path
_dsn = etc.sqlite['path']

#: Connection resource singleton
_cnx = None

#: Cursor singleton
_cur = None

## oroboros.db._atl_cnx
##_atl_cnx = None # atlas connection

## oroboros.db._atl_cur
##_atl_cur = None # atlas cursor


_basedir = os.path.abspath(os.path.dirname(__file__))


class Object(object):
	"""Base class for all objects stored in database."""
	
	__slots__ = ['_idx_']
	
	def _get_idx(self):
		"""Return db object idx.
		
		:rtype: int
		"""
		return self._idx_
	
	def _set_idx(self, idx):
		"""Set db object idx.
		
		:type idx: int > 0
		:raise ValueError: invalid idx
		"""
		if idx == None:
			self._idx_ = None
		else:
			idx = int(idx)
			if idx < 1:
				raise ValueError('Object %s Db index %s < 0.' % (self, idx))
			else:
				self._idx_ = idx


# Database functions

def _connect(dsn=_dsn):
	"""Connect to database.
	
	:type dsn: str
	:rtype: connection resource
	"""
	dsn = os.path.expanduser(dsn)
	return sqlite.connect(dsn, isolation_level=None,
		detect_types=sqlite.PARSE_DECLTYPES)


def _cursor(conn):
	"""Create a cursor.
	
	:rtype: cursor
	"""
	return conn.cursor()


def connect(dsn=_dsn):
	"""Connect to database, and create a cursor.
	
	Connection and cursor are set globally.
	
	:see: ``path`` option in oroboros.conf file.
	
	:type dsn: str
	"""
	dsn = os.path.expanduser(dsn)
	cnx = _connect(dsn)
	cnx = _create_functions(cnx) # user-defined functions
	cur = _cursor(cnx)
	global _cnx, _cur
	_cnx, _cur = cnx, cur


## oroboros.db.connect_atlas
##def connect_atlas(dsn):
##	"""Connect to atlas database.
##	
##	See the 'atlas_db' config option.
##	Default behavior is store connection and cursor globally.
##	If return_conn is not False, return connection and cursor in a tuple.
##	
##	"""
##	dsn = os.path.expanduser(dsn)
##	cnx = _connect(dsn)
##	cnx = _create_functions(cnx) # user-defined functions
##	cur = _cursor(cnx)
##	global _atl_cnx, _atl_cur
##	_atl_cnx, _atl_cur = cnx, cur


def execute(sql, var=None):
	"""Execute a SQL query.
	
	:type sql: str
	:type var: sequence
	:rtype: cursor
	"""
	global _cur
	try:
		if var == None:
			_cur.execute(sql)
		else:
			_cur.execute(sql, var)
	except:
		#print(sql, var)
		raise
	return _cur


def close():
	"""Close connection."""
	global _cnx, _cur
	try:
		_cur.execute('vacuum;')
	except:
		pass
	return _cnx.close()


def autoconnect(dsn=_dsn):
	"""Automagic database connection on module import.
	
	Return True if connected, False if not connected.
	
	:type dsn: str
	:rtype: bool
	"""
	try:
		connect(dsn)
	except:
		return False
	return True


def _execute_file(path):
	"""Execute SQL statements from a file.
	
	Statements must be delimited by ``;/*End*/``.
	
	:type path: str
	"""
	f = open(path, 'r')
	lines = f.read().split(';/*End*/')
	f.close()
	for sql in lines:
		execute(sql)


def install(path=_dsn):
	"""First install procedure.
	
	Return True on success.
	Return 1 if install already done (and version up to date).
	Return False if unable to query database (not connected).
	
	Delete the database and recreate it if this is a newer version.
	In this case return 2.
	
	:type path: str
	:rtype: bool or int
	"""
	# check db not exists
	sql = "select count(name) from sqlite_master where type = 'table';"
	try:
		res = execute(sql).fetchone()[0]
	except:
		return False # not connected
	if int(res) > 0:
		# stuff in there. check version
		if not _check_version():
			close()
			os.remove(os.path.expanduser(path))
			autoconnect()
			install()
			return 2
		else:
			return 1
	# executes
	f = os.path.join(_basedir, 'sqlite-creates.sql')
	_execute_file(f)
	f = os.path.join(_basedir, 'sqlite-inserts.sql')
	_execute_file(f)
	# chmod db file
	os.chmod(os.path.expanduser(path), stat.S_IRUSR|stat.S_IWUSR)
	# clean
	execute('vacuum;')
	return True


def _check_version():
	"""Return True if db is up to date.
	
	:rtype: bool
	"""
	version = execute('select version from Info;')
	version = int(version.fetchone()[0])
	if version < int(oroboros.__version__):
		return False
	else:
		return True


## oroboros.db.install_atlas
##def install_atlas(path):
##	"""Create atlas database structure.
##	
##	Return True on success.
##	Return -1 if install already done.
##	Return -2 if unable to query database (not connected).
##	
##	"""
##	# check db not exists
##	sql = "select count(name) from sqlite_master where type = 'table';"
##	try:
##		res = execute(sql, cursor=cursor).fetchone()[0]
##	except:
##		return -2
##	if int(res) > 0:
##		return -1
##	# executes
##	f = os.path.join(_basedir, 'atlas.sql')
##	_execute_file(f)
##	# chmod db file
##	os.chmod(os.path.expanduser(path), stat.S_IRUSR|stat.S_IWUSR)
##	return True


def _create_functions(cnx):
	"""Create user-defined functions.
	
	:type cnx: connection resource
	:rtype: connection resource
	"""
	# regexp search
	def regexp_search(pattern, string):
		if re.compile(pattern, re.IGNORECASE).search(string) != None:
			return 1
		return 0
	cnx.create_function('rgxp', 2, regexp_search)
	return cnx


def _test():
	import doctest
	doctest.testmod()


if __name__ == "__main__":
	_test()
else: # try to connect and create database if necessary
	autoconnect()
	install()

# End.
