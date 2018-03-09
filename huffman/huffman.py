storage = []

def pq_insert(a, fa):
	storage.append((a, fa))

def pq_pop_low_priority():
	sortedStorage = sorted(storage, key=lambda x: (x[1], x[0]))
	minElement = sortedStorage[0]
	i = 0
	while len(minElement[0]) > 1:
		i += 1
		minElement = sortedStorage[i]
	storage.remove(minElement)
	return minElement
	
def pq_pop_low_priority_not_leaf():
	sortedStorage = sorted(storage, key=lambda x: (x[1], x[0]))
	minElement = sortedStorage[0]
	i = 0
	while len(minElement[0]) == 1:
		i += 1
		if i >= len(sortedStorage):
			minElement = sortedStorage[0]
			break
		minElement = sortedStorage[i]
	storage.remove(minElement)
	return minElement

def pq_contains(c):
	listOfKeys = [x[0] for x in storage]
	return c in listOfKeys

def build_tree(s):
	for c in s:
		if not(pq_contains(c)):
			counter = 0			
			for x in s:
				if x == c: counter += 1
			pq_insert(c, counter)
	tree = ()
	if len(storage) == 1:
		min = pq_pop_low_priority()
		return (min[0], min[1])	
	min1 = pq_pop_low_priority()	
	min2 = pq_pop_low_priority()
	new = ((min2[0]+min1[0]), (min2[1]+min1[1]))
	pq_insert(new[0], new[1])
	tree = (min1, min2)	
	while len(storage) > 1:
		min1 = pq_pop_low_priority()	
		min2 = pq_pop_low_priority_not_leaf()
		new = ((min2[0]+min1[0]), (min2[1]+min1[1]))
		pq_insert(new[0], new[1])
		tree = (min1, tree)
	return tree	
	
def create_dict(s, tree):	
	codes = {}
	prefix = ""
	isBottom = False
	
	if isinstance(tree[1], int):
		return {tree[0]: "1"}
	
	while True:
		curNode = tree[0]
		codes[curNode[0]] = prefix + "0"
		curNode = tree[1]
		if isinstance(curNode[1], int):
			codes[curNode[0]] = prefix + "1"
			break
		else:
			prefix += "1"
			tree = curNode	
	return codes
 
def encode(s, codes):
	encoded = ""
	for c in s:
		encoded += str(codes[c])
	return encoded

def main():
	s = input()
	#s = "yyyyyyyyyyyyyyyeweggggggggggggggfsdddddddddddddfgjwwwwwwwwwwwwwwwwwwwwwwwggggggggggggggggggggdsssssssssssss"
	tr = build_tree(s)
	codes = create_dict(s, tr)
	codes = create_dict(s, tr)
	encoded = encode(s, codes)
	print(len(codes), len(encoded))
	for k, v in codes.items():
		print("{}: {}".format(k, v))
	print(encoded)

if __name__ == "__main__":
	main()


