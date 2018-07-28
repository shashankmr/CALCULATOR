class calculator():

	name = None

	def __init__(self, name):
		self.name = name

	def add(self, a, b):
		result = a+b
		return result

	def sub(self, a, b):
		result = a-b
		return result

	def mul(self, a, b):
		result = a*b
		return result

	def div(self, a, b):
		result = a/b
		return result

class ScientificCalculator(calculator):

	def power(self, a):
		return a*a


def prints_something(some_string):
	print("Inside a function outside a class"+some_string)


