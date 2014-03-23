#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Rearrange planets disposition.

"""

import swisseph as swe


__all__ = ['rearrange']


def rearrange(L, w):
	"""Return list of rearranged positions."""
	bunches = BunchBunch(L, w)
	return bunches.offer()



class BunchBunch(list):

	def __init__(self, L, w):
		self.L = L
		if len(L) > 36: # the usual width of 10px is cracked
			w = 360.0 / len(L)
		self.w = w
		for p in L:
			self.addflower(p)
		self.arrange()
	
	def addflower(self, p):
		if len(self) == 0:
			self.newbunch(p)
		else:
			for b in self:
				if b.inbunch(p):
					b.addflower(p)
					return
			self.newbunch(p)
	
	def newbunch(self, pos):
		self.append(Bunch(self.w, pos))
	
	def arrange(self):
		test = True
		while test:
			test = self._arrange()
			if test == False:
				self.reverse()
				test = self._arrange()
	
	def _arrange(self):
		for b1 in self[:-1]:
			for b2 in self[1:]:
				if b1 == b2:
					continue
				if b1.mixbunch(b2):
					self.pop(self.index(b1))
					self.pop(self.index(b2))
					b1.addbunch(b2)
					self.append(b1)
					return True
		return False
	
	def offer(self):
		ret = [None] * len(self.L)
		for b in [x.arrange() for x in self]:
			for k, v in b:
				key = None
				start = -1
				while key == None:
					idx = self.L.index(k, start+1)
					if ret[idx] == None:
						key = idx
					else:
						start = idx
				ret[key] = v
		return ret



class Bunch(list):
	
	def __init__(self, w, pos):
		self.w = w
		self.center = pos
		self.append(pos)
	
	def addflower(self, pos):
		self.append(pos)
		self.calc_center()
	
	def calc_center(self):
		tmp = 0
		for p1 in self[:-1]:
			for p2 in self[1:]:
				dist = abs(swe.difdeg2n(p1, p2))
				if dist >= tmp:
					maxw = (p1, p2)
					tmp = dist
		self.center = swe.deg_midp(*maxw)
	
	def inbunch(self, pos):
		test = swe._match_aspect(pos, 0, self.center, 0, 0, self.orb())
		if test[0] != None:
			return True
		return False
	
	def mixbunch(self, other):
		test = swe._match_aspect(self.center, 0, other.center, 0,
			0, self.orb()+other.orb())
		if test[0] != None:
			return True
		return False
	
	def orb(self):
		return (self.w * len(self)) / 2.0
	
	def addbunch(self, other):
		list.extend(self, other)
		self.calc_center()
	
	def arrange(self):
		self.sort(self.cmp)
		ret = list()
		dist = self.orb() - (self.w / 2.0)
		for i in range(len(self)):
			ret.append((self[i], swe.degnorm(self.center - dist)))
			dist -= self.w
		return ret
	
	def cmp(self, x , y):
		t1 = swe.difdeg2n(x, self.center)
		t2 = swe.difdeg2n(y, self.center)
		if t1 > t2:
			return 1
		elif t1 < t2:
			return -1
		else:
			return 0



def _test():
	import doctest
	doctest.testmod()


if __name__ == '__main__':
	_test()

# End.
