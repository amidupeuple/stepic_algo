from bisect import bisect_left

def test_lds():
    n, a = lds([1])
    assert n == 1
    n, a = lds([5, 3, 4, 4, 2])
    assert n == 4
    n, a = lds([5, 3, 4, 4, 2, 4, 4, 4, 4, 4])
    assert n == 8


def test_find_pos():
    n = find_pos([5], 0, 0, 3)
    assert n == 1
    n = find_pos([5, 4, 4, 2], 0, 3, 3)
    assert n == 3
    n = find_pos([], 0, 0, 1)
    assert n == 0
    n = find_pos([5, 4, 4, 3, 3, 3, 3, 3, 3, 2], 0, 9, 3)
    assert n == 9


def lis(a):
    seqs = []
    seqs.append(a[0])
    l = 1
    indxs = []
    indxs.append([0])

    for i in range(1, len(a)):
        j = bisect_left(seqs, a[i])
        if j == 0:
            seqs[0] = a[i]
            indxs[0] = [i]
        elif j == len(seqs):
            seqs.append(a[i])
            l += 1
            tmp = indxs[len(indxs) - 1][:]
            tmp.append(i)
            indxs.append(tmp)
        else:
            if j + 1 == len(seqs):
                seqs.append(a[i])
                l += 1
                tmp = indxs[len(indxs) - 1][:]
                tmp.append(i)
                indxs.append(tmp)
            else:
                seqs[j] = a[i]
                indxs[j][len(indxs[j]) - 1] = i

    print('E N D')


def find_pos(a, l, r, e):
    while l <= r and a:
        m = (l + r) // 2
        if a[m] < e:
            return find_pos(a, l, m - 1, e)
        elif a[m] > e:
            return find_pos(a, m + 1, r, e)
        else:
            while a[m] == e:
                m += 1
                if m == len(a):
                    break
            return m
    return l


def lds(a):
    seqs = []
    seqs.append(a[0])
    l = 1
    indxs = []
    indxs.append([0])

    for i in range(1, len(a)):
        j = find_pos(seqs, 0, len(seqs) - 1, a[i])
        if j == len(seqs):
            seqs.append(a[i])
            l += 1
            tmp = indxs[len(indxs) - 1][:]
            tmp.append(i)
            indxs.append(tmp)
        elif j == 0:
            seqs[0] = a[i]
            indxs[0] = [i]
        else:
            if j == len(seqs):
                seqs.append(a[i])
                l += 1
                tmp = indxs[len(indxs) - 1][:]
                tmp.append(i)
                indxs.append(tmp)
            else:
                seqs[j] = a[i]
                indxs[j][len(indxs[j]) - 1] = i
    return l, indxs[len(indxs) - 1]


def main():
    n = int(input())
    arr = [int(x) for x in input().split(' ')]
    assert n == len(arr)
    n, arr_ind = lds(arr)
    print(str(n))
    print(' '.join([str(x + 1) for x in arr_ind]))


if __name__ == "__main__":
    # test_lds()
    # test_find_pos()
    main()