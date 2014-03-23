#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Keywords dict objects, used for charts.

	>>> kwd = KeywordsDict('k1:v1;k2:v2')
	>>> print(kwd)
	k2:v2;k1:v1
	>>> kwd['k3'] = 'v3'
	>>> print(kwd)
	k3:v3;k2:v2;k1:v1

"""


__all__ = ['KeywordsDict']


class KeywordsDict(dict):
	"""Chart keywords.
	
		>>> kwd = KeywordsDict('key:value;key2:value2')
	
	"""
	
	__slots__ = tuple()
	
	def __init__(self, kwstr=None):
		"""Init keywords object.
		
		:type kwstr: str or None
		"""
		if kwstr != None:
			self._set_keywords(kwstr)
	
	def _set_keywords(self, kwstr=''):
		"""Set dict with a string.
		
		String are like: "key:value;key:value;...".
		Pass an empty str to clear the dict.
		
		:type kwstr: str
		"""
		if kwstr == '': # reset
			self.clear()
			return
		kvlist = _serialize(kwstr).split(';')
		for kv in kvlist[:]: # erase empty strings
			if kv == '':
				kvlist.pop(kvlist.index(kv))
		for kv in kvlist:
			kvs = kv.split(':')
			if len(kvs) > 2: # trying to get something out of errors
				for i in range(0, len(kvs), 2):
					try:
						self[kvs[i]] = kvs[i+1]
					except IndexError: # drop it.
						pass
			else: # no error in user input
				self[kvs[0].strip()] = kvs[1].strip()
	
	def __setitem__(self, k, v):
		"""Set keywords item.
		
		:type k: str
		:type v: str
		"""
		k = k.replace(':', '').replace(';', '')
		v = v.replace(':', '').replace(';', '')
		k.strip()
		v.strip()
		dict.__setitem__(self, _serialize(k), _serialize(v))
	
	def __str__(self):
		"""Get keywords as str (for database input).
		
		:rtype: str
		"""
		ret = str()
		for k, v in self.items():
			ret += '%s:%s;' % (k, v)
		return ret[:-1]
	
	def __repr__(self):
		return "KeywordsDict('''%s''')" % str(self)
	


def _serialize(s):
	"""Return string encoded in utf8, if it's not unicode already.
	
	:type s: str
	"""
	if not isinstance(s, unicode):
		return s.decode('utf-8')
	else:
		return s


def _test():
	import doctest
	doctest.testmod()

if __name__ == '__main__':
	_test()

# End.
