#item 32 use __getattr__,__getattribute__, and __setattr__ for 
#lazy attributes

class LazyDB(object):
	def __init__(self):
		self.exists = 5
	def __getattr__(self, name):
		value = 'value for %s ' %name
		setattr(self, name, value)
		return value
data = LazyDB()
print('before', data.__dict__)
print('foo', data.foo)
print('after', data.__dict__)

class LoggingLazyDB(LazyDB):
	def __getattr__(self, name):
		print('called __getattr__(%s)' %name)
		return super().__getattr__(name)

logg = LoggingLazyDB()
print(logg.__dict__)
print('foo' ,logg.foo)
print('after', logg.__dict__)

class ValidatingDB(object):
	def __init__(self):
		self.exists = 5

	def __getattr__(self, name):
		print('called __getattribute__(%s)'%name)
		try:
			return super().__getattribute__(name)
		except AttributeError:
			value = 'value for %s' %name
			setattr(self, name, value)
			return value

vali = ValidatingDB()
print('exists', data.exists)
print('foo', data.foo)
print('foo', data.foo)


class MissingPropertyDB(object):
	def __getattr__(self, name):
		if name == 'bad_name':
			raise AttributeError('%s is missing ' %name)
data = MissingPropertyDB()
data.bad_name

class SavingDB(object):
	def __setattr__(self, name, value):
		'''save some data to the DB log'''
		super().__setattr__(name, value)

#Here , I define a logging subclass of SavingDB. Its  __setattr__ method is 
#always called on each attribute assignment 
class LoggingSavingDB(SavingDB):
	def __setattr__(self, name, value):
		print('called __setattr__ (%s %r )' %(name ,value))
		super().__setattr__(name, value)
data = LoggingSavingDB()
print('before ', data.__dict__)
print('after ', data.__dict__)
data.foo = 7
print('finally', data.__dict__)


class BrokenDictionaryDB(object):
	def __init__(self, data):
		self._data= {}
	def __getattribute__(self, name):
		print('called __getattribute__ (%s) %name')
		return self._data[name]
data = BrokenDictionaryDB({'foo', 3})
print(data.foo)

class DictionaryDB(object):
	def __init__(self, data):
		self._data=data
	def __getattribute__(self, name):
		data_dict = super().__getattribute__('_data')
		return data_dict[name]
data = DictionaryDB({'foo', 6})
print('foo', data.foo) # foo : 6
# left unfinished.............	