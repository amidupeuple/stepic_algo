def find_max_sum(arr):
    n = len(arr)
    d = [float("-inf") for i in range(n + 1)]
    d[0] = 0
    d[1] = arr[0]
    for i in range(1, n + 1):
        for j in range(1, 3):
            if j == 1:
                d[i] = max(d[i], d[i - j] + arr[i - 1])
            elif j == 2 and i < len(arr):
                d[i+1] = max(d[i+1], d[i+1 - j] + arr[i])
    return str(d[len(d) - 1])


def test():
    # arr = [-1, 2, 1]
    # assert '3' == find_max_sum(arr)
    # arr = [1, 2]
    # assert '3' == find_max_sum(arr)
    # arr = [-5, -2, -6]
    # assert '-8' == find_max_sum(arr)
    arr = [-64, -16, -13, -9, -48]
    assert '-73' == find_max_sum(arr)
    arr = [3, 4, 10, 10, 0, -6, -10, 0]
    assert '21' == find_max_sum(arr)
    arr = [1, 1, -2, -4, -6, 2, 2]
    assert '2' == find_max_sum(arr)


def main():
    n = int(input())
    arr = [int(x) for x in input().split(' ')]
    print(find_max_sum(arr))


if __name__ == "__main__":
    main()
    # test()