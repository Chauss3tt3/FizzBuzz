# -*- coding: utf-8 -*-

class Base(object):
	"""
		>>> Base().calculer(1)
		'1'
	"""
	def calculer(self, x):
		if x%3 != 0 and x%5 != 0:
			return str(x)
		return ""

class Fizz(Base):
	"""
		>>> Fizz().calculer(3)
		'fizz'
	"""
	def calculer(self, x):
		if x%3 == 0:
			return super(Fizz, self).calculer(x) + "fizz"
		return super(Fizz, self).calculer(x)
			
class FizzBuzz(Fizz):
	"""
		>>> FizzBuzz().calculer(15)
		'fizzbuzz'
	"""
	def calculer(self, x):
		if x%5 == 0:
			return super(FizzBuzz, self).calculer(x) + "buzz"
		return super(FizzBuzz, self).calculer(x)
		

if __name__ == "__main__":
	import doctest
	doctest.testmod()
	fizzBuzz = FizzBuzz()
	for i in xrange(1, 101):
		print fizzBuzz.calculer(i)
