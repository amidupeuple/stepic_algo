from random import randint
from bisect import bisect_left, bisect_right


def change_elements(arr, i1, i2):
    tmp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = tmp


def compare_cuts(c1, c2):
    if c1 < c2:
        return -1
    elif c1 == c2:
        return 0
    elif c1 > c2:
        return 1


def partition(arr, l, r):
    ind = randint(l, r)
    x = arr[ind]
    change_elements(arr, l, ind)

    j = l
    offset = 0
    for i in range(l+1, r+1):
        if compare_cuts(arr[i], x) < 0:
            j += 1
            if offset != 0:
                change_elements(arr, j, i)
                change_elements(arr, j + offset, i)
            else:
                change_elements(arr, j, i)
        elif compare_cuts(arr[i], x) == 0:
            offset += 1
            change_elements(arr, j + offset, i)

    change_elements(arr, l, j)
    return j, offset


def quick_sort(arr, l, r):
    while l < r:
        m, o = partition(arr, l, r)
        if m - l > r - o:
            quick_sort(arr, o + 1, r)
            r = m - 1
        else:
            quick_sort(arr, l, m - 1)
            l = m + o + 1


def get_number_of_cuts_for_each_dot(cuts_left, cuts_right, dots):
    numbs = []
    for d in dots:
        ind1 = bisect_right(cuts_left, d)

        ind2 = bisect_left(cuts_right, d)

        numbs.append(ind1 - ind2)
    return numbs


def main():
    n, m = [int(x) for x in input().split(' ')]
    cuts = []
    for i in range(n):
        cuts.append([int(x) for x in input().split(' ')])
    dots = [int(x) for x in input().split(' ')]

    cuts_left = [e[0] for e in cuts]
    cuts_right = [e[1] for e in cuts]
    quick_sort(cuts_left, 0, len(cuts_left) - 1)
    quick_sort(cuts_right, 0, len(cuts_left) - 1)

    print(' '.join([str(x) for x in get_number_of_cuts_for_each_dot(cuts_left, cuts_right, dots)]))


if __name__ == "__main__":
    main()
