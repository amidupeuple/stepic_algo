### naive implementation of priority queue
storage = []

def pq_insert(a, fa):
	storage.append((a, fa))

def pq_pop_low_priority():
	sortedStorage = sorted(storage, key=lambda x: x[1])
	minElement = sortedStorage[0]
	storage.remove(minElement)
	return minElement

def pq_contains(c):
	listOfKeys = [x[0] for x in storage]
	return c in listOfKeys
#----------------------------------------


def encode(s):
	#this for loop fills queue
	for c in s:
		if not(pq_contains(c)):
			counter = 0			
			for x in s:
				if x == c: counter += 1
			pq_insert(c, counter)

def main():
	s = input()
	encode(s)
	print(storage)
	

if __name__ == "__main__":
	main()


