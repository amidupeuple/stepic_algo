def lds(arr):
    D = [1 for i in range(len(arr))]
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] <= arr[j] and (D[j] + 1) > D[i]:
                D[i] = D[j] + 1

    m = 0
    for i in range(len(D)):
        if D[i] > m:
            m = D[i]

    s = m
    res = []
    if m == 1:
        m = 0
    prev = arr[m]
    while len(res) != s:
        if arr[m] >= prev:
            prev = arr[m]
            res.append(m + 1)
            if m != 0:
                m = D[D[m]] - 1
        else:
            m -= 1
    res.reverse()
    return s, res


def test():
    n, a = lds([1])
    assert n == 1 and len(a) == 1 and a[0] == 1
    n, a = lds([5, 3, 4, 4, 2])
    assert n == 4 and len(a) == 4


def main():
    # n = int(input())
    # arr = [int(x) for x in input().split(' ')]
    # assert n == len(arr)
    arr = [5, 3, 4, 4, 2]
    n, arr_ind = lds(arr)
    print(str(n))
    print(' '.join([str(x) for x in arr_ind]))


if __name__ == "__main__":
    test()