from random import randint
from bisect import bisect_left, bisect_right


def change_elements(arr, i1, i2):
    tmp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = tmp


def compare_cuts(c1, c2, key_ind):
    if c1[key_ind] < c2[key_ind]:
        return -1
    elif c1[key_ind] == c2[key_ind]:
        return 0
    elif c1[key_ind] > c2[key_ind]:
        return 1


def partition(arr, l, r, key_ind):
    ind = randint(l, r)
    x = arr[ind]
    change_elements(arr, l, ind)

    j = l
    offset = 0
    for i in range(l+1, r+1):
        if compare_cuts(arr[i], x, key_ind) < 0:
            j += 1
            if offset != 0:
                change_elements(arr, j, i)
                change_elements(arr, j + offset, i)
            else:
                change_elements(arr, j, i)
        elif compare_cuts(arr[i], x, key_ind) == 0:
            offset += 1
            change_elements(arr, j + offset, i)

    change_elements(arr, l, j)
    return j, offset


def quick_sort(arr, l, r, key_ind):
    while l < r:
        m, o = partition(arr, l, r, key_ind)
        if m - l > r - o:
            quick_sort(arr, o + 1, r, key_ind)
            r = m - 1
        else:
            quick_sort(arr, l, m - 1, key_ind)
            l = m + o + 1


def extract_array(arr, key_ind):
    res = []
    for a in arr:
        res.append(a[key_ind])
    return res


def get_number_of_cuts_for_each_dot(cuts, dots):
    numbs = []
    for d in dots:
        tmp = extract_array(cuts, 0)
        ind = bisect_right(tmp, d)

        new_cuts = cuts[0:ind]
        # quick_sort(new_cuts, 0, ind - 1, 1)
        new_cuts.sort(key=lambda tup: tup[1])
        tmp = extract_array(new_cuts, 1)

        ind2 = bisect_left(tmp, d)

        if ind2 <= 0:
            c = len(new_cuts)
        elif ind2 > (len(new_cuts) - 1):
            c = 0
        else:
            c = len(new_cuts) - ind2

        numbs.append(c)
    return numbs


def main():
    n, m = [int(x) for x in input().split(' ')]
    cuts = []
    for i in range(n):
        cuts.append([int(x) for x in input().split(' ')])
    dots = [int(x) for x in input().split(' ')]
    # cuts = [(6, 6), (0, 3), (1, 3), (2, 3), (3, 4), (3, 5), (3, 6)]
    # dots = [1, 2, 3, 4, 5, 6]
    # cuts = [(7, 10), (7, 10), (7, 11), (0, 5), (7, 10)]
    # dots = [1, 6, 11]
    # quick_sort(cuts, 0, len(cuts)-1, 0)
    cuts.sort(key=lambda tup: tup[0])
    print(' '.join([str(x) for x in get_number_of_cuts_for_each_dot(cuts, dots)]))


if __name__ == "__main__":
    main()
