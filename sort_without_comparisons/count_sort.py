def sort_count(arr):
    res = [0 for i in range(len(arr))]
    freqs = [0 for i in range(11)]
    for n in arr:
        freqs[n] += 1
    for j in range(1, len(freqs)):
        freqs[j] = freqs[j] + freqs[j-1]
    for i in reversed(range(len(arr))):
        res[freqs[arr[i]]-1] = arr[i]
        freqs[arr[i]] -= 1

    return res


def main():
    n = int(input())
    arr = [int(x) for x in input().split(' ')]
    assert n == len(arr)
    # arr = [2, 3, 9, 2, 9]
    print(' '.join([str(x) for x in sort_count(arr)]))


if __name__ == "__main__":
    main()