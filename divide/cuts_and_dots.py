from random import randint


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
    # ind = l
    x = arr[ind]
    change_elements(arr, l, ind)

    j = l
    for i in range(l+1, r+1):
        if compare_cuts(arr[i], x, key_ind) <= 0:
            j += 1
            change_elements(arr, j, i)
    change_elements(arr, l, j)
    return j


def quick_sort(arr, l, r, key_ind):
    while l < r:
        m = partition(arr, l, r, key_ind)
        if m > ((l + r) / 2):
            quick_sort(arr, m + 1, r, key_ind)
            r = m - 1
        else:
            quick_sort(arr, l, m - 1, key_ind)
            l = m + 1


def find_index(arr, l, r, d, side):
    ind = m = 0
    while l <= r:
        m = (l + r) // 2
        if arr[m][side] == d:
            ind = m
            break
        elif arr[m][side] > d:
            r = m -1
        elif arr[m][side] < d:
            l = m + 1

    if r < 0:
        ind = r
    elif l > r:
        ind = l
    else:
        ind = m

    while (ind > 0 and (ind < len(arr))) and arr[ind][side] == d:
        if side == 0:
            ind += 1
        else:
            ind -= 1

    if ind == -1:
        ind = 0

    return ind


def get_number_of_cuts_for_each_dot(cuts, dots):
    numbs = []
    for d in dots:
        ind = find_index(cuts, 0, len(cuts) - 1, d, 0)

        new_cuts = cuts[0:ind]
        quick_sort(new_cuts, 0, ind - 1, 1)

        ind2 = find_index(new_cuts, 0, ind - 1, d, 1)

        c = len(new_cuts) - ind2

        numbs.append(c)
    return numbs


def main():
    n, m = [int(x) for x in input().split(' ')]
    cuts = []
    for i in range(n):
        cuts.append([int(x) for x in input().split(' ')])
    dots = [int(x) for x in input().split(' ')]
    # cuts = [(0, 5), (7, 10), (7, 11)]
    # dots = [1, 6, 11]
    quick_sort(cuts, 0, len(cuts)-1, 0)
    print(' '.join([str(x) for x in get_number_of_cuts_for_each_dot(cuts, dots)]))


if __name__ == "__main__":
    main()
