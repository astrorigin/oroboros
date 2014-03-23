#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oroboros IRC plugin.

"""

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

from oroboros.core.bicharts import BiChart
from oroboros.core.charts import Chart
from oroboros.gui.chtimage import makeImage


class Oroboros(callbacks.Plugin):
	"""Provides IRC interface to Oroboros astrology software"""
	
	threaded = False
	
	def current(self, irc, msg, args):
		"""takes no arguments
		
		Draw the current chart, put it in the local http server,
		and give the address.
		"""
		path = '/home/sm/public_html/irc/chart.png' # your public path here
		ext = 'png'
		width = 800
		height = 800
		cht = BiChart(Chart())
		makeImage(cht, path, ext, width, height)
		irc.reply('Done, http://ranoraraku.atarax.org/~sm/irc/chart.png') # your httpd here
	current = wrap(current)
	
	def showme(self, irc, msg, args, pth):
		"""<chart>
		
		Draw your chart and show it.
		"""
		path = '/home/sm/public_html/irc/%s.png' % pth # your public path here
		ext = 'png'
		width = 800
		height = 800
		cht = BiChart(Chart('/home/sm/charts/%s.xml' % pth)) # your charts dir here
		makeImage(cht, path, ext, width, height)
		pth = pth.replace(' ', '%20')
		irc.reply('Done, http://ranoraraku.atarax.org/~sm/irc/%s.png' % pth) # your httpd here
	showme = wrap(showme, ['text'])



Class = Oroboros


# End.
