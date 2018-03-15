class Heap:
    def __init__(self):
        self.array = []

    def insert(self, e):
        self.array.append(e)
        cur_ind = len(self.array) - 1
        cur_parent = int((cur_ind+1) / 2 - 1)
        while self.array[cur_ind] > self.array[cur_parent]:
            tmp = self.array[cur_ind]
            self.array[cur_ind] = self.array[cur_parent]
            self.array[cur_parent] = tmp
            cur_ind = cur_parent
            cur_parent = int((cur_ind+1) / 2 - 1)

    def extract_max(self):
        if len(self.array) > 0:
            max_vertex = self.array[0]

            if len(self.array) == 1:
                del self.array[0]
                return max_vertex

            self.array[0] = self.array[len(self.array)-1]
            del self.array[len(self.array)-1]

            if len(self.array) >= 3:
                max_child_ind = 1 if self.array[1] > self.array[2] else 2
            elif len(self.array) == 2:
                max_child_ind = 1
            elif len(self.array) == 1:
                return max_vertex

            cur_vertex_ind = 0
            while self.array[max_child_ind] > self.array[cur_vertex_ind]:
                tmp = self.array[cur_vertex_ind]
                self.array[cur_vertex_ind] = self.array[max_child_ind]
                self.array[max_child_ind] = tmp
                cur_vertex_ind = max_child_ind
                left_ind = ((cur_vertex_ind + 1) * 2) - 1
                right_ind = left_ind + 1
                if left_ind < (len(self.array)-1) and right_ind <= (len(self.array)-1):
                    max_child_ind = left_ind if self.array[left_ind] > self.array[right_ind] else right_ind
                elif left_ind == (len(self.array)-1):
                    max_child_ind = left_ind
                else:
                    break

            return max_vertex


def main():
    heap = Heap()
    command_list = []

    n = int(input())
    for i in range(n):
        input_str = input()
        if "Insert" in input_str:
            command, numb = input_str.split()
            numb = int(numb)
        else:
            command = input_str
            numb = None
        command_list.append((command, numb))

    '''command_list.append(("Insert", 200))
    command_list.append(("Insert", 10))
    command_list.append(("ExtractMax", None))
    command_list.append(("Insert", 5))
    command_list.append(("Insert", 500))
    command_list.append(("ExtractMax", None))'''

    for com, num in command_list:
        if com == "Insert":
            heap.insert(num)
        elif com == "ExtractMax":
            print(heap.extract_max())


if __name__ == "__main__":
    main()