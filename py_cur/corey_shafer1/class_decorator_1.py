class decorator_class(object):

	def __init__(self, original_function):
		self.original_function = original_function

	def __call__(self, *args):
		print("call method executed before {} ".format(self.original_function.__name__))
		return self.original_function(*args)

@decorator_class
def display_info(name , age):
	print('this executed with {} in age of  {}'.format(name , age ))


display_info('lus fj', 37)

