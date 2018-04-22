class Quick_sort():

	def __init__(self,left,right,arr,pivot):
		self.left = left
		self.right = right
		self.arr = arr
		self.pivot = pivot
	@classmethod
	def swapy(self):
		temp = self.arr[self.left]
		self.arr[self.left] = self.arr[self.right]
		self.arr[self.right] = temp
		return (self.arr[self.left])

	def partitions(self ):
		k = 0
		for i  in range(len(self.arr)):
			if(self.arr[i] == self.pivot):
				k=i
		while(self.left <= k):#  and self.left >=0 ):
			print(self.arr[self.left],end = ' ')
			self.left+=1
		while(self.right  > k  ) :
			print(self.arr[self.right],end = ' ')
			self.right -= 1
		print('\n')
		l=0
		while(l < len(self.arr)-1):
			if(self.arr[self.left] > self.arr[self.right]):
				temp = self.arr[self.left]
				self.arr[self.left] = self.arr[self.right]
				self.arr[self.right] = temp
				print (self.arr[self.left], end = ' ')
				self.left +=1
				self.right-=1
			else : print(self.arr[self.left] , end = ' ')	
			
			l+=1

ad = [21,4,427,31,132,2,24,41]
q = Quick_sort(0,len(ad)-1,ad,31)

q.partitions()