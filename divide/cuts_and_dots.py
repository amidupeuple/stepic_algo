from random import randint


def change_elements(arr, i1, i2):
    tmp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = tmp


def compare_cuts(c1, c2):
    if c1[0] < c2[0]:
        return -1
    elif c1[0] == c2[0]:
        if c1[1] < c2[1]:
            return -1
        elif c1[1] == c2[1]:
            return 0
        elif c1[1] > c2[1]:
            return 1
    elif c1[0] > c2[0]:
        return 1


def partition(arr, l, r):
    ind = randint(l, r)
    # ind = l
    x = arr[ind]
    change_elements(arr, l, ind)

    j = l
    for i in range(l+1, r+1):
        if compare_cuts(arr[i], x) <= 0:
            j += 1
            change_elements(arr, j, i)
    change_elements(arr, l, j)
    return j


def quick_sort(arr, l, r):
    while l < r:
        m = partition(arr, l, r)
        if m > ((l + r) / 2):
            quick_sort(arr, m + 1, r)
            r = m - 1
        else:
            quick_sort(arr, l, m - 1)
            l = m + 1


def get_number_of_cuts_for_each_dot(cuts, dots):
    numbs = []
    for d in dots:
        ind = len(cuts)
        l = 0
        r = len(cuts) - 1
        while l <= r:
            m = (l + r) // 2
            if cuts[m][0] == d:
                ind = m
                break
            elif cuts[m][0] > d:
                r = m -1
            elif cuts[m][0] < d:
                l = m + 1
        ind = m
        while cuts[ind][0] == d:
            ind += 1

        l = 0
        r = ind - 1
        ind2 = 0
        while l <= r:
            m = (l + r) // 2
            if cuts[m][1] == d:
                ind2 = m
                break
            elif cuts[m][1] > d:
                r = m -1
            elif cuts[m][1] < d:
                l = m + 1

        while cuts[ind2][1] == d:
            ind2 -= 1

        c = ind - ind2 - 1

        numbs.append(c)
    return numbs


def main():
    # n, m = [int(x) for x in input().split(' ')]
    # cuts = []
    # for i in range(n):
    #     cuts.append([int(x) for x in input().split(' ')])
    # dots = [int(x) for x in input().split(' ')]
    # n = 2
    # m = 3
    cuts = [(0, 5), (7, 10), (0, 1), (1, 3), (7, 11)]
    dots = [1, 6, 11]
    quick_sort(cuts, 0, len(cuts)-1)
    # print(cuts)
    # print(dots)
    print(' '.join([str(x) for x in get_number_of_cuts_for_each_dot(cuts, dots)]))


if __name__ == "__main__":
    main()
