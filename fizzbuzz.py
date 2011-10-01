# -*- coding: utf-8 -*-
class FizzBuzz():
	def tabFizzBuzz(self, x):
		"""
		return le nombre passé n'est pas multiple de 3 ou 5
		>>> [val for val in FizzBuzz().tabFizzBuzz(1)]
		['1']
		
		return fizz si multiple de 3
		>>> [val for val in FizzBuzz().tabFizzBuzz(3)]
		['fizz']
		
		return buzz si multiple de 5
		>>> [val for val in FizzBuzz().tabFizzBuzz(5)]
		['buzz']
		
		return les 2 si multiple des 2
		>>> [val for val in FizzBuzz().tabFizzBuzz(15)]
		['fizz', 'buzz']
		"""
		if x%3==0:
			yield "fizz"
		if x%5==0:
			yield "buzz"
			return
		if not x%3==0 and not x%5==0:
			yield str(x)
		
def main():
	"""
	instencie la classe FizzBuzz
	>>> fizz = FizzBuzz()
	"""
	fizz = FizzBuzz()
	print ["".join([val for val in fizz.tabFizzBuzz(i)]) for i in range(1,101)]
if __name__=="__main__":
	import doctest
	doctest.testmod()
	main()
