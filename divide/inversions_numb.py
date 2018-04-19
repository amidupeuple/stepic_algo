def merge(t1, t2):
    arr1 = t1[0]
    arr2 = t2[0]
    counter = 0
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] > arr2[j]:
                counter += 1
    arr1.extend(arr2)
    return arr1, (counter + t1[1] + t2[1])


def count_numb_of_inversions(arr, l, r):
    if l < r:
        m = int((l + r) / 2)
        return merge(count_numb_of_inversions(arr, l, m), count_numb_of_inversions(arr, m+1, r))
    else:
        return arr[l:r+1], 0


def main():
    n = int(input())
    init_arr = [int(x) for x in input().split(' ')]
    assert n == len(init_arr)
    print(count_numb_of_inversions(init_arr, 0, len(init_arr)-1)[1])


if __name__ == '__main__':
    main()
