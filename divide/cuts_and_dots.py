from random import randint


def change_elements(arr, i1, i2):
    tmp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = tmp


def partition(arr, l, r):
    # ind = randint(l, r)
    ind = l
    x = arr[ind]
    # change_elements(arr, l, ind)

    j = l
    for i in range(l+1, r+1):
        if arr[i] <= x:
            j += 1
            change_elements(arr, j, i)
    change_elements(arr, l, j)
    return j


def quick_sort(arr, l, r):
    while l < r:
        m = partition(arr, l, r)
        quick_sort(arr, l, m - 1)
        l = m + 1


def main():
    n = 2
    m = 3
    cuts = [(0, 5), (7, 10)]
    cuts = [3, 4, 2, 6, 1, 1, 8, 2, 4, 7, 4]
    dots = [1, 6, 11]
    quick_sort(cuts, 0, len(cuts)-1)
    print(cuts)


if __name__ == "__main__":
    main()
