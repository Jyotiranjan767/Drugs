from functools import wraps

def my_logger(orig_function):
	import logging 
	logging.basicConfig(filename  = '{}.log'.format(orig_function.__name__),
									level = logging.INFO)
	@wraps(orig_function)
	def wrapper(*args , **kwargs):
		logging.info("ran with args :{} and {} ".format(args , kwargs))
		return orig_function(*args , **kwargs)
	return wrapper

def my_timer(orig_func):
	import time 

	@wraps(orig_func)
	def wrapper(*args , **kwargs):
		t1 = time.time()
		result = orig_func(*args , **kwargs)
		t2 = time.time() - t1
		print('{} ran in {} sec '.format(orig_func.__name__, t2 ))
		return result
	return wrapper

@my_logger
def display_info1(name, age):
	print('display_info ran with arguments ({}, {})'.format(name , age ))
display_info1('loser', 23)
# @my_logger
# @my_timer
def fibona_(n):
	if(n==0 or n==1):
		return 1
	return n*fibona_(n-1)
fibona_(2)
fibona_1 =my_timer( my_logger(fibona_))
# fibona_1(3)
print(type(fibona_1(3)))