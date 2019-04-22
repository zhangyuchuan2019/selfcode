import numpy as np

def loadfile(filename):
	datas=[]
	with open(filename,'r') as file_to_read:
		while True:
			lines=file_to_read.readline()
			if not lines:
				break
				pass
			data=[float(i) for i in lines.split()]
			datas.append(data[0])
			pass
		file_to_read.close()
		for i in datas:
			print(i)

loadfile("C3.txt")