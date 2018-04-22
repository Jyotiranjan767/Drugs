lis = {}
def fibo1(n):

	if n in lis:
		return lis

	if (n==1):
		value = 1
	elif(n ==2 ):
		value = 2
	else :
		value = fibo1(n-1) + fibo1(n-2)

import time
t1= time.time()
fi = fibo1(40)
t2 = time.time() - t1
print(fi, '   ', t2)