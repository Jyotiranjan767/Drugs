
def decorate_message(func):
	def get_me(*message):
		return "welcome to "+*message
	return get_me

def my_calculator(func):
	def calculate(a,b):
		return calculate 
	return func

@decorate_message
@my_calculator
def site_name(message,a,b):
	return str(a+b)+message

# # z = decorate_message(site_name)
# # print(z("luckie was not Lucky"))

print(site_name('lily',12,13))
	