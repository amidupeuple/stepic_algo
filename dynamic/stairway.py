def find_max_sum(arr):
    n = len(arr)
    d = [0 for i in range(n + 1)]

    i = 1
    while i < len(d):
        if (i == len(d) - 1) or d[i-1] + arr[i-1] > d[i - 1] + arr[i]:
            d[i] = d[i-1] + arr[i-1]
        else:
            i += 1
            d[i] = d[i-2] + arr[i-1]
        i += 1

    return str(d[len(d) - 1])



def main():
    n = int(input())
    arr = [int(x) for x in input().split(' ')]
    print(find_max_sum(arr))


if __name__ == "__main__":
    main()