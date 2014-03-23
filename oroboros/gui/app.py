#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application manager.

"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from oroboros.core import cfg
from oroboros.core import desktop


##__all__ = []


# singleton
mainwin = None ## main window


def appendMultiChart(cht):
	desktop.charts.append(cht)
	mainwin.addTabs(len(desktop.charts) - 1)

def insertMultiChart(idx, cht):
	desktop.charts.insert(idx, cht)
	mainwin.addTabs(idx)

def replaceMultiChart(idx, cht):
	desktop.charts[idx] = cht
	mainwin.resetTabs(idx)

def removeMultiChart(idx):
	del(desktop.charts[idx])
	mainwin.removeTabs(idx)

def replaceChart(idx, num, cht):
	try:
		desktop.charts[idx][num] = cht
	except IndexError:
		desktop.charts[idx].append(cht)
	mainwin.resetTabs(idx)

def removeChart(idx, num):
	del(desktop.charts[idx][num])
	mainwin.resetTabs(idx)




def filterUpdatedEvent(idx):
	for i, cht in enumerate(desktop.charts):
		rset = False
		for c in cht:
			reset = False
			if c._filter._idx_ == idx:
				c._filter.reset()
				rset, reset = True, True
			if reset:
				c.calc()
		if rset:
			cht.calc()
			mainwin.resetTabs(i)


def planetsFilterUpdatedEvent(idx):
	for i, cht in enumerate(desktop.charts):
		rset = False
		for c in cht:
			reset = False
			if c._filter._planets._idx_ == idx:
				c._filter._planets.reset()
				rset, reset = True, True
			if c._filter._midpoints._planets._idx_ == idx:
				c._filter._midpoints._planets.reset()
				rset, reset = True, True
			if reset:
				c.calc()
		if rset:
			cht.calc()
			mainwin.resetTabs(i)


def aspectsFilterUpdatedEvent(idx):
	for i, cht in enumerate(desktop.charts):
		rset = False
		for c in cht:
			reset = False
			if c._filter._aspects._idx_ == idx:
				c._filter._aspects.reset()
				rset, reset = True, True
			if c._filter._midpoints._aspects._idx_ == idx:
				c._filter._midpoints._aspects.reset()
				rset, reset = True, True
			if reset:
				c.calc()
		if rset:
			cht.calc()
			mainwin.resetTabs(i)


def orbsFilterUpdatedEvent(idx):
	for i, cht in enumerate(desktop.charts):
		rset = False
		for c in cht:
			reset = False
			if c._filter._orbs._idx_ == idx:
				c._filter._orbs.reset()
				rset, reset = True, True
			if c._filter._midpoints._orbs._idx_ == idx:
				c._filter._midpoints._orbs.reset()
				rset, reset = True, True
			if reset:
				c.calc()
		if rset:
			cht.calc()
			mainwin.resetTabs(i)


def aspectsRestrictionsUpdatedEvent(idx):
	for i, cht in enumerate(desktop.charts):
		rset = False
		for c in cht:
			reset = False
			if c._filter._asprestr._idx_ == idx:
				c._filter._asprestr.reset()
				rset, reset = True, True
			if c._filter._midpoints._asprestr._idx_ == idx:
				c._filter._midpoints._asprestr.reset()
				rset, reset = True, True
			if reset:
				c.calc()
		if rset:
			cht.calc()
			mainwin.resetTabs(i)


def orbsRestrictionsUpdatedEvent(idx):
	for i, cht in enumerate(desktop.charts):
		rset = False
		for c in cht:
			reset = False
			if c._filter._orbrestr._idx_ == idx:
				c._filter._orbrestr.reset()
				rset, reset = True, True
			if c._filter._midpoints._orbrestr._idx_ == idx:
				c._filter._midpoints._orbrestr.reset()
				rset, reset = True, True
			if reset:
				c.calc()
		if rset:
			cht.calc()
			mainwin.resetTabs(i)


def midPointsFilterUpdatedEvent(idx):
	for i, cht in enumerate(desktop.charts):
		rset = False
		for c in cht:
			reset = False
			if c._filter._midpoints._idx_ == idx:
				c._filter._midpoints.reset()
				rset, reset = True, True
			if reset:
				c.calc()
		if rset:
			cht.calc()
			mainwin.resetTabs(i)


# End.
