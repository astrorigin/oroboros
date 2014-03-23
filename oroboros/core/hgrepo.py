#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Synchronize charts directory using Mercurial.

Little how-to:

  - Setup your Mercurial server.
  - Setup a server repo for your charts, accessible by http.
    See ``oroboros-hg --init`` command, or use hg itself.
    Ex: ``su -c "oroboros-hg --init=/path/to/hg/repo/charts" apache``
  - Set your Hg repo settings with the graphical interface.
    If you want to pull/push changes automagically, edit your
    settings so that your charts directory points to the local repo.
  - Clone the main repo in your charts directory.
    See ``oroboros-hg --clone`` or use hg itself.

"""

import os
import os.path

from oroboros.core import cfg

__all__ = ['init', 'clone']


# hgignore file
_hgignore = """# Oroboros Charts Repo - hgignore
syntax: glob
# backups
*~
*.bak
# images
*.png
*.jpg
*.bmp
*.tiff
*.ppm
*.xpm
*.xbm
*.svg
"""

# hgrc file
_hgrc = """[web]
name = %s
contact = %s
description = %s
allow_push = %s
deny_push = %s
push_ssl = %s
"""

# commit message
_commit_msg = "Auto-commit by Oroboros"


def init(path=None, allow=['*'], deny=[], ssl=False):
	"""Init hg charts repository.
	
	By default, anybody is allowed to push changes.
	
	:type path: str or None
	:type allow: sequence
	:type deny: sequence
	:type ssl: bool
	"""
	if path == None: # use cfg charts dir
		path = os.path.abspath(os.path.expanduser(cfg.charts_dir))
	else:
		path = os.path.abspath(os.path.expanduser(path))
	# check dir exists
	if not os.path.isdir(path):
		os.mkdir(path)
	# copy hgignore
	f = open(os.path.join(path, '.hgignore'), 'w')
	f.write(_hgignore)
	f.close()
	# init
	os.system('hg init %s' % path)
	# copy hgrc
	hgrc = os.path.join(path, '.hg', 'hgrc')
	f = open(hgrc,  'w')
	f.write(_hgrc % ('Oroboros-charts', cfg.usermail, 'Oroboros charts', 
		','.join(allow), ','.join(deny), str(ssl)))
	f.close()
	# commit
	commit(path)


def commit(path=None):
	"""Commit local changes.
	
	:type path: str or None
	"""
	if path == None:
		path = cfg.charts_dir
	os.system('hg commit -A -m "%s" -R %s' % (
		_commit_msg, path))
	

def clone(src=None, dest=None, user=None, pswd=None):
	"""Clone distant repository.
	
	:type src: str or None
	:type dest: str or None
	:type user: str or None
	:type pswd: str or None
	"""
	if src == None:
		src = cfg.hg_repo
	if dest == None:
		dest = os.path.abspath(os.path.expanduser(cfg.charts_dir))
	if user == None:
		user = cfg.hg_user if cfg.hg_user != '' else None
		pswd = cfg.hg_pswd if cfg.hg_pswd != '' else None
	src = make_dest_url(src, user, pswd)
	os.system('hg clone %s %s' % (src, dest))


def make_dest_url(dest, user, pswd):
	"""Get the destination Url for pull/push.
	
	:type dest: str
	:type user: str
	:type pswd: str
	:rtype: str
	"""
	if user != None:
		ret = user
		if pswd != None:
			ret += ':%s' % pswd
		proto, col = dest.split('://')
		ret = '%s://%s@%s' % (proto, ret, col)
		return ret
	else:
		return dest


def pull(src=None, dest=None, user=None, pswd=None):
	"""Pull changes from distant repo.
	
	:type src: str or None
	:type dest: str or None
	:type user: str or None
	:type pswd: str or None
	"""
	if src == None:
		src = cfg.hg_repo
	if dest == None:
		dest = os.path.abspath(os.path.expanduser(cfg.charts_dir))
	if user == None:
		user = cfg.hg_user if cfg.hg_user != '' else None
		pswd = cfg.hg_pswd if cfg.hg_pswd != '' else None
	src = make_dest_url(src, user, pswd)
	os.system('hg pull -u -R %s %s' % (dest, src))


def push(src=None, dest=None, user=None, pswd=None):
	"""Push changes to distant repo.
	
	:type src: str or None
	:type dest: str or None
	:type user: str or None
	:type pswd: str or None
	"""
	if src == None:
		src = os.path.abspath(os.path.expanduser(cfg.charts_dir))
	if dest == None:
		dest = cfg.hg_repo
	if user == None:
		user = cfg.hg_user if cfg.hg_user != '' else None
		pswd = cfg.hg_pswd if cfg.hg_pswd != '' else None
	dest = make_dest_url(dest, user, pswd)
	os.system('hg push -R %s %s' % (src, dest))



# End.
