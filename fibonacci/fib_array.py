from rcviz import viz
from functools import lru_cache
import time
from matplotlib import pyplot as plt

def fib_naive(n):
    assert n >= 0
    return n if n <= 1 else fib_naive(n-1) + fib_naive(n-2) 


global_cache = {}


def fib_global_cache(n):
	assert n >= 0
	if n not in global_cache:
		global_cache[n] = n if n <= 1 else fib_global_cache(n-1) + fib_global_cache(n-2)

	return global_cache[n]


def memo(f):
	'''
	custom 	decorator with local cache
	'''
	
	cache = {}
	
	def inner(n):
		if 	n not in cache:
			cache[n] = f(n)
		return cache[n]

	return inner

#it is possible to use lru cache for speed
#f = lru_cache(maxsize=None)(f)


def fib(n):
    '''
    computing of desired Fibonacci number:
    naive - via recursion 
    better - via massive
    here is modified massive-version
    '''
    prev = 0
    cur = 1
    
    for i in range(n-1):
        prev, cur = cur, prev + cur
    
    return cur

def fib_last_digit(n):
    prev = 0
    cur = 1
    
    for i in range(n-1):
        prev, cur = cur, ((prev + cur) % 10)
    
    return cur
    
def fib_remainder(n, m):
    a = [0, 1]
    for i in range(n-1):
        prev = a[-2]
        cur = a[-1]
        
        if a[0] == prev and a[1] == cur and len(a) > 2:
            l = len(a) - 2
            if l < n:
                return a[n % l]
            else:
                return a[l]
        
        a.append((prev + cur) % m)
    
    return a[-1]

def timed(f, *args, n_iter=100):
	acc = float("inf")
	for i in range(n_iter):
		t0 = time.perf_counter()
		f(*args)
		t1 = time.perf_counter()
		acc = min(acc, t1-t0)
	return acc


def compare(fs, args):
	for f in fs:
		plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
	plt.legend()
	plt.grid(True)
	plt.show()


