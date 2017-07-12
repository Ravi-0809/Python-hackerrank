def leap(year):
	if year%100 == 0 and year % 400==0:
		return True
	if year % 100 ==0 and year % 400 != 0:
		return False
	if year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
		return True

if __name__ == "__main__":
	year = int(raw_input("Enter a year: "))
	print leap(year)

