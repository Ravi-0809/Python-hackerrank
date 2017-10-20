if __name__ == "__main__":
	n = int(raw_input())
	student_records = {}
	s = 0
	flag = 0
	if n >= 2 and n <= 100:
		for _ in range(n):
			line = raw_input()
			line = line.split()
			name,scores = line[0],line[1:]
			scores = map(float, scores)
			student_records[name] = scores
		querry_name = raw_input()
		querry_score_list = student_records[querry_name]
#		print querry_score_list
#		print querry_score_list[1]
		for i in range(3):
			if querry_score_list[i] >= 0.0 and querry_score_list[i] <= 100.0:
#				print querry_score_list[i]
				flag = 1
#		print flag
		if flag == 1:
			for i in range(3):
				s = s + querry_score_list[i]
			avg = float(s/3)
			print "%.2f" % (avg)
