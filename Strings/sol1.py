def swap(s):
	length = len(s)
	s1 = list(s)
	if length <= 1000 and length > 0:
		for i in range(length):
			if s1[i].islower():
				s1[i] = s1[i].upper()
				final = "".join(s1)
			if s[i].isupper():
				s1[i] = s1[i].lower()
				final = "".join(s1)
	return final
#	else
#		return "bad input"

if __name__ == "__main__":
	s = raw_input()
	result = swap(s)
	print result



