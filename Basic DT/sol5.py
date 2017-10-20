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
		print cls
	if N <= 5 and N >= 2:
		biggest = cls[1][1]
		secbig = cls[0][1]
#	print "secbig = "+secbig
	for j in range(len(cls)):
		if cls[j][1] > secbig and cls[j][1] < biggest:
			secbig = cls[j][1]
			index.append(j)
		if cls[j][1] == secbig:
			index.append(j)
	for k in range(len(index)):
		finalnames.append(cls[k][0])
		finalnames.sort()
	for m in range(len(finalnames)):
		print finalnames[m]
