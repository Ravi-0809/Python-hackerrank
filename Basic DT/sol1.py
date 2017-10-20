from __future__ import print_function

if __name__ == "__main__":
	n = int(raw_input())
	mylist = []
	for i in range(n):
		string = raw_input()
		if string[:6] == "insert":
			com, pos, num = string.split()
			mylist.insert(int(pos),int(num))
		if string[:5] == "print":
			print(mylist)
		if string[:6] == "remove":
			com, ele = string.split()
			mylist.remove(int(ele))
		if string[:6] == "append":
			com, ele = string.split()
			mylist.append(int(ele))
		if string[:4] == "sort":
			mylist.sort()
		if string[:3] == "pop":
			mylist.pop()
		if string[:7] == "reverse":
			mylist.reerse()
