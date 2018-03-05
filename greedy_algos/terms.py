def get_terms(n):
	i = 1
	terms = []
	while n:
		if not((n-i) <= i) or ((n-i) == 0):
			terms.append(i)
			n -= i
		i += 1
	return terms		


def main():
	n = int(input())
	arr = get_terms(n)
	print(len(arr))
	print(" ".join([str(a) for a in arr]))

if __name__ == "__main__":
	main()
