def decorator_function(original_finction):
	def wrapper_function(*args, ** sd):
		print('wrapper  function executed before {} '.format(original_finction.__name__))
		return original_finction(*args, **sd)
	return wrapper_function

class decorator_class():
	def __init__(self, origi):
		self.origii =origi

	def __call__(self, *args, **skjf):
		print('call method executed from  before {}'.format(self.origii.__name__))
		return self.origii(*args, **skjf)

@decorator_class
def display():
	print('luckkie ')

@decorator_function
def defoine_a_person(race , age ):
	print('age of {} and corlor was {}'.format(race,age))

# dis = decorator_class(display)
# dis()

display()
defoine_a_person(32, 'black')