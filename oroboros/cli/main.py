#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Main script.

"""

import sys

import oroboros


if len(sys.argv) == 1:
	from oroboros.gui.mainwin import main
	main()

if len(sys.argv) > 2:
	sys.exit('oroboros: too many arguments. Try "oroboros --help" instead.')



disclaimer = """
Oroboros - Astrology software for Python (version %s).

Copyright (C) 2008 Stanislas Marquis <stnsls@gmail.com>
Homepage http://oroboros.atarax.org

This is free software; see the license for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
""" % (oroboros.__version__,)


help_text = """%s
usage: oroboros [option]

options:
  --version         print version
  -h, --help        print this text
""" % (disclaimer,)


version_text = """%s
Running on %s with Python %s.
""" % (disclaimer, sys.platform, sys.version)


cmd = sys.argv[1]

if cmd in ('-h', '--help'):
	sys.exit(help_text)
elif cmd == '--version':
	sys.exit(version_text)
else:
	print('Ha ha ha ...!')


# End.
