#!/usr/bin/env python3
# sample python code, Bill Ola Rasmussen

class Point(object):
	'point coordinates, any dimension'
	def __init__(self,*f):
		self.f=f
	def __str__(self):
		return ','.join(map(str,self.f))
	def __add__(self,rhs):
		return Point( *map(sum,zip(self.f,rhs.f)) )
	# todo: draw function

class Bezier(object):
	'Points defining a Bezier curve (start point, 1-n control points, end point)'
	def __init__(self,*p):
		self.p=p
	def __str__(self):
		return ' '.join(map(str,self.p))
	def draw(self):
		return '_curve '+str(self)+' _enter'
