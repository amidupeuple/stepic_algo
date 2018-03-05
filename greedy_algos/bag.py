def get_max_cost(pieces, w):
	sortedPieces = sorted(pieces, key=lambda p: p[0]/p[1], reverse=True)
	resultCost = []
	i = 0
	while w and i < len(sortedPieces):
		if w <= sortedPieces[i][1]:
			newC = (sortedPieces[i][0]/sortedPieces[i][1]) * w
			resultCost.append(newC)
			w = 0
		else:
			resultCost.append(sortedPieces[i][0])			
			w = w - sortedPieces[i][1]
		i += 1
	return sum(resultCost)
			

def main():
	n, w = map(int, input().split())
	
	pieces = [tuple(map(int, input().split())) for _ in range(n)]
	
	'''n = 3
	w = 50
	pieces = [(60, 20), (100, 50), (120, 30)]'''

	print("{0:.3f}".format(get_max_cost(pieces, w)))

if __name__ == "__main__":
	main()
