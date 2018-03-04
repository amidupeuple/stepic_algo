import random

def gcd_naive(a, b):
	assert a >= 0 and b >= 0
	for d in reversed(range(max(a, b) + 1)):
		if d == 0 or a % d == b % d == 0:
			return d

def gcd_recursion(a, b):
    #print("a={}, b={}".format(a, b))
    if a == 0:
        #print("gcd,b={}".format(b))
        return b
    elif b == 0:
        #print("gcd,a={}".format(a))
        return a
    else:
        if a > b:
            return gcd(a % b, b)
        else:
            return gcd(a, b % a)

def gcd_recursion_x(a, b):
	'''
	здесь используется факт, что рекурсивный вызов всегда строго чередуется
	'''
	assert a>= 0 and b >= 0
	if a == 0 or b == 0:
		return max(a, b)
	return gcd_recursion(b % a, a)

def gcd(a, b):
	while a and b:
		if a > b:
			a %= b
		else:
			b %= a
	return max(a, b)


def test_gcd(gcd, n_iter=100):
	for i in range(n_iter):
		c = random.randint(0, 1024)
		a = c * random.randint(0, 128)
		b = c * random.randint(0, 128)
		assert gcd(a, a) == gcd(a, 0) == a
		assert gcd(b, b) == gcd(b, 0) == b
		assert gcd(a, 1) == gcd(b, 1) == 1
		d = gcd(a, b)
		assert a % d == b % d == 0


'''def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()'''
