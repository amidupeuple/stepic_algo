def fib(n):
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
    
def main():
    n, m = map(int, input().split())
    print(fib_remainder(n, m))
    print(fib(n) % m)

if __name__ == "__main__":
    main()