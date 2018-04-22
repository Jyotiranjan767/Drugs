def decorator_func(original_function):
	def wrapper_function(*ek):
		return original_function(*ek)
	return wrapper_function
@decorator_func
def sub(x, y):
	return x - y

x = decorator_func(sub(3,6))
print(sub(23,2))

def decorator_function(origi_function):
	def wrapper_function(*i):
		print("wrapper executed this before {}".format(origi_function.__name__))
		return origi_function(*i)
	return wrapper_function

@decorator_function
def display():
	print("I am a loser of all time ")
@decorator_function
def display_info(name , age ):
	print('display_info ran with name {}  in age of {}'.format(name, age ))

display()
display_info('lickie ', 248)
# x = decorator_function(display_info)
# x('luckie ', 2)