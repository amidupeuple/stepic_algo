def find_max_weight(W, arrw):
    D = []
    for i in range(W + 1):
        D.append([0 for j in range(len(arrw) + 1)])
    for i in range(1, len(arrw) + 1):
        for w in range(1, W + 1):
            D[w][i] = D[w][i-1]
            if arrw[i - 1] <= w:
                D[w][i] = max(D[w][i], D[w - arrw[i - 1]][i - 1] + arrw[i - 1])
    return D[W][len(arrw)]


def test():
    W = 10
    n = 3
    arrw = [1, 4, 8]
    find_max_weight(W, arrw)


def main():
    tmpa = [int(s) for s in input().split()]
    W = tmpa[0]
    n = tmpa[1]
    arrw = [int(s) for s in input().split()]
    assert n == len(arrw)
    print(find_max_weight(W, arrw))


if __name__ == "__main__":
    main()