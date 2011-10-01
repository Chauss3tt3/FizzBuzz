# -*- coding: utf-8 -*-

def fizzBuzz(mini, maxi):
	"""
		>>> "".join(fizzBuzz(1,2))
		'1'

		>>> "".join(fizzBuzz(3,4))
		'fizz'

		>>> "".join(fizzBuzz(5,6))
		'buzz'

		>>> "".join(fizzBuzz(14,16))
		'fizzbuzz'
	"""
	for i in range(mini,maxi): yield '\n'+(-(i%3-1)*'fizz'+-(i%5-1)*'buzz' or str(i))
	
import doctest
doctest.testmod()
print "".join(fizzBuzz(1,101))
