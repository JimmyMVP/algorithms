import sys
import timeit
import math

numbers=[]
f = open("algorithm_data", "r")
o = open("sorted", "w")
for line in f:
	line = line.strip()
	numbers.append(int(line))

############MERGE_SORT#################

def merge_sort(numbers):
	if(len(numbers) == 1):
		return numbers
	
	middle = int(len(numbers)/2)
	left = merge_sort(numbers[0:middle])
	right = merge_sort(numbers[middle:len(numbers)])
	return merge(left, right)

def merge(left, right):
	merged = []
	while len(left) > 0 and len(right) > 0:
		if left[0] < right[0]:
			merged.append(left[0])
			del left[0]
		else:
			merged.append(right[0])
			del right[0]
	#At least one of them is empty
	merged.extend(left)
	merged.extend(right) 
	return merged
  

##############INSERTION_SORT######################

def selection_sort(numbers):
	s = []
	while len(numbers) > 0:
		m = numbers[0]
		index_m = 0
		#Find lowest element
		for i in range(0, len(numbers)):
			if (numbers[i] > m):
				index_m = i
				m = numbers[i]
		#Append element to the beginning
		s.append(numbers[index_m])
		del numbers[index_m]
	return s


#############BUBBLE_SORT##########################

def swap(i, j, array):
	tmp = array[i]
	array[i] = array[j]
	array[j] = tmp

def bubble_sort(numbers):
	
	s = numbers
	swapped = True
	while(swapped):
		swapped = False
		for i in range(0, len(numbers) - 1):
			j = i + 1
			if s[i] > s[j]:
				swap(i,j,s)
				swapped = True
	return s

#############QUICK_SORT##############################

def quick_sort(numbers):
	s = []
	if(len(numbers) <= 1):
		return numbers
	#Pick pivot
	pivot = numbers[len(numbers) / 2]
	del numbers[len(numbers) / 2]
	larger = []
	smaller = []
	for element in numbers:
		if element >= pivot:
			larger.append(element)
		else:
			smaller.append(element)
	a = quick_sort(smaller)
	b = quick_sort(larger)			
	s.extend(a)
	s.extend([pivot])
	s.extend(b)
	return s


##########INSERTION_SORT###################

def insertion_sort(numbers):
	k = 0
	while k < len(numbers):
		ins = False
		for	i in range(k, len(numbers)):
			if(numbers[i] <= numbers[k]):
				for j in range(0, k+1):
					if(numbers[i] <= numbers[j]):
						tmp = numbers[i]
						del numbers[i]
						numbers.insert(j, tmp)
						k+=1
						break
	return numbers



#############RADIX_SORT############################


def radix_sort(numbers):

	i = 0
	l = len(numbers)
	while True:
		buckets = [[] for x in range(0,10)] 
		for n in numbers:
			num = str(n)
			if(len(num) < i):
				index = 0
			else:
				index = int(num[-i])
			buckets[index].append(n)
		numbers = []
		for bucket in buckets:
			for n in bucket:
				numbers.append(n)
		if(len(buckets[0])  == l):
			break
		i+=1
	return numbers


#############SHELL_SORT######################

def shell_sort(numbers):
	step = len(numbers)-1
	while step != 0:
		sw = False
		for i in range(0, len(numbers), step):
			if(i+step >= len(numbers)):
				if(not sw):
					step = int(step/2)
				break
			if(numbers[i] < numbers[i+step]):
				swap(i, i+step, numbers)
				sw = True
	return numbers

#############HEAP_SORT########################

def arrange_heap(array):

	#Arrange max heap
	switch = True
	while(switch):
		switch = False
		for i in range(len(numbers)-2**int(math.sqrt(len(numbers))), -1, -1):
			try:
				if(numbers[2*i+1] < numbers[i]):
					swap(2*i+1, i, numbers)
					switch = True
				if(numbers[2*i+2] < numbers[i]):
					swap(2*i+2, i, numbers)
					switch = True
			except:
				pass

def heap_sort(numbers):

	s = []
	while(len(numbers) > 0):
		arrange_heap(numbers)
		s.append(numbers[0])
		del numbers[0]	
	return s


#################BUCKET_SORT###################

def bucket_sort(numbers, sort="quick"):
	bucket_length = 1000
	buckets = [[] for x in range(bucket_length)]
	m = max(numbers)
	for n in numbers:
		buckets[int(n/m * (bucket_length-1))].append(n)

	s = []
	for b in buckets:
		s.extend(sorts[sort](b))

	return s

sorts = {"merge" : merge_sort, "bubble" : bubble_sort, "selection" : selection_sort, \
"quick" : quick_sort, "insertion" : insertion_sort, "radix" : radix_sort}



numbers = numbers[0:100000]


if __name__ == '__main__':
	
	import timeit
	
	print merge_sort(numbers)

	