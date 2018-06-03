def find_min_number_of_operations(n):
    d = [float("inf") for i in range(n + 1)]
    arr = ["" for i in range(n)]
    arr[0] = "1"
    d[0] = 0
    d[1] = 0
    for i in range(2, n + 1):
        for j in range(1, 4):
            if j == 1:
                d[i] = min(d[i], d[i-1] + 1)
                arr[d[i-1] + 1] += str(i)
            elif j == 2 and (i % 2) == 0:
                d[i] = min(d[i], d[int(i / 2)] + 1)
                arr[d[int(i / 2)] + 1] += str(i)
            elif j == 3 and (i % 3) == 0:
                d[i] = min(d[i], d[int(i / 3)] + 1)
                arr[d[int(i / 3)] + 1] += str(i)
    arr = [float("-inf") for i in range(n + 1)]
    arr[-1] = d[n]
    return d[n], find_sequence(arr)


def find_sequence(arr):
    for i in range(len(arr) - 1, -1, -1):
        for j in range(1, 4):
            if j == 1 and arr[i] > 0:
                arr[i-1] = max(arr[i-1], arr[i] - 1)
            elif j == 2 and (i % 2 == 0) and arr[i] > 0:
                arr[int(i / 2)] = max(arr[int(i / 2)], arr[i] - 1)
            elif j == 3 and (i % 3 == 0) and arr[i] > 0:
                arr[int(i / 3)] = max(arr[int(i / 3)], arr[i] - 1)
    c = 1
    res = [1]
    prev = 1
    for i in range(len(arr)):
        if arr[i] == c and (i == prev + 1 or i == prev * 2 or i == prev * 3):
            prev = i
            c += 1
            res.append(i)
    return res


def test():
    n = 9
    k, arr = find_min_number_of_operations(n)
    assert k == 2 and arr == [1, 3, 9]
    n = 1
    k, arr = find_min_number_of_operations(n)
    assert k == 0 and arr == [1]
    n = 5
    k, arr = find_min_number_of_operations(n)
    assert k == 3 and arr == [1, 2, 4, 5]
    n = 96234
    k, arr = find_min_number_of_operations(n)
    assert k == 14 and arr == [1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234]


def main():
    n = int(input())
    k, arr = find_min_number_of_operations(n)
    print(str(k))
    print(" ".join(str(x) for x in arr))


if __name__ == "__main__":
    main()
    # test()b