from abc import ABC , abstractmethod

class AbstractClassExample(ABC):

	@abstractmethod
	def do_something(self):
		print('some implementations@!')

class AnotherSubclass(AbstractClassExample):

	def do_something(self):
		super().do_something()
		print('the enrichment from anotherSubClass')

x = AnotherSubclass()
x.do_something()

