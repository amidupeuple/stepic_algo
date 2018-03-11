class TreeNode:
	def __init__(self, label, freq):
		self.label = label
		self.freq = freq
		self.left = self.right = self.parent = None
		
	def set_parent(self, parent):
		self.parent = parent
		
	def set_left(self, left):
		self.left = left
		
	def set_right(self, right):
		self.right = right

	def __str__(self):
		return ("label: {}, freq: {}").format(self.label, self.freq)

storage = []

def print_tree(root):
	if root.left == None and root.right == None:
		print(root)
		return
	print_tree(root.left)
	print_tree(root.right)

def pq_insert(x):
	storage.append(x)

def pq_pop_low_priority():
	sortedStorage = sorted(storage, key=lambda x: (x.freq, x.label))
	minElement = sortedStorage[0]
	storage.remove(minElement)
	return minElement

def pq_contains(c):
	listOfKeys = [x.label for x in storage]
	return c in listOfKeys

def build_tree(s):
	for c in s:
		if not(pq_contains(c)):
			counter = 0			
			for x in s:
				if x == c: counter += 1
			pq_insert(TreeNode(c, counter))
	
	if len(storage) == 1:
		return storage
	
	while len(storage) > 1:
		min1 = pq_pop_low_priority()	
		min2 = pq_pop_low_priority()
		new = TreeNode(min1.label+min2.label, min1.freq+min2.freq)
		new.left = min2
		new.right = min1
		min2.parent = new
		min1.parent = new
		pq_insert(new)
	return storage

codes = {}
def create_dict(root, prefix):	
	if root.left == None and root.right == None:
		if prefix == "": prefix = "1"
		codes[root.label] = prefix
		return
	create_dict(root.left, prefix+"1")
	create_dict(root.right, prefix+"0")
	
	
def encode(s, codes):
	encoded = ""
	for c in s:
		encoded += str(codes[c])
	return encoded

def main():
	s = input()
	build_tree(s)
	create_dict(storage[0], "")
	encoded = encode(s, codes)
	print(len(codes), len(encoded))
	for k, v in codes.items():
		print("{}: {}".format(k, v))
	print(encoded)
	

if __name__ == "__main__":
	main()


