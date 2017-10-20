
if __name__ == "__main__":
	n = int(raw_input())
	l = map(int , raw_input().split())
	tup = tuple(l)
	print hash(tup)
