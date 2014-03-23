#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oroboros-Mercurial utilities.

For more complex operations, directly use the core module, or hg itself.
Or submit a patch...

"""

import sys

if len(sys.argv) == 1:
	sys.exit('oroboros-hg: no arguments. Try "oroboros-hg --help" instead.')

from oroboros.core import cfg
from oroboros.core import hgrepo

help_text = """
usage: oroboros-hg option[=arg]

options:
  --init[=path]     init charts repo in charts dir, default %s
  --clone[=src]     copy charts repo in charts dir, default %s
  --pull[=src]      pull changes from repo to charts dir, default %s
  --push[=src]      push changes from charts dir to repo, default %s
  -h, --help        print this text

see also: hg
""" % (cfg.charts_dir, cfg.hg_repo, cfg.hg_repo, cfg.charts_dir)

cmd = sys.argv[1]

def getarg(opt):
	"""Get option argument.
	
	:type opt: str
	:rtype: str or None
	"""
	try:
		cmd, arg = opt.split('=')
	except ValueError:
		arg = None
	return arg

if cmd in ('-h', '--help'):
	sys.exit(help_text)
elif cmd.startswith('--init'):
	arg = getarg(cmd)
	hgrepo.init(arg)
elif cmd.startswith('--clone'):
	arg = getarg(cmd)
	hgrepo.clone(arg)
elif cmd.startswith('--pull'):
	arg = getarg(cmd)
	hgrepo.pull(arg)
elif cmd.startswith('--push'):
	arg = getarg(cmd)
	hgrepo.push(arg)
else:
	sys.exit(help_text)


# End.
