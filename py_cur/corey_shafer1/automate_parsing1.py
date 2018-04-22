import os

os.chdir("G:\\Music\\Ajab-Gazabb-Love-128Kbps-2012(Songs.PK)")
print(os.getcwd())

lis = []
for f in os.listdir():
	# print(f)
	try:
		file_name , file_ext = os.path.splitext(f)
		movie_name, serial_no, song_name = file_name.split(" - ")
		for i in movie_name.split(' '):
			lis.append(i)
		# print(lis[1],lis[2],lis[3])
		new_name = "{}-{}".format(serial_no, song_name)
		
		os.rename(f, new_name)

	except ValueError :
			pass

