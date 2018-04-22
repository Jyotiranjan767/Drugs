count =1 
def my_logger(orig_function):
	import logging
	logging.basicConfig(filename='{}.log'.format(orig_function.__name__),level = logging.INFO)

	def wrapper(*args ,**rj): 
		global count
		count+=1
		logging.info('ran with args : {}, and kwargs : {} '.format(args, rj,count))
		return orig_function(*args, **rj)
	return wrapper

def my_timer(orig_function):
	import time
	def wrapper(*args, **kwargs):
		t1= time.time()
		result = orig_function(*args, **kwargs)
		t2 = time.time() - t1
		print('{} ran in : {}'.format(orig_function.__name__, t2))
		return result
	return wrapper

# @my_logger
# @my_logger
def display_info(name  , age, count ):
	print('display_info ran with arguements ({}, {})'.format(name, age))

display_info('jyoti', 25,count )

import time
@my_timer
def fib_ona(n):
	if (n==1 ):
		return 1
	if(n == 2):
		return 1
	elif(n > 2):
		return(fib_ona(n-1) + fib_ona(n-2))

print(fib_ona(2))