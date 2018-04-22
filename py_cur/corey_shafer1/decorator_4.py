import json

def as_json(func):
	def inner(*args,**kw):
		result = func(*args, **kw)
		return json.dumps(result)
	return inner

@as_json
def dic(x, y):
	return {'result' : x+y}

print(type(dic(3,4))) 