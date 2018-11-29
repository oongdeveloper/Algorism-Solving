def sum_a(progresses, speeds):
	return [sum(z) for z in zip(progresses, speeds)]


def calsolution1(progresses, speeds):
	answer = []
	idx = 0
	while idx < len(progresses):
		if progresses[idx] >= 100:
			cnt = 0
			while idx < len(progresses):
				if progresses[idx] < 100:
					break
				cnt += 1
				idx += 1
				answer.append(cnt)
		progresses = sum_a(progresses, speeds)
	return answer

	
def calsolution2(progresses, speeds):
	answer = []
	while progresses:
		days = 1
		for i in range(len(speeds)):
			progresses[i] += speeds[i]
		cnt = 0
		while progresses:
			if progresses[0] >= 100:
				progresses.pop(0)
				speeds.pop(0)
				cnt += 1
			else:
				break
		if cnt:
			answer.append(cnt)
		return answer
	
def calsolution3(progresses, speeds):
	Q=[]
	pr_q = []
	for p, s in zip(progresses, speeds):
		
		if len(Q)==0 or Q[-1][0]<(100-int(p))//int(s):
			if len(Q) != 0:
				print( " q = " + str(Q[-1][0]))
			Q.append([(100-int(p))//int(s),1])
		else:
			print( " q -1 1= " + str(Q[-1][1]))
			Q[-1][1]+=1
	print (Q)
	for q in Q:
		pr_q.append(q[1])
		
	print (pr_q)

if __name__ == '__main__':
	progresses = ["99", "85", "92", "20"]
	speeds = ["1", "15", "8", "15"]
	calsolution3(progresses,speeds)
