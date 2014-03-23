#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
XML parser (wrapping ElementTree).

This module provides a few pythonic conveniances for building and parsing
XML documents.

Create an element:

	>>> el = Element('root_tag', {'attr': 1})

Append an subelement:

	>>> el.append('section1', text='some text')

Another subelement:

	>>> el.append('section2', {'id': 2, 'var': 'spam'}, 'another text')

Another subelement:

	>>> el.append('section2', {'foo': 'eggs'}, 'how ya doing?')

Get second child attribute 'var':

	>>> el.get_child_attr(idx=1, attr='var')
	'spam'

Get second 'section2' element text:

	>>> el.get_child_text(1, tag='section2')
	'how ya doing?'

Second 'section2' has attribute 'foo'?

	>>> el.get_children(tag='section2')[1].has_attr('foo')
	True

Get number of subelements:

	>>> len(el)
	3

Some tag 'section3' in child elements?

	>>> 'section3' in el
	False

Iterate over all child elements:

	>>> for e in el:
	...     print(e.tag)
	...
	section1
	section2
	section2

Write element to file:

	>>> el.write('test-xmlutils-DELETEME.xml')

"""

import xml.etree.cElementTree as etree


__all__ = ['Element', 'parse', 'comment']


def _serialize(obj):
	"""Return str."""
	if not isinstance(obj, str):
		try:
			return str(obj)
		except:
			try:
				return obj.encode('utf8') # hate python 2
			except:
				raise TypeError('Could not serialize %s.' % type(obj))
	return obj


_default_tag = 'xXx'


class Element(object):
	"""Simple XML element.
	
		- tag -> element name
		- attributes -> dict of attributes
		- text -> element text content
		- tail -> element text tail
	
	"""
	
	__slots__ = ['_etree_elem']
	
	def _get_elem(self):
		"""Return elementtree element."""
		return self._etree_elem
	
	def _set_elem(self, elem):
		"""Set elementtree element.
		
		:raise TypeError: invalid element
		"""
		if not etree.iselement(elem):
			raise TypeError('xml: invalid etree element (%s).' % _etree_elem)
		self._etree_elem = elem
	
	def _get_tag(self):
		"""Return element tag name.
		
		:rtype: str
		"""
		return self._elem.tag
	
	def _set_tag(self, tag):
		"""Set element tag name.
		
		:type tag: str
		"""
		self._elem.tag = _serialize(tag)
	
	def _get_attributes(self):
		"""Return all attributes in a dict.
		
		:rtype: dict
		"""
		return self._elem.attrib
	
	def _set_attributes(self, attrdict):
		"""Set attributes (with a dict).
		
		:type attrdict: dict
		"""
		attr = dict()
		for k, v in attrdict.items():
			attr[_serialize(k)] = _serialize(v)
		self._elem.attrib = attr
	
	def _get_text(self):
		"""Get element text.		
		
		:rtype: str
		"""
		return self._elem.text
	
	def _set_text(self, text):
		"""Set element text.
		
		:type text: str
		"""
		self._elem.text = _serialize(text)
	
	def _get_tail(self):
		"""Get element tail.
		
		:rtype: str
		"""
		return self._elem.tail
	
	def _set_tail(self, tail):
		"""Set element tail.
		
		:type tail: str
		"""
		self._elem.tail = _serialize(tail)
	
	_elem = property(_get_elem, _set_elem,
		doc="ElementTree element.")
	tag = property(_get_tag, _set_tag,
		doc="Element tag.")
	attributes = property(_get_attributes, _set_attributes,
		doc="Element attributes (dict).")
	text = property(_get_text, _set_text,
		doc="Element text.")
	tail = property(_get_tail, _set_tail,
		doc="Element tail.")
	
	def __init__(self, tag=None, attributes={}, text='', tail='',
		_etree_elem=None):
		"""Element instanciation.
		
		:type tag: str
		:type attributes: dict
		:type text: str
		:type tail: str
		:type _etree_elem: elementtree element
		"""
		if _etree_elem != None: # got etree element
			self._elem = _etree_elem
			return
		if tag == None:
			tag = _default_tag
		self._elem = etree.Element(_default_tag)
		self.tag, self.attributes, self.text, self.tail = (tag,
			attributes, text, tail)
	
	def has_attr(self, attribute):
		"""Return True if element has an attribute 'attribute', else False.
		
		:type attribute: str
		:rtype: bool
		"""
		if _serialize(attribute) in self._elem.keys():
			return True
		return False
	
	def get_attr(self, attribute):
		"""Get value of an element attribute.
		
		:type attribute: str
		:rtype: str
		"""
		return self._elem.get(_serialize(attribute))
	
	def set_attr(self, attribute, value):
		"""Set value of element attribute.
		
		:type attribute: str
		:type value: str
		"""
		self._elem.set(_serialize(attribute), _serialize(value))
	
	def append(self, elem=None, attributes={}, text='', tail='',
		_etree_elem=None):
		"""Append an xml element.
		
		The elem is created on the fly or just added if it's already created.
		
		:type elem: Element or str
		:type attributes: dict
		:type text: str
		:type tail: str
		:type _etree_elem: elementtree element
		"""
		if _etree_elem != None: # got etree element
			self._elem.append(_etree_elem)
		elif isinstance(elem, Element): # got xml element
			self._elem.append(elem._elem)
		else: # create and append new element
			self._elem.append(Element(elem, attributes, text, tail)._elem)
	
	def insert(self, elem, attributes={}, text='', tail='', idx=0,
		_etree_elem=None):
		"""Insert an xml element at index 'idx' (default 0).
		
		The elem is created on the fly or just added if it's already created.
		
		:type elem: Element or str
		:type attributes: dict
		:type text: str
		:type tail: str
		:type idx: int
		:type _etree_elem: elementtree element
		"""
		if _etree_elem != None: # got etree element
			self._elem.insert(idx, _etree_elem)
		elif isinstance(elem, Element): # got xml element
			self._elem.insert(idx, elem._elem)
		else:
			self._elem.insert(idx, Element(elem, attributes, text, tail)._elem)
	
	def prepend(self, elem, attributes={}, text='', tail='', _etree_elem=None):
		"""Prepend an xml element.
		
		The elem is created on the fly or just added if it's already created.
		
		:type elem: Element or str
		:type attributes: dict
		:type text: str
		:type tail: str
		:type _etree_elem: elementtree element
		"""
		self.insert(elem, attributes, text, tail, 0, _etree_elem)
	
	def get_child(self, idx=0, tag=None):
		"""Return nth child element (with name 'tag', or any) default first.
		
		Return None if nothing found.
		
		:type idx: int
		:type tag: str
		:rtype: Element or None
		:raise ValueError: invalid index
		"""
		if idx < 0:
			raise ValueError('xml: search index < 0 (%s).' % idx)
		if tag == None: # search all tags
			for i, e in enumerate(self._elem.getiterator()):
				if i == 0 and e.tag == self._elem.tag:
					idx += 1
					continue
				if i == idx:
					return Element(_etree_elem=e)
			return
		if idx == 0: # get first child matching tag
			e = self._elem.find(_serialize(tag))
			if e != None:
				return Element(_etree_elem=e)
			else:
				return
		# iterate over tags
		for i, e in enumerate(self._elem.getiterator(_serialize(tag))):
			if i == 0 and e.tag == self._elem.tag:
				idx += 1
				continue
			if i == idx:
				return Element(_etree_elem=e)
	
	def get_children(self, tag=None):
		"""Return list of subelements 'tag' (or all children if no tag).
		
		:type tag: str or None
		:rtype: list
		"""
		if tag == None:
			all = self._elem.getchildren()
		else:
			all = self._elem.findall(_serialize(tag))
		ret = list()
		for e in all:
			ret.append(Element())
			ret[-1]._elem = e
		return ret
	
	def get_child_text(self, idx=0, tag=None):
		"""Return nth child (matching 'tag' or any) text, default first.
		
		Return None if nothing found.
		
		:type idx: int
		:type tag: str or None
		:rtype: Element or None
		:raise ValueError: invlaid index
		"""
		if idx < 0:
			raise ValueError('xml: search index < 0 (%s).' % idx)
		if tag == None:
			for i, e in enumerate(self._elem.getiterator()):
				if i == 0 and e.tag == self._elem.tag:
					idx += 1
					continue
				if i == idx:
					return e.text
			return
		if idx == 0:
			return self._elem.findtext(_serialize(tag), None)
		else:
			for i, e in enumerate(self._elem.getiterator(_serialize(tag))):
				if i == 0 and e.tag == self._elem.tag:
					idx += 1
					continue
				if i == idx:
					return e.text
	
	def get_child_attr(self, attr, idx=0, tag=None):
		"""Return nth child (matching 'tag' or any) attribute, default first.
		
		Return None if nothing found.
		
		:type attr: str
		:type idx: int
		:type tag: str
		:rtype: str or None
		:raise ValueError: invalid index
		"""
		if idx < 0:
			raise ValueError('xml: search index < 0 (%s).' % idx)
		if tag == None:
			for i, e in enumerate(self._elem.getiterator()):
				if i == 0 and e.tag == self._elem.tag:
					idx += 1
					continue
				if i == idx:
					return e.get(attr)
			return
		if idx == 0:
			e = self._elem.find(_serialize(tag))
			if e != None:
				return e.get(attr)
			else:
				return
		else:
			for i, e in enumerate(self._elem.getiterator(_serialize(tag))):
				if i == 0 and e.tag == self._elem.tag:
					idx += 1
					continue
				if i == idx:
					return e.get(attr)
	
	def remove_child(self, idx=0, tag=None):
		"""Remove nth child element (matching 'tag' or any), default first.
		
		:type idx: int
		:type tag: str
		:raise ValueError: invalid index
		"""
		if idx < 0:
			raise ValueError('xml: search index < 0 (%s).' % idx)
		if tag == None:
			for i, e in enumerate(self._elem.getiterator()):
				if i == 0 and e.tag == self._elem.tag:
					idx += 1
					continue
				if i == idx:
					self._elem.remove(e)
					return
			return
		if idx == 0:
			e = self._elem.find(_serialize(tag))
			if e != None:
				self._elem.remove(e)
				return
			else:
				return
		else:
			for i, e in enumerate(self._elem.getiterator(_serialize(tag))):
				if i == 0 and e.tag == self._elem.tag:
					idx += 1
					continue
				if i  == idx:
					self._elem.remove(e)
					return
	
	def remove_children(self, tag):
		"""Remove all child elements 'tag'.
		
		Return number of elements removed.
		
		:type tag: str
		:rtype: int
		"""
		i = 0
		for j, e in enumerate(self._elem.getiterator(_serialize(tag))):
			if j == 0 and e.tag == self._elem.tag:
				continue
			self._elem.remove(e)
			i += 1
		return i
	
	def clear(self):
		"""Clear everything."""
		self._elem.clear()
	
	def __len__(self):
		"""Get number of child elements.
		
		:rtype: int
		"""
		i = 0
		for e in self._elem.getiterator():
			i += 1
		if i == 0:
			return 0
		else:
			return i - 1
	
	# write element
	
	def write(self, path, encoding='UTF-8'):
		"""Write element to file.
		
		:type path: str
		:type encoding: str
		"""
		etree.ElementTree(self._elem).write(path, encoding)
	
	def dump(self):
		"""Print element.
		
		:rtype: str
		"""
		return etree.dump(self._elem)
	
	def __str__(self, encoding='UTF-8'):
		"""Return str of a complete XML document.
		
		:type encoding: str
		:rtype: str
		"""
		return etree.tostring(self._elem, encoding)
	
	# iterators
	
	def __iter__(self):
		"""Return iterator over all children.
		
		:rtype: iterator
		"""
		return (Element(_etree_elem=x) for x in self._elem.getchildren())

	def get_iterator(self, tag):
		"""Return iterator over children matching 'tag'.
		
		:type tag: str
		:rtype: iterator
		"""
		return (Element(_etree_elem=x) for x in self._elem.findall(_serialize(tag)))
	
	def __contains__(self, tag):
		"""Return True if element has child element named 'tag', else False.
		
		:type tag: str
		:rtype: bool
		"""
		return bool(self._elem.find(_serialize(tag)))



def parse(path):
	"""Read a file and return root element.
	
	:type path: str
	:rtype: Element
	"""
	return Element(_etree_elem=etree.parse(path).getroot())


def comment(text):
	"""Comment factory. Return an elementree comment to append somewhere.
	
	:type text: str
	:rtype: elementtree comment
	"""
	return etree.Comment(text)


def _test():
	import doctest
	doctest.testmod()


if __name__ == '__main__':
	_test()

# End.
