# 소수 찾기 _ 완전 탐색


import itertools
import math
import time

prime_num = []

def solution(numbers):
	answer = 0
	for i in range(1,len(numbers)+1):
		
		find_prime(numbers,i)
	
	print (prime_num)
	answer = len(prime_num)
	print (answer)
	return answer

def find_prime(numbers,i):
	arrlist = list(numbers)
	mypermuatation =  itertools.permutations(arrlist,i)

	for myarr in mypermuatation:
		num = int(''.join(myarr))
	
		flag = True
		if (num<2):	
			continue
			
		for j in range(2,int(math.sqrt(num))+1):
			if (num % j == 0):
				
				flag = False
				break
		if (flag == False):
			continue
		
		if (num not in prime_num):
			prime_num.append(num)
	#print (prime_num)
	

def solution_other(numbers):
	answer = 0
	candidates, num_set = [], set()
	digits = [digit for digit in numbers]

	for i in range(1, len(numbers)+1):
		candidates += [*list(itertools.permutations(digits, i))]

	for candidate in candidates:
		num_set.add(int(''.join(map(str, candidate))))

	for num in num_set:
		if is_prime_other(num):
			answer += 1

	print ("others ",answer)
	return answer

def is_prime_other(number):
	if number == 0 or number == 1:
		return False

	for i in range(2, number//2 + 1):
		if (number/i) == (number//i):
			return False

	return True

	
	
if __name__=='__main__':
	numbers = '52169'
	start_time = time.time() 
	solution(numbers)
	print ("----- %s seconds ----- {}".format(time.time() - start_time))
	
	start_time = time.time() 
	solution_other(numbers)
	print ("----- %s seconds ----- {}".format(time.time() - start_time))
