"""
This is a usage example for the foo logic under tmp1.
THIS IS A CHANGE
See Also:
    tmp1/foo.py
"""
from tmp1.foo import FooClass

class NoneSense:
	"""
	cool stuff.
	"""
def sense(self, nonesense):
	"""
	no sense ha sense?
	Args:
		self: me!!!
		nonesense: nothing actually

	Returns:cool stuff

	"""
	if "x" in dir(self):
		self.x += nonesense
	else:
		self.x = nonesense

	return self.x


if __name__ == '__main__':
    a = FooClass()
    b = a.run(10)
    c = a.run(20)

    print(b, c)
