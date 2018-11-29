
def solution(array, commands):
	answer = []
	for command in commands:
		arr = array[command[0]-1:command[1]]
		
		arr.sort()
		print (arr[command[2]-1])
		answer.append(arr[command[2]-1])
	print (answer)
	return answer
	
def solution_other(array, commands):
	answer = []
	for command in commands:
		i,j,k = command
		#answer.append(list(sorted(array[i-1:j]))[k-1])
		#print ((sorted(array[i-1:j]))[k-1])
		answer.append((sorted(array[i-1:j]))[k-1])
	print (answer)
	return answer
	
if __name__ == '__main__':
	array = [1, 5, 2, 6, 3, 7, 4]
	commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
	#solution(array,commands)
	solution_other(array,commands)
