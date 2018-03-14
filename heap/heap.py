class Heap:
    def __init__(self):
        self.array = []

    def insert(self, e):
        self.array.append(e)
        cur_ind = len(self.array) - 1
        cur_parent = int(cur_ind / 2)
        while self.array[cur_ind] > self.array[cur_parent]:
            tmp = self.array[cur_ind]
            self.array[cur_ind] = self.array[cur_parent]
            self.array[cur_parent] = tmp
            cur_ind = cur_parent
            cur_parent = int(cur_ind / 2)

    def extract_max(self):
        max = self.array[0]
        if self.array[1] > self.array[2]:
            next_max_ind = 1
        else:
            next_max_ind = 2



def main():
    heap = Heap()
    heap.insert(100)
    heap.insert(101)
    heap.insert(104)
    heap.insert(103)
    print(heap.array)


if __name__ == "__main__":
    main()