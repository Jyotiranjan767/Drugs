from pprint import pprint
class MyBaseClass(object):
	def __init__(self, value):
		self.value = value

class MyChildClass(object):
	def __init__(self):
		MyBaseClass.__init__(self,5)

class TimesTwo(object):
	def __init__(self):
		self.value *= 2
class PlusFive(object):
	def __init__(self):
		self.value += 5

# this class defines its parent classes in one odering

class OneWay(MyBaseClass, TimesTwo, PlusFive):
	def __init__(self, value):
		MyBaseClass.__init__(self, value)
		TimesTwo.__init__(self)
		PlusFive.__init__(self)
foo = OneWay(5)
print(foo.value)

class TimesFive(MyBaseClass):
	def __init__(self, value):
		MyBaseClass.__init__(self, value)
		self.value *= 5
class PlusTwo(MyBaseClass):
	def __init__(self, value):
		MyBaseClass.__init__(self, value)
		self.value += 2
# then I define a child class that inherits from both the classes , 
#making MyBaseClass the top of the diamond 

class ThisWay(TimesFive, TimesTwo):
	def __init__(self, value):
		TimesFive.__init__(self, value)
		PlusTwo.__init__(self, value)
foo = ThisWay(5)
print("should be (5*5)+2 = 27 but it is ", foo.value)


#python 2
class TimesFiveCorrect(MyBaseClass):
	def __init__(self, value):
		super(TimesFiveCorrect, self).__init__(value)
		self.value *= 5
class PlusTwoCorrect(MyBaseClass):
	def __init__(self, value):
		super(PlusTwoCorrect,self).__init__(value)
		self.value += 2
# python 2 
class GoodWay(TimesFiveCorrect, PlusTwoCorrect):
	def __init__(self, value):
		super(GoodWay, self).__init__(value)

foo = GoodWay(5)
print("shou be (5*5)+2 = 27 and get also ", foo.value)

pprint(GoodWay.mro())

class Explicit(MyBaseClass):
	def __init__(self, value):
		super(__class__, self).__init__(value * 2)
class Implicit(MyBaseClass):
	def __intit__(self, value):
		super().__init__(value * 2)
print(Explicit(10).value)
print(Implicit(10).value)
assert  Explicit(10).value == Implicit(10).value