if __name__ == '__main__':
	N = int(raw_input())
	l = []
	cls = []
	index = []
	finalnames = []
	for i in range(N):
		name = str(raw_input())
		score = float(raw_input())
		l = [name , score]
		cls.append(l)
	if N <= 5 and N >= 2:
		cls.sort(key = lambda x:x[1])
		lowest = cls[0][1]
		for m in range(len(cls)):
			if cls[m][1] > lowest:
				sec_lowest = cls[m][1]
				break
		for j in range(len(cls)):
			if cls[j][1] == sec_lowest:
				finalnames.append(cls[j][0])
		finalnames.sort()
		for k in range(len(finalnames)):
			print finalnames[k]
	
