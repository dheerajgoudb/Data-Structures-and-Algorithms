def Rev(data):
	for i in range(len(data)-1,-1,-1):
		yield data[i]
		
x = Rev('Dheeraj')
for i in x:
	print i,
