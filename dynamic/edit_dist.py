def get_edit_dist(s1, s2):
    d = []
    for i in range(0, len(s1) + 1):
        d.append([0 for j in range(len(s2) + 1)])
    for i in range(0, len(s1) + 1):
        d[i][0] = i
    for j in range(len(s2) + 1):
        d[0][j] = j

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            c = 0 if s1[i-1] == s2[j-1] else 1
            d[i][j] = min([d[i][j-1] + 1, d[i-1][j] + 1, d[i-1][j-1] + c])
    return d[len(s1)][len(s2)]


def test():
    s1 = 'short'
    s2 = 'portS'
    assert get_edit_dist(s1, s2) == 3


def main():
    s1 = input()
    s2 = input()
    print(str(get_edit_dist(s1, s2)))


if __name__ == "__main__":
    main()
    # test()