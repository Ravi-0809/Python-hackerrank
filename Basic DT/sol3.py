if __name__ == '__main__':
	x = int(raw_input())
	y = int(raw_input())
	z = int(raw_input())	
	N = int(raw_input())
	tot = []
	arr = []
	if x >= 0 and y >= 0 and z >= 0:
		for i in range(x+1):
			for j in range(y+1):
				for l in range(z+1):
					if i+j+l != N:
						arr = [i,j,l]
						tot.append(arr)
		print tot
