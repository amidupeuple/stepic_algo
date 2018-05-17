def lis(arr):
    subs = [1 for i in range(len(arr))]
    for i in range(1, len(arr)):
        for j in range(0, i):
            if (arr[i] % arr[j] == 0) and (subs[j] + 1 > subs[i]):
                subs[i] = subs[j] + 1
    ans = 0
    for i in range(len(subs)):
        if subs[i] > ans:
            ans = subs[i]
    return ans


def main():
    n = int(input())
    arr = [int(x) for x in input().split(' ')]
    assert n == len(arr)
    # arr = [3, 6, 7, 12]
    print(lis(arr))


if __name__ == "__main__":
    main()