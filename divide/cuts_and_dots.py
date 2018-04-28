from random import randint
from bisect import bisect_left, bisect_right
import time


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

    return ind


def extract_array(arr, key_ind):
    res = []
    for a in arr:
        res.append(a[key_ind])
    return res


def get_number_of_cuts_for_each_dot_v2(cuts_left, cuts_right, dots):
    numbs = []
    for d in dots:
        tmp = extract_array(cuts_left, 0)
        ind1 = bisect_right(tmp, d)

        tmp = extract_array(cuts_right, 1)
        ind2 = bisect_left(tmp, d)

        arr_c = list(filter(lambda x: x in cuts_left[:ind1], cuts_right[ind2:]))

        numbs.append(len(arr_c))
    return numbs


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


def get_number_of_cuts_for_each_dot_old(cuts, dots):
    numbs = []
    for d in dots:
        ind = find_index(cuts, 0, len(cuts) - 1, d, 0)

        new_cuts = cuts[0:ind]
        quick_sort(new_cuts, 0, ind - 1, 1)

        ind2 = find_index(new_cuts, 0, ind - 1, d, 1)

        if ind2 <= 0:
            c = len(new_cuts)
        elif ind2 > (len(new_cuts) - 1):
            c = 0
        else:
            c = len(new_cuts) - ind2 - 1

        numbs.append(c)
    return numbs


def main():
    sizes = [10, 50, 100, 200, 500, 1000]
    test(sizes, 0, 20)


def test(sizes, mi, ma):
    for s in sizes:
        print("size: {}".format(s))
        cuts = []
        dots = []
        for i in range(s):
            x1 = randint(mi, ma)
            x2 = randint(mi, ma)
            while x2 < x1:
                x2 = randint(mi, ma)
            cuts.append((x1, x2))
        for i in range(s):
            x = randint(mi, ma)
            dots.append(x)

        t0 = time.perf_counter()
        cuts_left = cuts[:]
        cuts_right = cuts[:]
        cuts_left.sort(key=lambda tup: tup[0])
        cuts_right.sort(key=lambda tup: tup[1])
        res1 = get_number_of_cuts_for_each_dot_v2(cuts_left, cuts_right, dots)
        t1 = time.perf_counter()
        print("v2 finished: {0:.7f}".format((t1 - t0)))

        t0 = time.perf_counter()
        cuts2 = cuts[:]
        cuts2.sort(key=lambda tup: tup[0])
        res2 = get_number_of_cuts_for_each_dot(cuts2, dots)
        t1 = time.perf_counter()
        print("New finished: {0:.7f}".format((t1 - t0)))
        print("Results are matched?: {}".format((res1 == res2)))
        print(res1[:100])
        print(res2[:100])
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')


if __name__ == "__main__":
    main()
