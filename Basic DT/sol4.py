if __name__ == '__main__':
	n = int(raw_input())
	arr = []
	arr = map(int , raw_input().split())
	flag = 0
	if n >= 2 and n <=10:
		for i in arr:
			if i >= -100 and i <= 100:
				flag = 1
	if flag == 1:
	  	arr.sort()
		biggest = arr[len(arr)-1]
		secbig = arr[0]
	  	for i in range(len(arr)):
			if arr[i] >= secbig and arr[i] < biggest:
				secbig = arr[i]
		print secbig
			

	  	
