import sys

cnt = 0


def merge(a, b):
    res = []
    while a and b:
        global cnt
        if a[0] <= b[0]:
            res.append(a.pop(0))
        else:
            cnt += len(a)
            res.append(b.pop(0))
    res.extend(a or b)
    return res


def merge_sort(a):
    if len(a) > 1:
        m = len(a) // 2
        return merge(merge_sort(a[:m]), merge_sort(a[m:]))
    return a


def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    next(reader)
    arr = list(next(reader))
    merge_sort(arr)
    print(cnt)


if __name__ == "__main__":
    main()