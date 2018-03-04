def find_dots(linesArr):
	dots = []
	while linesArr:
		#print("+ {}".format(linesArr))
		rmin = linesArr[0][1]
		for l in linesArr:
			if l[1] <= rmin: 
				rmin = l[1]
		#print("rmin={}".format(rmin))
		delIndxs = []
		for i, l in enumerate(linesArr):
			if l[0] <= rmin:
				delIndxs.append(i)
		for j in sorted(delIndxs, reverse=True):
			del linesArr[j]
		dots.append(rmin)
	return dots


def main():
	n = int(input())
	lines = []
	for i in range(n):
		l, r = map(int, input().split())
		lines.append((l, r))
	#print(lines)
	#lines = [(1, 3), (2, 5), (3, 6)]
	res = find_dots(lines)
	print(len(res))
	print(" ".join([str(a) for a in res]))

if __name__ == "__main__":
	main()
