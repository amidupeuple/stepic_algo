def gcd(a, b):
    print("a={}, b={}".format(a, b))
    if a == 0:
        print("gcd,b={}".format(b))
        return b
    elif b == 0:
        print("gcd,a={}".format(a))
        return a
    else:
        if a > b:
            return gcd(a % b, b)
        else:
            return gcd(a, b % a)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()