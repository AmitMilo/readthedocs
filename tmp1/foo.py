"""
This is a foo file under tmp1 directory.
This is a new line.
"""


def my_foo(foo):
	"""
	print foo to the screen
	
	Args:
		foo: my foo

	Returns:
		Nothing.
	"""
	print(foo)


class FooClass:
	"""
	This is a foo class.
	"""
	def run(self, y):
		"""
		Run the foo object with the given oarameter.
		Args:
			y: a parameter.

		Returns:
			x
		"""
		if "x" in dir(self):
			self.x += y
		else:
			self.x = y
		my_foo(self.x)

		return self.x
