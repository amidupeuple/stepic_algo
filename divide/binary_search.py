class IndexFinder:
    def __init__(self, ref_arr):
        self.ref_arr = ref_arr

    def find(self, arr):
        result_indexes = []
        for i in range(len(arr)):
            cur_ind = -2
            l = 0
            r = len(self.ref_arr) - 1
            while l <= r:
                m = int((l + r) / 2)
                if self.ref_arr[m] == arr[i]:
                    cur_ind = m
                    break
                elif self.ref_arr[m] > arr[i]:
                    r = m - 1
                elif self.ref_arr[m] < arr[i]:
                    l = m + 1
            result_indexes.append(cur_ind + 1)
        return " ".join([str(x) for x in result_indexes])


if __name__ == "__main__":
    a1 = [int(x) for x in input().split(" ")]
    n1 = a1[0]
    a1 = a1[1:]
    assert n1 == len(a1)

    a2 = [int(x) for x in input().split(" ")]
    n2 = a2[0]
    a2 = a2[1:]
    assert n2 == len(a2)

    '''a1 = [1, 5, 8, 12, 13]
    a2 = [8, 1, 23, 1, 11]'''

    index_finder = IndexFinder(a1)
    print(index_finder.find(a2))