def merge(t1, t2):
    o1 = o2 = 0
    arr1 = t1[0]
    arr2 = t2[0]
    arr = []
    counter = 0

    while o1 != len(arr1) and o2 != len(arr2):
        if arr1[0 + o1] > arr2[0 + o2]:
            counter += (len(arr2) - o2)
            arr.append(arr2[0 + o2])
            o2 += 1
        else:
            arr.append(arr1[0 + o1])
            o1 += 1

    if o1 == len(arr1):
        while o2 != len(arr2):
            arr.append(arr2[0 + o2])
            o2 += 1
    if o2 == len(arr2):
        while o1 != len(arr1):
            arr.append(arr1[0 + o1])
            counter += len(arr2)
            o1 += 1

    return arr, (counter + t1[1] + t2[1])


def count_numb_of_inversions(arr, l, r):
    if l < r:
        m = int((l + r) / 2)
        return merge(count_numb_of_inversions(arr, l, m), count_numb_of_inversions(arr, m+1, r))
    else:
        return arr[l:r+1], 0


def main():
    '''n = int(input())
    init_arr = [int(x) for x in input().split(' ')]
    assert n == len(init_arr)'''
    init_arr = [3, 5, 1, 4, 6, 2, 7, 8]
    print(count_numb_of_inversions(init_arr, 0, len(init_arr)-1)[1])


if __name__ == '__main__':
    main()
