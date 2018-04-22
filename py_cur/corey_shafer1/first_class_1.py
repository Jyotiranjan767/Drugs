def square(x):
	return x**2

def cube(d):
	return d*d*d
def exec1(func, args):
	lie = []
	for i in args:
		lie.append(func(i))
	return lie

s =exec1(cube,[1,3,4,5,6,7,8])
print(s)

def logger(msgs):
	def log_message():
		print('log: ' , msgs)
	return log_message

log_hi = logger('hi')
log_hi()
