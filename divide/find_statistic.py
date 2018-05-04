from random import randint


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def partition(arr, l, r):
    o = randint(l, r)
    swap(arr, l, o)
    j = l
    offset = 0
    for i in range(l+1, r+1):
        if arr[i] < arr[l]:
            j += 1
            swap(arr, j, i)
            if offset != 0:
                swap(arr, j + offset + 1, i)
        elif arr[i] == arr[l]:
            offset += 1
            swap(arr, j + offset, i)
    swap(arr, l, j)
    return j, j + offset


def find_k_position(arr, l, r, k):
    if l >= r:
        return arr[l]

    m1, m2 = partition(arr, l, r)
    if k < m1:
        return find_k_position(arr, l, m1 - 1, k)
    elif m1 <= k <= m2:
        return arr[m1]
    elif k > m2:
        return find_k_position(arr, m2 + 1, r, k)


def main():
    arr = [2, 3, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9]
    k = 3
    print(find_k_position(arr, 0, len(arr) - 1, k))


if __name__ == '__main__':
    main()
